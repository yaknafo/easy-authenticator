from fastapi import APIRouter, status

from schema.auth import AuthSchemaInput
from service.authentication_service import AuthenticationService
import service.tyk_token.tyk_helper as t_helper
router = APIRouter()


@router.post(
    "",
    response_model=str,
    status_code=status.HTTP_200_OK,
    name="auth"
)
async def auth(auth_input:AuthSchemaInput):
    return AuthenticationService().authenticate_user(auth_input)


@router.get(
    "",

    status_code=status.HTTP_200_OK,
    name="create_endpoint"
)
async def create_endpoint():
    t_helper.create_endpoint()