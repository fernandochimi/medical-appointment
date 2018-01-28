# coding: utf-8
from aiohttp.test_utils import unittest_run_loop
from aiohttp import web

from src.tests import BaseTest


class PatientTest(BaseTest):
    @unittest_run_loop
    async def test_01_get_patients(self):
        request = await self.client.request("GET", "/patients")
        print(request)
        assert request.status == 200
