# coding: utf-8
from aiohttp import web
from sqlalchemy import Column, DateTime, ForeignKey, func, Integer, Table

from models.base import META, RecordNotFound,\
    DataTypeError, DateValidationError
from utils import validate_int_values, _format_string_to_datetime


appointment = Table(
    "appointment", META,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("patient_id", Integer, ForeignKey("patient.id"), nullable=False),
    Column("procedure_id", Integer,
           ForeignKey("procedure.id"), nullable=False),
    Column("start_date", DateTime(timezone=True),
           default=func.now(), nullable=False),
    Column("end_date", DateTime(timezone=True))
)


def validate_date(data):
    start_date = _format_string_to_datetime(data["startDate"])
    end_date = _format_string_to_datetime(data["endDate"])
    time_now = _format_string_to_datetime(
        datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))

    if args.startDate < time_now:
        msg = "Start date cannot be less than current date"
        raise DateValidationError(msg)

    if args.startDate > args.endDate:
        msg = "Start date cannot be more than end date"
        raise DateValidationError(msg)


async def get_appointment(conn, request):
    appointment_id = validate_int_values(
        request.match_info["appointment_id"])
    if appointment_id is False:
        msg = "This is not a valid id for appointment"
        raise DataTypeError(msg)

    result = await conn.execute(
        appointment.select()
        .where(appointment.c.id == appointment_id))
    appointment_data = await result.first()

    if not appointment_data:
        msg = "Appointment with id: {} does not exists"
        raise RecordNotFound(msg.format(appointment_id))

    return appointment_data


async def create_appointment(conn, data):
    validate_date(data)
    result = await conn.execute(
        appointment.insert()
        .returning(*appointment.c)
        .values(
            patient_id=data["patientId"],
            procedure_id=data["procedureId"],
            start_date=data["startDate"],
            end_date=data["endDate"],
        )
    )
    record = await result.fetchall()
    if not record:
        msg = "Appointment not created"
        raise RecordNotFound(msg)


async def alter_appointment(conn, request, data):
    validate_date(data)
    appointment_id = validate_int_values(request.match_info["appointment_id"])
    result = await conn.execute(
        appointment.update()
        .returning(*appointment.c)
        .where(appointment.c.id == appointment_id)
        .values(
            patient_id=data["patientId"],
            procedure_id=data["procedureId"],
            start_date=data["startDate"],
            end_date=data["endDate"],
        )
    )
    record = await result.fetchone()
    if not record:
        msg = "Appointment with id: {} does not exists"
        raise RecordNotFound(msg.format(appointment_id))
    return record


async def delete_appointment(conn, request, data):
    appointment_id = validate_int_values(request.match_info["appointment_id"])
    result = await conn.execute(
        appointment.delete()
        .where(appointment.c.id == appointment_id)
    )
    if not result:
        msg = "Appointment with id: {} does not exists"
        raise RecordNotFound(msg.format(appointment_id))
    return result
