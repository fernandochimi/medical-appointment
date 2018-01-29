import unittest

import pytest
from aiohttp import web

from resources.patients import PatientResource as pr

JSON = [{
    "id": 1,
    "firstName": "Fernando",
    "lastName": "Chimicoviaki",
    "cpf": "000.000.000-00",
    "dateOfBirth": "1991-01-16",
    "gender": 0,
    "active": 1},
    {
    "id": 2,
    "firstName": "Maria",
    "lastName": "Carolina",
    "cpf": "000.000.000-00",
    "dateOfBirth": "1989-10-23",
    "gender": 1,
    "active": 1,
}]

JSON_DETAIL = {
    "id": 1,
    "firstName": "Fernando",
    "lastName": "Chimicoviaki",
    "cpf": "000.000.000-00",
    "dateOfBirth": "1991-01-16",
    "gender": 0,
    "active": 1}

JSON_REGISTER = {
    "id": 3,
    "firstName": "Novo",
    "lastName": "Usuário",
    "cpf": "000.000.000-00",
    "dateOfBirth": "1992-02-17",
    "gender": 0,
    "active": 1}


class TestPatient(unittest.TestCase):
    @pytest.fixture
    def cli(loop, test_client):
        app = web.Application()
        app.router.add_get(r"/patients", pr().get_list)
        app.router.add_get(
            r"/patients/{patient_id}".format(patient_id), pr().get_detail)
        app.router.add_post(r"/patients", pr().register)
        app.router.add_put(r"/patients/{patient_id}", pr().alter)
        app.router.add_delete(r"/patients/{patient_id}", pr().delete)
        return loop.run_until_complete(test_client(app))

    async def test_01_get_list(cli):
        cli.server.app["patients"] = JSON
        resp = await cli.get("/patients")
        assert resp.status == 200
        assert await resp.text() == JSON

    async def test_02_get_detail(cli):
        cli.server.app = JSON_DETAIL
        resp = await cli.get("/patients/{}".format(
            JSON_DETAIL["id"]))
        assert resp.status == 200
        assert await resp.text() == JSON_DETAIL

    async def test_03_register(cli):
        cli.server.app = JSON_REGISTER
        resp = await cli.post("/patients", data=JSON_REGISTER)
        assert resp.status == 302
        assert await resp.text() == JSON_REGISTER

    async def test_04_alter(cli):
        JSON_DETAIL["lastName"] = "Nascimento"
        cli.server.app = JSON_DETAIL
        resp = await cli.put("/patients/{}".format(
            JSON_DETAIL["id"]))
        assert resp.status == 302
        assert await resp.text() == JSON_DETAIL

    async def test_05_delete(cli):
        resp = await cli.delete("/patients/{}".format(
            JSON_DETAIL["id"]))
        assert resp.status == 204
        assert await resp.text() == ""
