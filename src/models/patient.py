# coding: utf-8
from sqlalchemy import Boolean, Column, Date, Integer, String, Table

from models import META


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
