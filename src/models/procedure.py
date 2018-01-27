# coding: utf-8
from sqlalchemy import Boolean, Column, Integer, String, Table

from models import META


procedure = Table(
    "procedure", META,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String(255), nullable=False),
    Column("active", Boolean, default=True, nullable=False)
)
