# coding: utf-8
from sqlalchemy import Boolean, Column, Date, Integer, String, Table

from models import META, RecordNotFound
from utils import validate_int_values


patient = Table(
    "patient", META,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("first_name", String(255), nullable=False),
    Column("last_name", String(255), nullable=False),
    Column("cpf", String(14), nullable=False),
    Column("date_of_birth", Date, nullable=False),
    Column("gender", Boolean, nullable=False),
    Column("active", Boolean, default=True, nullable=False)
)


async def get_patient(conn, request):
    patient_id = validate_int_values(request.match_info["patient_id"])
    if patient_id is False:
        msg = "This is not a valid id for patient"
        raise DataTypeError(msg)

    result = await conn.execute(
        patient.select()
        .where(patient.c.id == patient_id))
    patient_data = await result.first()

    if not patient_data:
        msg = "Patient with id: {} does not exists"
        raise RecordNotFound(msg.format(patient_id))

    return dict(patient_data.items())


async def create_patient(conn, data):
    result = await conn.execute(
        patient.insert()
        .returning(*patient.c)
        .values(
            first_name=data["firstName"],
            last_name=data["lastName"],
            cpf=data["cpf"],
            date_of_birth=data["dateOfBirth"],
            gender=data["gender"],
            active=data["active"],
        )
    )
    record = await result.fetchone()
    if not record:
        msg = "Patient not created"
        raise RecordNotFound(msg)
    return record
