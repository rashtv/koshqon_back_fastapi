import environ  # noqa
from decouple import config # noqa


@environ.config(prefix='')
class AppConfig:
    @environ.config(prefix='API')
    class API:
        title = 'KoshQon FastAPI'
        description = 'Reading Part of KQ Backend. Fast API version.'
        version = '0.0.1'
        prefix = None
        debug = config('DEBUG', cast=bool)
        allowed_hosts = None
        key = None

    @environ.config(prefix='MONGO')
    class Mongo:
        atlas = config('_MONGO_ATLAS')
        details = config('MONGO_DETAILS')

    @environ.config(prefix='PSQL')
    class PostgreSQL:
        url = config('PSQL_URL')
        uri = config('PSQL_URI')
        username = config('PSQL_USERNAME')
        password = config('PSQL_PASSWORD')
        port = config('PSQL_PORT')

    api: API = environ.group(API)
    mongo: Mongo = environ.group(Mongo)
    psql: PostgreSQL = environ.group(PostgreSQL)

app_config: AppConfig = AppConfig.from_environ()  # noqa
