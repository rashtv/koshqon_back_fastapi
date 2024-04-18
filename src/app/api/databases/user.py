from datetime import datetime
from typing import List

from api.databases.db_client import (
    users_collection,
)


def user_helper(user) -> dict:
    return {
        'id': user['_id'],
        # 'password': user['password'],
        'phone': user['phone'],
        'active': user['active'],
        'profile_id': user['profile_id'],
        # 'created_at': datetime.strptime(user['created_at'], '%Y-%m-%d %H:%M:%S.%f'),
        'created_at': str(user['created_at']),
        'created_by': user['created_by'],
        # 'updated_at': datetime.strptime(user['updated_at'], '%Y-%m-%d %H:%M:%S.%f'),
        'updated_at': str(user['updated_at']),
        'updated_by': user['updated_by'],
    }


async def retrieve_users() -> List:
    users = []
    async for user in users_collection.find():
        users.append(user_helper(user))
    return users


async def retrieve_user(user_id: int) -> dict:
    user = await users_collection.find_one({"_id": user_id})
    if user:
        return user_helper(user)
