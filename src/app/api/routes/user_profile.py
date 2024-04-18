from fastapi import APIRouter
from starlette import status


from api.databases.user_profile import (
    retrieve_user_profiles,
    retrieve_user_profile,
    retrieve_user_favorites,
    retrieve_friends,
    retrieve_user_announcements,
)
from api.schemas.response import (
    success_response,
    error_response,
)

responses = {
    # 200: {'message': 'Success'},
    # 404: {'message': 'Not Found'},
}

router = APIRouter()


@router.get(
    path='/user_profiles',
    summary='Get list of user profiles',
    operation_id='UserProfilesList',
    description='Returns all existing user profiles.',
    tags=['UserProfiles'],
    status_code=status.HTTP_200_OK,
    responses={**responses},
)
async def get_user_profiles():
    user_profiles = await retrieve_user_profiles()
    return success_response(
        data=user_profiles,
        details='user profiles successfully retrieved',
    )


@router.get(
    path='/user_profiles/{user_profile_id:int}',
    summary='Get the user profile',
    operation_id='UserProfileDetail',
    description='Returns the concrete user profile using ID parameter.',
    tags=['UserProfiles'],
    status_code=status.HTTP_200_OK,
    responses={**responses},
)
async def get_user_profile(user_profile_id):
    user_profile = await retrieve_user_profile(user_profile_id)
    if user_profile:
        return success_response(
            data=user_profile,
            details='user profile successfully retrieved',
        )
    return error_response(
        name='Not Found',
        code=4,
        details='user profile not found'
    )


@router.get(
    path='/user_profiles/{user_profile_id:int}/announcements',
    summary='Get user announcements',
    operation_id='UserAnnouncements',
    description='Returns announcements of the user',
    tags=['UserProfiles'],
    status_code=status.HTTP_200_OK,
    responses={**responses},
)
async def get_user_announcements(user_profile_id: int):
    announcements = await retrieve_user_announcements(user_profile_id)
    return success_response(
        data=announcements,
        details='announcements successfully retrieved',
    )


@router.get(
    path='/user_profiles/{user_profile_id:int}/friends',
    summary='Get user friends',
    operation_id='Friends',
    description='Returns friends of user',
    tags=['UserProfiles'],
    status_code=status.HTTP_200_OK,
    responses={**responses},
)
async def get_user_friends(user_profile_id: int):
    friends = await retrieve_friends(user_profile_id)
    return success_response(
        data=friends,
        details='friends successfully retrieved',
    )


@router.get(
    path='/user_profiles/{user_profile_id:int}/favorites',
    summary='Get user favorites',
    operation_id='FavoriteAnnouncements',
    description='Returns favorite announcements of user',
    tags=['UserProfiles'],
    status_code=status.HTTP_200_OK,
    responses={**responses},
)
async def get_user_favorites(user_profile_id: int):
    favorites = await retrieve_user_favorites(user_profile_id)
    return success_response(
        data=favorites,
        details='favorites successfully retrieved'
    )
