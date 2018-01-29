import unittest

import pytest
from aiohttp import web

from resources.appointments import AppointmentResource as ap

JSON = [{
    "id": 1,
    "patientId": 1,
    "procedureId": 1,
    "startDate": "2018-02-20T13:00:00",
    "endDate": "2018-02-20T13:30:00"},
    {
    "id": 2,
    "patientId": 2,
    "procedureId": 1,
    "startDate": "2018-02-20T14:00:00",
    "endDate": "2018-02-20T14:30:00"}]

JSON_DETAIL = {
    "id": 2,
    "patientId": 2,
    "procedureId": 1,
    "startDate": "2018-02-20T14:00:00",
    "endDate": "2018-02-20T14:30:00"}

JSON_REGISTER = {
    "id": 3,
    "patientId": 3,
    "procedureId": 2,
    "startDate": "2018-02-20T15:00:00",
    "endDate": "2018-02-20T15:30:00"}


class TestAppointment(unittest.TestCase):
    @pytest.fixture
    def cli(loop, test_client):
        app = web.Application()
        app.router.add_get(r"/appointments", ap().get_list)
        app.router.add_get(
            r"/appointments/{appointment_id}".format(
                appointment_id), ap().get_detail)
        app.router.add_post(r"/appointments", ap().register)
        app.router.add_put(r"/appointments/{appointment_id}", ap().alter)
        app.router.add_delete(r"/appointments/{appointment_id}", ap().delete)
        return loop.run_until_complete(test_client(app))

    async def test_01_get_list(cli):
        cli.server.app["appointments"] = JSON
        resp = await cli.get("/appointments")
        assert resp.status == 200
        assert await resp.text() == JSON

    async def test_02_get_detail(cli):
        cli.server.app = JSON_DETAIL
        resp = await cli.get("/appointments/{}".format(
            JSON_DETAIL["id"]))
        assert resp.status == 200
        assert await resp.text() == JSON_DETAIL

    async def test_03_register(cli):
        cli.server.app = JSON_REGISTER
        resp = await cli.post("/appointments", data=JSON_REGISTER)
        assert resp.status == 302
        assert await resp.text() == JSON_REGISTER

    async def test_04_alter(cli):
        JSON_DETAIL["startDate"] = "2018-02-20T14:10:00"
        cli.server.app = JSON_DETAIL
        resp = await cli.put("/appointments/{}".format(
            JSON_DETAIL["id"]))
        assert resp.status == 302
        assert await resp.text() == JSON_DETAIL

    async def test_05_delete(cli):
        resp = await cli.delete("/appointments/{}".format(
            JSON_DETAIL["id"]))
        assert resp.status == 204
        assert await resp.text() == ""
