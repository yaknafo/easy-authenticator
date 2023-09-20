from fastapi import APIRouter, status

from schema.role import RoleSchema, RoleSchemaInput, RoleEndpointSchema
from service.role_service import RoleService

router = APIRouter()


@router.get(
    "/all",
    # response_model=list[RoleSchema],
    status_code=status.HTTP_200_OK,
    name="roles"
)
async def roles():
    return RoleService().get_all_roles();

@router.get(
    "",
    response_model=RoleSchema,
    status_code=status.HTTP_200_OK,
    name="role"
)
async def get_role(role_name: str):
    return RoleService().get_role_by_name(role_name)


@router.post(
    "",
    response_model=RoleSchema,
    status_code=status.HTTP_201_CREATED,
    name="create_role"
)
async def create_role(role: RoleSchemaInput):
    return RoleService().create_role(role)


@router.put(
    "",
    response_model=RoleSchema,
    status_code=status.HTTP_200_OK,
    name="update_role"
)
async def update_role(role: RoleSchemaInput):
    return RoleService().update_role(role)


@router.delete(
    "",
    status_code=status.HTTP_204_NO_CONTENT,
    name="delete_role"
)
async def delete_role(role: RoleSchema):
    return RoleService().delete_role(role)

@router.post(
    "/add_endpoint",
    response_model=RoleSchema,
    status_code=status.HTTP_201_CREATED,
    name="add_endpoint"
)
async def add_endpoint_role(role_endpoint: RoleEndpointSchema):
    return RoleService().add_endpoint_to_role(role_endpoint)
