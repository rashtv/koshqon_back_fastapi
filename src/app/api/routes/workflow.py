from fastapi import APIRouter
from starlette import status

from api.databases.workflow import retrieve_cities
from api.schemas.response import success_response

responses = {}

router = APIRouter()


@router.get(
    path='/workflow/cities',
    summary='Get list of cities',
    operation_id='CitiesList',
    description='Returns all existing cities.',
    tags=['Workflow'],
    status_code=status.HTTP_200_OK,
    responses={**responses},
)
async def get_cities():
    cities = await retrieve_cities()
    return success_response(
        data=cities,
        details='cities successfully retrieved',
    )
