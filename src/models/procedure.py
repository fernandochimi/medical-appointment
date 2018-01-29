# coding: utf-8
from sqlalchemy import Boolean, Column, Integer, String, Table

from models.base import META, RecordNotFound
from utils import validate_int_values


procedure = Table(
    "procedure", META,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String(255), nullable=False),
    Column("active", Boolean, default=True, nullable=False)
)


async def get_procedure(conn, request):
    procedure_id = validate_int_values(request.match_info["procedure_id"])
    if procedure_id is False:
        msg = "This is not a valid id for procedure"
        raise DataTypeError(msg)

    result = await conn.execute(
        procedure.select()
        .where(procedure.c.id == procedure_id))
    procedure_data = await result.first()

    if not procedure_data:
        msg = "Patient with id: {} does not exists"
        raise RecordNotFound(msg.format(procedure_id))

    return dict(procedure_data.items())


async def create_procedure(conn, data):
    result = await conn.execute(
        procedure.insert()
        .returning(*procedure.c)
        .values(
            name=data["name"],
            active=data["active"],
        )
    )
    record = await result.fetchone()
    if not record:
        msg = "Patient not created"
        raise RecordNotFound(msg)
    return record


async def alter_procedure(conn, request, data):
    procedure_id = validate_int_values(request.match_info["procedure_id"])
    result = await conn.execute(
        procedure.update()
        .returning(*procedure.c)
        .where(procedure.c.id == procedure_id)
        .values(
            name=data["name"],
            active=data["active"],
        )
    )
    record = await result.fetchone()
    if not record:
        msg = "Patient with id: {} does not exists"
        raise RecordNotFound(msg.format(procedure_id))
    return record


async def delete_procedure(conn, request, data):
    procedure_id = validate_int_values(request.match_info["procedure_id"])
    result = await conn.execute(
        procedure.delete()
        .where(procedure.c.id == procedure_id)
    )
    if not result:
        msg = "Patient with id: {} does not exists"
        raise RecordNotFound(msg.format(procedure_id))
    return result
