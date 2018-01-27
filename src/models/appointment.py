# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, func, Integer, Table

from models import META


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
