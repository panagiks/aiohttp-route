from aiohttp import web
from aiohttp_route import route


@route('GET', '/')
def handler(request):
    return web.HTTPNoContent()
