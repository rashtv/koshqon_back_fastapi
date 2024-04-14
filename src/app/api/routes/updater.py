from fastapi import APIRouter
from starlette import status

from api.databases.db_client import add_data_to_mongo
from api.schemas.response import (
    success_response,
    error_response,
)

responses = {}

router = APIRouter()


@router.post(
    path='/update_mongo/{table_name:str}/entity_id:int',
    summary='Update MongoDB via PostgreSQL data',
    operation_id='MongoUpdate',
    description='Update MongoDB via PostgreSQL data.',
    tags=['Mongo'],
    status_code=status.HTTP_200_OK,
    responses={**responses},
)
async def update_mongo(table_name: str, entity_id: int):
    await add_data_to_mongo(table_name, entity_id)
    return success_response(
        data=None,
        details='mongo updated',
    )
