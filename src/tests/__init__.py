# coding: utf-8
from aiohttp.test_utils import AioHTTPTestCase
from aiohttp import web

TEST_DB = "sqlite:///memory"


class BaseTest(AioHTTPTestCase):
    async def get_application(self):
        return web.Application()
