# coding: utf-8
from sqlalchemy import Boolean, Column, Integer, \
    MetaData, String, Table, PrimaryKeyConstraint

meta = MetaData()

procedure = Table(
    "procedure", meta,
    Column("id", Integer, nullable=False),
    Column("name", String(255), nullable=False),
    Column("active", Boolean, nullable=False)
)

PrimaryKeyConstraint("id", name="procedure_id_pkey")
