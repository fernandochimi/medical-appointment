# coding: utf-8
import asyncio
import logging
import sys

from aiohttp import web
from aiohttp_swagger import *

from models.base import init_pg, close_pg
from routes import setup_routes
from utils import import_env_variables


def init(loop, argv):
    app = web.Application(loop=loop)

    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    setup_routes(app)

    setup_swagger(
        app,
        description="""
        This is a API that allows to create,
        alter, consult and delete medical appointments,
        procedures and patients.
        """,
        title="Medical Appointments",
        api_version="1.0.0",
        swagger_url="/medical-api-docs")

    return app


def main(argv):
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    app = init(loop, argv)
    web.run_app(
        app,
        host=import_env_variables("HOST"),
        port=int(import_env_variables("PORT")))


if __name__ == "__main__":
    main(sys.argv[1:])
