from fastapi import APIRouter
from starlette import status

from api.databases.announcement import retrieve_announcements, retrieve_announcement
from api.schemas.response import (
    success_response,
    error_response,
)

responses = {}

router = APIRouter()


@router.get(
    path='/announcements',
    summary='Get list of announcements',
    operation_id='AnnouncementsList',
    description='Returns all existing announcements.',
    tags=['Announcements'],
    status_code=status.HTTP_200_OK,
    responses={**responses},
)
async def get_announcements():
    announcements = await retrieve_announcements()
    return success_response(
        data=announcements,
        details='announcements successfully retrieved',
    )


@router.get(
    path='/announcements/{announcement_id:int}',
    summary='Get the announcement',
    operation_id='AnnouncementDetail',
    description='Returns the concrete announcement using ID parameter.',
    tags=['Announcements'],
    status_code=status.HTTP_200_OK,
    responses={**responses},
)
async def get_announcement(announcement_id):
    announcement = await retrieve_announcement(announcement_id)
    if announcement:
        return success_response(
            data=announcement,
            details='announcement successfully retrieved',
        )
    return error_response(
        name='Not Found',
        code=4,
        details='announcement not found'
    )
