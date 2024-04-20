import uvicorn
from loguru import logger
from decouple import config
from fastapi import FastAPI, Request, Depends
from prometheus_fastapi_instrumentator import Instrumentator, PrometheusFastApiInstrumentator
from starlette.middleware.cors import CORSMiddleware

from api.router import api_router
from config.settings import app_config

logger_format = (
    '{time:YYYY-MM-DD HH:mm:ss} |  '
    '{message} '
)

logger.remove()
logger.add(
    'logs/debug.json',
    format=logger_format,
    rotation='12:00',
    compression='zip'
)

app = FastAPI(
    title=app_config.api.title,
    debug=app_config.api.debug,
    version=app_config.api.version,
    description=app_config.api.description,
    openapi_url='/openapi.json',
    docs_url='/docs',
)

instrumentator: PrometheusFastApiInstrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

app.add_middleware(
    middleware_class=CORSMiddleware, # noqa
    allow_origins=app_config.api.allowed_hosts or ['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(api_router, prefix='')


async def logging_dependency(request: Request):
    ipaddress = f'{request.client.host : ^20} |'
    _request = f'{request.method} {str(request.url) : ^40} |'
    user_agent = f'{request.headers.get("User-Agent") : ^80}|'

    log_message = ipaddress + _request + user_agent
    logger.debug(log_message)

app.include_router(
    router=api_router,
    prefix='',
    dependencies=[Depends(logging_dependency)]
)

if __name__ == '__main__':
    uvicorn.run(
        app=config('FASTAPI_APP'),
        host=config('FASTAPI_HOST'),
        port=config('FASTAPI_PORT', cast=int),
        reload=config('RELOAD', cast=bool),
    )
