import psycopg2
import motor.motor_asyncio

from config.settings import app_config

# MongoDB
# client = motor.motor_asyncio.AsyncIOMotorClient(app_config.mongo.atlas)
client = motor.motor_asyncio.AsyncIOMotorClient(app_config.mongo.details)

database = client.get_database('koshqon')

announcement_types_collection = database.get_collection('announcement_type')
announcements_collection = database.get_collection('announcements')
announcements_images_collection = database.get_collection('announcements_images')
characteristics_collection = database.get_collection('characteristics')
connections_collection = database.get_collection('connections')
errors_collection = database.get_collection('errors')
favorites_collection = database.get_collection('favorites')
profiles_collection = database.get_collection('profiles')
profiles_images_collection = database.get_collection('profiles_images')
status_collection = database.get_collection('status_images')
users_collection = database.get_collection('users')

# workflow collections
cities_collection = database.get_collection('cities')

# PostgreSQL
conn = psycopg2.connect(app_config.psql.url)


async def add_data_to_mongo(table_name: str, entity_id: int):
    collection = database.get_collection(table_name)
    cur = conn.cursor()
    try:
        cur.execute(f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_schema = 'public'
            AND table_name = '{table_name}';
        """)
        columns = cur.fetchall()
        column_names = [col[0] for col in columns]
        column_names[0] = '_id'
    except psycopg2.Error as e:
        print('Probably this table does not exist.')
        print(dir(e))

    try:
        cur.execute(
            f"SELECT * "
            f"FROM {table_name} "
            f"WHERE id = {entity_id}"
        )
        row = cur.fetchall()
        data = dict()
        for key, val in zip(column_names, row): # noqa
            data[key] = val
        await collection.insert_one(**data)

    except psycopg2.Error as e:
        print(f'Tried to get from {table_name} row with id = {entity_id}')
        print(dir(e))
    finally:
        cur.close()
