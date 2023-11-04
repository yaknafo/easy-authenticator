import os

import bcrypt
import service.tyk_token.tyk_helper as tyk_helper

from schema.auth import AuthSchemaInput
from service.redis_client import RedisClient
from service.role_service import RoleService
from service.user_service import UserService
import secrets
import string

TOKEN_LENGTH = 32
TYK_AUTH = os.getenv('TYK_AUTH', False)


def _generate_random_token():
    # Define the characters to use for generating the token
    characters = string.ascii_letters + string.digits
    # Generate a random token with the specified length
    token = ''.join(secrets.choice(characters) for _ in range(TOKEN_LENGTH))
    return token


class AuthenticationService:

    def __init__(self):
        self.redis_client = RedisClient()

    def authenticate_user(self, auth_input: AuthSchemaInput):
        user = UserService().auth_user(user_name=auth_input.user_name, password=auth_input.password)
        if user:
            stored_hashed_password_bytes = bytes.fromhex(user.password[2:])
            if bcrypt.checkpw(auth_input.password.encode("utf-8"), stored_hashed_password_bytes):
                if TYK_AUTH:
                    role = RoleService().get_role_by_id(user.role_id)
                    return tyk_helper.create_key([n.api_id for n in role.endpoint])
                else:
                    auth_token = _generate_random_token()
                    self.redis_client.set_token(auth_token, user.id)
                    return auth_token
        raise Exception("user not found")

    def check_token(self, auth_token: str):
        user_id = self.redis_client.get_key(auth_token)
        if user_id:
            return True
        return False
