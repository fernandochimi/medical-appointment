# coding: utf-8
from aiohttp import web

from models.appointment import appointment


class AppointmentResource:
    def __init__(self):
        pass

    async def get_appointments(self, request):
        async with request.app['db'].acquire() as conn:
            cursor = await conn.execute(appointment.select())
            records = await cursor.fetchall()
            appointments = [dict(q) for q in records]
            data = {'appointments': appointments}
            return web.json_response(data)
