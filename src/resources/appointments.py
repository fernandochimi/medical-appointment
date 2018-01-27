# coding: utf-8
from aiohttp import web

from models import RecordNotFound, DataTypeError
from models.appointment import appointment, get_appointment


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
            else:
                raise web.HTTPClientError(text=DataTypeError)
            return web.json_response(appointment)
