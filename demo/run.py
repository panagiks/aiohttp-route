from aiohttp import web
from aiohttp_route import router


app = web.Application()
# `router` function returns an array of routes, allowing to i.e. apply CORS
routes = router(app, ['views'])
web.run_app(app, host='127.0.0.1', port=8080)
