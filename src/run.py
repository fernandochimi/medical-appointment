# coding: utf-8
import argparse
import asyncio
import logging
import sys

from aiohttp import web
from trafaret_config import commandline

from models import init_pg, close_pg
from routes import setup_routes
from utils import TRAFARET


def init(loop, argv):
    ap = argparse.ArgumentParser()
    commandline.standard_argparse_options(
        ap, default_config='./config/db.yml')
    options = ap.parse_args(argv)

    config = commandline.config_from_options(options, TRAFARET)

    app = web.Application(loop=loop)

    app['config'] = config

    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    setup_routes(app)

    return app


def main(argv):
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    app = init(loop, argv)
    web.run_app(app, host=app["config"]["host"], port=app["config"]["port"])


if __name__ == "__main__":
    main(sys.argv[1:])
