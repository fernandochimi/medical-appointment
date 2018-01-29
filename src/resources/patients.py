# coding: utf-8
from aiohttp import web

from models.base import RecordNotFound, DataTypeError
from models.patient import alter_patient, create_patient,\
    delete_patient, get_patient, patient
from utils import json_handler


class PatientResource:
    def __init__(self):
        pass

    async def get_list(self, request):
        async with request.app['db'].acquire() as conn:
            cursor = await conn.execute(patient.select())
            records = await cursor.fetchall()
            patients = [dict(q) for q in records]
            data = {'patients': patients}
            return web.json_response(json_handler(data))

    async def get_detail(self, request):
        async with request.app['db'].acquire() as conn:
            try:
                patient = await get_patient(conn, request)
            except RecordNotFound as e:
                raise web.HTTPNotFound(text=str(e))
            except TypeError:
                return web.HTTPServerError(text=str(DataTypeError))
            return web.json_response(json_handler(patient))

    async def register(self, request):
        async with request.app["db"].acquire() as conn:
            data = await request.json()
            try:
                new_patient = await create_patient(conn, data)
            except RecordNotFound as e:
                raise web.HTTPNotFound(text=str(e))
            router = request.app.router
            url = router["patient_detail"].url(parts={
                "patient_id": new_patient.id})
            return web.HTTPFound(location=url)

    async def alter(self, request):
        async with request.app['db'].acquire() as conn:
            data = await request.json()
            update_patient = await alter_patient(conn, request, data)
            router = request.app.router
            url = router["patient_detail"].url(parts={
                "patient_id": update_patient.id})
            return web.HTTPFound(location=url)

    async def delete(self, request):
        async with request.app['db'].acquire() as conn:
            data = await request.json()
            update_patient = await delete_patient(conn, request, data)
            return web.HTTPNoContent()
