# coding: utf-8
from sqlalchemy import Boolean, Column, Date, Integer, \
    MetaData, String, Table, PrimaryKeyConstraint

meta = MetaData()

patient = Table(
    "patient", meta,
    Column("id", Integer, nullable=False),
    Column("first_name", String(255), nullable=False),
    Column("last_name", String(255), nullable=False),
    Column("cpf", String(14), nullable=False),
    Column("date_of_birth", Date, nullable=False),
    Column("gender", Boolean, nullable=False),
    Column("active", Boolean, nullable=False)
)

PrimaryKeyConstraint("id", name="patient_id_pkey")
