# aiohttp-route
`@route` decorator for aiohttp.web that actually needs no singletons

## Install

```sh
pip install aiohttp_route
```

## Example

### Basic

File structure:

.
└── src
     ├ views.py
     └ run.py

`run.py`:

```py
from aiohttp import web
from aiohttp_route import router


app = web.Application()
routes = router(app, ['views'])
web.run_app(app, host='127.0.0.1', port=8080)
```

`views.py`:

```py
from aiohttp import web
from aiohttp_route import route


@route('GET', '/')
def handler(request):
    return web.HTTPNoContent()
```

## With name spaces

File structure:

.
└── src
     └ my_app
         ├ __init__.py
         ├ views.py
         └ run.py

`run.py`:

 ```py
 from aiohttp import web
 from aiohttp_route import router


 app = web.Application()
 routes = router(app, ['my_app.views'])
 web.run_app(app, host='127.0.0.1', port=8080)
 ```

 `views.py`:

 ```py
 from aiohttp import web
 from aiohttp_route import route


 @route('GET', '/')
 def handler(request):
     return web.HTTPNoContent()
 ```
