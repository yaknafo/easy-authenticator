from fastapi import APIRouter, status, Depends
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from models.role import Role
from service.role_service import RoleService
from utils.db_connector import get_session

router = APIRouter()


@router.get(
    "/all",
#     response_model=list[BandRead],
    status_code=status.HTTP_200_OK,
    name="roles"
)
async def roles():
    return RoleService().get_all_roles();

@router.get(
    "",
    status_code=status.HTTP_200_OK,
    name="role"
)
async def get_role(role_name: str):
    return role_name


@router.post(
    "",
    status_code=status.HTTP_200_OK,
    name="create_role"
)
async def create_role(role_name: str):
    ## Adding role
    return role_name


@router.put(
    "",
    status_code=status.HTTP_200_OK,
    name="update_role"
)
async def update_role(role_name: str):
    ## upadate role
    return role_name

