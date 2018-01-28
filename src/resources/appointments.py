# coding: utf-8
from aiohttp import web

from models import RecordNotFound, DataTypeError
from models.appointment import appointment, get_appointment,\
    create_appointment


class AppointmentResource:
    def __init__(self):
        pass

    async def get_list(self, request):
        async with request.app['db'].acquire() as conn:
            cursor = await conn.execute(appointment.select())
            records = await cursor.fetchall()
            appointments = [dict(q) for q in records]
            data = {'appointments': appointments}
            return web.json_response(data)

    async def get_detail(self, request):
        async with request.app['db'].acquire() as conn:
            try:
                appointment = await get_appointment(conn, request)
            except RecordNotFound as e:
                raise web.HTTPNotFound(text=str(e))
            except TypeError:
                return web.HTTPServerError(text=str(DataTypeError))
            return web.json_response(appointment)

    async def register(self, request):
        async with request.app['db'].acquire() as conn:
            data = await request.post()
            try:
                new_appointment = await create_appointment(conn, request)
            except RecordNotFound as e:
                raise web.HTTPNotFound(text=str(e))
            router = request.app.router
            url = router['results'].url(parts={
                'appointment_id': new_appointment.id})
            return web.HTTPFound(location=url)

    async def alter(self, request):
        async with request.app['db'].acquire() as conn:
            try:
                appointment = await get_appointment(conn, request)
            except RecordNotFound as e:
                raise web.HTTPNotFound(text=str(e))
            except TypeError:
                return web.HTTPServerError(text=str(DataTypeError))
            return web.json_response(appointment)

    async def delete(self, request):
        async with request.app['db'].acquire() as conn:
            try:
                appointment = await get_appointment(conn, request)
            except RecordNotFound as e:
                raise web.HTTPNotFound(text=str(e))
            except TypeError:
                return web.HTTPServerError(text=str(DataTypeError))
            return web.json_response(appointment)
