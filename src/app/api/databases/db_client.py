import psycopg2
import motor.motor_asyncio

from config.settings import app_config

# MongoDB
# client = motor.motor_asyncio.AsyncIOMotorClient(app_config.mongo.atlas)
client = motor.motor_asyncio.AsyncIOMotorClient(app_config.mongo.details)

database = client.get_database('koshqon')

announcements_collection = database.get_collection('announcements')
announcement_types_collection = database.get_collection('announcement_type')
favorites_collection = database.get_collection('favorites')
user_profiles_collection = database.get_collection('profiles')
user_characteristics_collection = database.get_collection('characteristics')
users_collection = database.get_collection('users')
friends_collection = database.get_collection('connections')

# workflow collections
cities_collection = database.get_collection('cities')

# PostgreSQL
conn = psycopg2.connect(app_config.psql.url)


def update_mongo(table_name: str, entity_id: int):
    collection = database.get_collection(table_name)
    cur = conn.cursor()
    try:
        cur.execute(f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_schema = 'public'  -- or your schema name
            AND {table_name} = 'your_table_name';
        """)
        column_names = cur.fetchone()

    except psycopg2.Error as e:
        print('Probably this table does not exist.')
        print(dir(e))

    try:
        cur.execute(
            f"SELECT * "
            f"FROM {table_name} "
            f"WHERE id = {entity_id}"
        )
        row = cur.fetchone()
        data = dict()
        for key, val in zip(column_names, row): # noqa
            data[key] = val
        collection.insert_one(**data)

    except psycopg2.Error as e:
        print(f'Tried to get from {table_name} row with id = {entity_id}')
        print(dir(e))
    finally:
        cur.close()
        conn.close()
