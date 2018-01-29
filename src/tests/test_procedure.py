import unittest

import pytest
from aiohttp import web

from resources.procedures import ProcedureResource as pr

JSON = [{
    "id": 1,
    "name": "Procedure 1",
    "active": 1},
    {
    "id": 2,
    "name": "Procedure 2",
    "active": 1,
}]

JSON_DETAIL = {
    "id": 1,
    "name": "Procedure 1",
    "active": 1}

JSON_REGISTER = {
    "id": 3,
    "name": "Procedure 3",
    "active": 1}


class TestProcedure(unittest.TestCase):
    @pytest.fixture
    def cli(loop, test_client):
        app = web.Application()
        app.router.add_get(r"/procedures", pr().get_list)
        app.router.add_get(
            r"/procedures/{procedure_id}".format(
                procedure_id), pr().get_detail)
        app.router.add_post(r"/procedures", pr().register)
        app.router.add_put(r"/procedures/{procedure_id}", pr().alter)
        app.router.add_delete(r"/procedures/{procedure_id}", pr().delete)
        return loop.run_until_complete(test_client(app))

    async def test_01_get_list(cli):
        cli.server.app["procedures"] = JSON
        resp = await cli.get("/procedures")
        assert resp.status == 200
        assert await resp.text() == JSON

    async def test_02_get_detail(cli):
        cli.server.app = JSON_DETAIL
        resp = await cli.get("/procedures/{}".format(
            JSON_DETAIL["id"]))
        assert resp.status == 200
        assert await resp.text() == JSON_DETAIL

    async def test_03_register(cli):
        cli.server.app = JSON_REGISTER
        resp = await cli.post("/procedures", data=JSON_REGISTER)
        assert resp.status == 302
        assert await resp.text() == JSON_REGISTER

    async def test_04_alter(cli):
        JSON_DETAIL["name"] = "procedure (NEW)"
        cli.server.app = JSON_DETAIL
        resp = await cli.put("/procedures/{}".format(
            JSON_DETAIL["id"]))
        assert resp.status == 302
        assert await resp.text() == JSON_DETAIL

    async def test_05_delete(cli):
        resp = await cli.delete("/procedures/{}".format(
            JSON_DETAIL["id"]))
        assert resp.status == 204
        assert await resp.text() == ""
