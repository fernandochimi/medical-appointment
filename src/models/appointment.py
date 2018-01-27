# coding: utf-8
from aiohttp import web
from sqlalchemy import Column, DateTime, ForeignKey, func, Integer, Table

from models import META, RecordNotFound, DataTypeError
from utils import validate_int_values


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


async def get_appointment(conn, request):
    appointment_id = validate_int_values(request.match_info["appointment_id"])
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
