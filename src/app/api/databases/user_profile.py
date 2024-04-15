from datetime import datetime
from typing import List

from api.databases.announcement import (
    retrieve_announcement,
    retrieve_announcement_type,
    announcement_helper
)
from api.databases.db_client import (
    profiles_collection,
    profiles_images_collection,
    characteristics_collection,
    connections_collection,
    favorites_collection,
    announcements_collection,
)


def user_profile_helper(user_profile) -> dict:
    return {
        # 'id': user_profile['_id'],
        'first_name': user_profile['first_name'],
        'last_name': user_profile['last_name'],
        'country': user_profile['country'],
        'age': user_profile['age'],
        'biography': user_profile['biography'],
        'rating': user_profile['rating'],
        # 'created_at': datetime.strptime(user_profile['created_at'], '%Y-%m-%d %H:%M:%S.%f'),
        'created_at': str(user_profile['created_at']),
        'created_by': user_profile['created_by'],
        # 'updated_at': datetime.strptime(user_profile['updated_at'], '%Y-%m-%d %H:%M:%S.%f'),
        'updated_at': str(user_profile['updated_at']),
        'updated_by': user_profile['updated_by'],
        # 'birthdate': datetime.strptime(user_profile['birthdate'], '%Y-%m-%d'),
        'birthdate': str(user_profile['birthdate']),
        'gender': user_profile['gender'],
    }


def user_characteristics_helper(user_characteristics) -> dict:
    return {
        # 'id': user_characteristics['_id'],
        # 'profile_id': user_characteristics['profile_id'],
        'aspects': user_characteristics['aspects'],
        'interests': user_characteristics['interests'],
    }


def connection_helper(connection) -> dict:
    return {
        # 'id': connection['_id'],
        'profile_1': connection['profile_1'],
        'profile_2': connection['profile_2'],
        'connection_date': connection['connection_date'],
        'status': connection['status'],
    }


async def retrieve_user_characteristics(profile_id: int):
    user_characteristics = await characteristics_collection.find_one({'profile_id': profile_id})
    if user_characteristics:
        return user_characteristics_helper(user_characteristics)


async def retrieve_profile_image(profile_id: int):
    profile_image = await profiles_images_collection.find_one({'profile_id': profile_id})
    if profile_image:
        return profile_image


async def retrieve_user_profiles():
    user_profiles = []
    async for user_profile in profiles_collection.find():
        user_characteristics = await retrieve_user_characteristics(user_profile.get('_id'))
        profile_image = await retrieve_profile_image(user_profile.get('_id'))
        user_profile = user_profile_helper(user_profile)
        user_profile['characteristics'] = user_characteristics
        user_profile['image'] = profile_image
        user_profiles.append(user_profile)
    return user_profiles


async def retrieve_user_profile(profile_id: int):
    user_profile = await profiles_collection.find_one({'_id': profile_id})
    if user_profile:
        user_characteristics = await retrieve_user_characteristics(profile_id)
        profile_image = await retrieve_profile_image(user_profile.get('_id'))
        user_profile = user_profile_helper(user_profile)
        user_profile['characteristics'] = user_characteristics
        user_profile['image'] = profile_image
        return user_profile


async def retrieve_friends(profile_id: int) -> List:
    friends = []
    async for data in connections_collection.find({'profile_1': profile_id}):
        friend = await retrieve_user_profile(data.get('profile_2'))
        friends.append(friend)
    return friends


async def retrieve_user_favorites(profile_id: int) -> List:
    favorites = []
    async for data in favorites_collection.find({'profile_id': profile_id}):
        favorite = await retrieve_announcement(data.get('announcement_id'))
        favorites.append(favorite)
    return favorites


async def retrieve_user_announcements(profile_id: int) -> List:
    announcements = []
    async for announcement in announcements_collection.find({'profile_id': profile_id}):
        announcement_type = await retrieve_announcement_type(announcement.get('announcement_type'))
        announcement = announcement_helper(announcement)
        announcement['announcement_type'] = announcement_type
        announcements.append(announcement)
    return announcements
