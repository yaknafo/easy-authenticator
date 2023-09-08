from fastapi import APIRouter

from api.routes.auth import router as auth_router
from api.routes.role import router as role_router
from api.routes.user import router as user_router


router = APIRouter()


router.include_router(auth_router, prefix="/auth")
router.include_router(role_router, prefix="/role")
router.include_router(user_router, prefix="/user")