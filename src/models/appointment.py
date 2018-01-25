# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, \
    MetaData, Table, PrimaryKeyConstraint, \
    ForeignKeyConstraint

from models.patient import patient
from models.procedure import procedure

meta = MetaData()

appointment = Table(
    "appointment", meta,
    Column("id", Integer, nullable=False),
    Column("patient_id", Integer, nullable=False),
    Column("procedure_id", Integer, nullable=False),
    Column("start_date", DateTime, nullable=False),
    Column("end_date", DateTime, nullable=False),
)

PrimaryKeyConstraint("id", name="appointment_id_pkey"),
ForeignKeyConstraint(
    ['patient_id'],
    [patient.c.id],
    name='patient_id_fkey',
    ondelete='CASCADE')
ForeignKeyConstraint(
    ['procedure_id'],
    [procedure.c.id],
    name='procedure_id_fkey',
    ondelete='CASCADE')
