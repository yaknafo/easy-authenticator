from fastapi import APIRouter

from api.routes.auth import router as auth_router

router = APIRouter()


router.include_router(auth_router, prefix="/auth")