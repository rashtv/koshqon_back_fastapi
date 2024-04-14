from fastapi import APIRouter

from api.routes.announcement import router as announcement_router
from api.routes.user import router as user_router
from api.routes.user_profile import router as user_profile_router
from api.routes.updater import router as mongo_updater_router
from api.routes.workflow import router as workflow_router

api_router = APIRouter(prefix='/api/v1')

api_router.include_router(announcement_router)
api_router.include_router(user_router)
api_router.include_router(user_profile_router)
api_router.include_router(mongo_updater_router)
api_router.include_router(workflow_router)
