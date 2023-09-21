import bcrypt
import service.tyk_token.tyk_helper as tyk_helper

from schema.auth import AuthSchemaInput
from service.role_service import RoleService
from service.user_service import UserService
import secrets


class AuthenticationService:

    def authenticate_user(self, auth_input:AuthSchemaInput):
        user = UserService().auth_user(user_name=auth_input.user_name, password= auth_input.password)
        if user:
            stored_hashed_password_bytes = bytes.fromhex(user.password[2:])
            if bcrypt.checkpw(auth_input.password.encode("utf-8"), stored_hashed_password_bytes):
                role = RoleService().get_role_by_id(user.role_id)
                return tyk_helper.create_key([n.api_id for n in role.endpoint])
                # return "aa"
        raise Exception("user not found")