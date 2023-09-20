from fastapi import APIRouter, status

from schema.auth import AuthSchemaInput
from service.authentication_service import AuthenticationService

router = APIRouter()


@router.post(
    "",
    response_model=str,
    status_code=status.HTTP_200_OK,
    name="auth"
)
async def auth(auth_input:AuthSchemaInput):
    return AuthenticationService().authenticate_user(auth_input)