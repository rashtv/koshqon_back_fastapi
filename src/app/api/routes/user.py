from fastapi import APIRouter
from starlette import status

from api.databases.user import (
    retrieve_users,
    retrieve_user,
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
    path='/users',
    summary='Get list of users',
    operation_id='UsersList',
    description='Returns all existing users.',
    tags=['Users'],
    status_code=status.HTTP_200_OK,
    responses={**responses},
)
async def get_users():
    users = await retrieve_users()
    return success_response(
        data=users,
        details='users successfully retrieved',
    )


@router.get(
    path='/users/{user_id:int}',
    summary='Get the user',
    operation_id='UserDetail',
    description='Returns the concrete user using ID parameter.',
    tags=['Users'],
    status_code=status.HTTP_200_OK,
    responses={**responses},
)
async def get_user(user_id: int):
    user = await retrieve_user(user_id)
    if user:
        return success_response(
            data=user,
            details='user successfully retrieved',
        )
    return error_response(
        name='Not Found',
        code=4,
        details='user not found',
    )
