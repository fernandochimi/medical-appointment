# coding: utf-8
from aiohttp import web

from models.base import RecordNotFound, DataTypeError
from models.procedure import alter_procedure, create_procedure,\
    delete_procedure, get_procedure, procedure
from utils import json_handler


class ProcedureResource:
    def __init__(self):
        pass

    async def get_list(self, request):
        async with request.app['db'].acquire() as conn:
            cursor = await conn.execute(procedure.select())
            records = await cursor.fetchall()
            procedures = [dict(q) for q in records]
            data = {'procedures': procedures}
            return web.json_response(json_handler(data))

    async def get_detail(self, request):
        async with request.app['db'].acquire() as conn:
            try:
                procedure = await get_procedure(conn, request)
            except RecordNotFound as e:
                raise web.HTTPNotFound(text=str(e))
            except TypeError:
                return web.HTTPServerError(text=str(DataTypeError))
            return web.json_response(json_handler(procedure))

    async def register(self, request):
        async with request.app["db"].acquire() as conn:
            data = await request.json()
            try:
                new_procedure = await create_procedure(conn, data)
            except RecordNotFound as e:
                raise web.HTTPNotFound(text=str(e))
            router = request.app.router
            url = router["procedure_detail"].url(parts={
                "procedure_id": new_procedure.id})
            return web.HTTPFound(location=url)

    async def alter(self, request):
        async with request.app['db'].acquire() as conn:
            data = await request.json()
            update_procedure = await alter_procedure(conn, request, data)
            router = request.app.router
            url = router["procedure_detail"].url(parts={
                "procedure_id": update_procedure.id})
            return web.HTTPFound(location=url)

    async def delete(self, request):
        async with request.app['db'].acquire() as conn:
            data = await request.json()
            update_procedure = await delete_procedure(conn, request, data)
            return web.HTTPNoContent()
