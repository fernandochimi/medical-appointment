# coding: utf-8
import aiopg.sa
from sqlalchemy import MetaData

from utils import import_env_variables

META = MetaData()


async def init_pg(app):
    ENGINE = await aiopg.sa.create_engine(
        database=import_env_variables("DB_NAME"),
        user=import_env_variables("DB_USER"),
        password=import_env_variables("DB_PASS"),
        host=import_env_variables("DB_HOST"),
        port=import_env_variables("DB_PORT"))
    app["db"] = ENGINE


async def close_pg(app):
    app["db"].close()
    await app["db"].wait_closed()


class RecordNotFound(Exception):
    """Requested record in database was not found"""


class DataTypeError(Exception):
    """Data not compatible"""
