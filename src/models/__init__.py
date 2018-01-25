# coding: utf-8
import aiopg.sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool

ENGINE = await aiopg.sa.create_engine(
    database=conf['database'],
    user=conf['user'],
    password=conf['password'],
    host=conf['host'],
    port=conf['port'],
    minsize=conf['minsize'],
    maxsize=conf['maxsize'])

session = sessionmaker()
session.configure(bind=ENGINE)
Base.metadata.create_all(ENGINE)


async def init_pg(app):
    app['db'] = ENGINE


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
