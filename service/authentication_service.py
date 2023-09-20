import bcrypt

from schema.auth import AuthSchemaInput
from service.user_service import UserService
import secrets


class AuthenticationService():

    def authenticate_user(self, auth_input:AuthSchemaInput):
        user = UserService().auth_user(user_name=auth_input.user_name, password= auth_input.password)
        if user:
            stored_hashed_password_bytes = bytes.fromhex(user.password[2:])
            if bcrypt.checkpw(auth_input.password.encode("utf-8"), stored_hashed_password_bytes):
                return secrets.token_hex(32)
        raise Exception("user not found")