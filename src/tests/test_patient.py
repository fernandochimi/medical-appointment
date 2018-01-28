# coding: utf-8
from aiohttp import web

from .resources.patients import PatientResource


async def test_01_get_patients(raw_test_server):
    app = web.Application()
    app.router.add.get("/patients", PatientResource().get_list)
    client = await test_client(app)
    resp = await client.get('/patients')
    assert resp.status == 200
