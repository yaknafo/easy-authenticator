from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from schema.auth import AuthSchemaInput
from service.authentication_service import AuthenticationService
import service.tyk_token.tyk_helper as t_helper
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()


@router.post(
    "",
    response_model=str,
    status_code=status.HTTP_200_OK,
    name="auth"
)
async def auth(auth_input: AuthSchemaInput):
    return AuthenticationService().authenticate_user(auth_input)


@router.get(
    "/check",
    status_code=status.HTTP_200_OK,
    name="check_auth"
)
async def check_auth(token: str = Depends(oauth2_scheme)):
    if not AuthenticationService().check_token(token):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Authentication failed")
    return {"message": "Authentication successful"}


@router.get(
    "",

    status_code=status.HTTP_200_OK,
    name="create_endpoint"
)
async def create_endpoint():
    t_helper.create_endpoint()
