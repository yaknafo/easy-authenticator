from fastapi import APIRouter, status

from schema.role import RoleSchema, RoleSchemaInput
from schema.user import UserSchema, UserSchemaInput
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



@router.post(
    "",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
    name="create_user"
)
async def create_role(user: UserSchemaInput):
    return UserService().create_user(user)

@router.put(
    "",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
    name="update_user"
)
async def update_role(user: UserSchemaInput):
    return UserService().update_user(user)


@router.delete(
    "",
    status_code=status.HTTP_204_NO_CONTENT,
    name="delete_user"
)
async def delete_role(user: UserSchemaInput):
    return UserService().delete_user(user)
