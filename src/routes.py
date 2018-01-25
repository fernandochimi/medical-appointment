# coding: utf-8
from resources.appointments import index


def setup_routes(app):
    app.router.add_get("/", index)
