# # coding: utf-8
# import unittest

# from aiohttp.test_utils import RawTestServer
# from aiohttp import web


# # class MyAppTestCase(AioHTTPTestCase):
# async def test_my_server(test_server):
#     app = web.Application()
#     server = await test_server(app)

# if __name__ == '__main__':
#     unittest.main()
"""HTTP client functional tests against aiohttp.web server"""
import unittest


class TestPatient(unittest.TestCase):
    def test_01(self):
        self.assertEqual('foo'.upper(), 'FOO')
