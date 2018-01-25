# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, func, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Appointment(Base):
    __tablename__ = "appointment"
    id = Column("id", Integer, primary_key=True, nullable=False)
    patient_id = Column(Integer, ForeignKey("patient.id"), nullable=False)
    procedure_id = Column(Integer, ForeignKey("procedure.id"), nullable=False)
    start_date = Column(DateTime, default=func.now(), nullable=False)
    end_date = Column(DateTime)
    patient = relationship("Patient")
    procedure = relationship("Procedure")
