# coding: utf-8
from sqlalchemy import Boolean, Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Patient(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True, nullable=False),
    first_name = Column(String(255), nullable=False),
    last_name = Column(String(255), nullable=False),
    cpf = Column(String(14), nullable=False),
    date_of_birth = Column(Date, nullable=False),
    gender = Column(Boolean, nullable=False),
    active = Column(Boolean, default=True, nullable=False)
