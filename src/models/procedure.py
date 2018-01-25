# coding: utf-8
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Procedure(Base):
    id = Column(Integer, primary_key=True, nullable=False),
    name = Column(String(255), nullable=False),
    active = Column(Boolean, default=True, nullable=False)
