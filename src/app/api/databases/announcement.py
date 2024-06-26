from datetime import datetime
from typing import List

from api.databases.db_client import (
    announcements_collection,
    announcement_types_collection,
    announcements_images_collection,
)


def announcement_helper(announcement) -> dict:
    return {
        "id": announcement["_id"],
        "active": announcement["active"],
        "city": announcement["city"],
        "country": announcement["country"],
        "address": announcement["address"],
        "announcement_type": announcement["announcement_type"],
        "description": announcement["description"],
        "profile_id": announcement["profile_id"],
        # "created_at": datetime.strptime(announcement["created_at"], "%Y-%m-%d %H:%M:%S.%f"),
        "created_at": str(announcement["created_at"]),
        "created_by": announcement["created_by"],
        # "updated_at": datetime.strptime(announcement["updated_at"], "%Y-%m-%d %H:%M:%S.%f"),
        "updated_at": str(announcement["updated_at"]),
        "updated_by": announcement["updated_by"],
    }


def announcement_type_helper(announcement_type):
    return {
        # 'id': announcement_type['_id'],
        'name': announcement_type['name'],
        'description': announcement_type['description'],
    }


async def retrieve_announcement_type(announcement_type_id: int):
    announcement_type = await announcement_types_collection.find_one({'_id': announcement_type_id})
    return announcement_type_helper(announcement_type)


async def retrieve_announcement_images(announcement_id: int):
    announcement_images = await announcements_images_collection.find(
        {'announcements_id': announcement_id}
    ).to_list(length=None)
    if announcement_images:
        return announcement_images


async def retrieve_announcements() -> List:
    announcements = []
    async for announcement in announcements_collection.find():
        announcement_type = await retrieve_announcement_type(announcement.get('announcement_type'))
        announcement_images = await retrieve_announcement_images(announcement.get('_id'))
        announcement = announcement_helper(announcement)
        announcement['announcement_type'] = announcement_type
        announcement['images'] = announcement_images
        announcements.append(announcement)
    return announcements


async def retrieve_announcement(announcement_id: int) -> dict:
    announcement = await announcements_collection.find_one({"_id": announcement_id})
    if announcement:
        announcement_type = await retrieve_announcement_type(announcement.get('announcement_type'))
        announcement_images = await retrieve_announcement_images(announcement.get('_id'))
        announcement = announcement_helper(announcement)
        announcement['announcement_type'] = announcement_type
        announcement['images'] = announcement_images
        return announcement
