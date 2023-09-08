from fastapi import APIRouter, status

from schema.role import RoleSchema, RoleSchemaInput
from service.user_service import UserService

router = APIRouter()


@router.get(
    "/all",
    # response_model=list[RoleSchema],
    status_code=status.HTTP_200_OK,
    name="users"
)
async def users():
    return UserService().get_all_users()