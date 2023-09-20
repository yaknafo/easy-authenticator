from dal.user_dal import UserDal
from models.models import User
from schema.user import UserSchemaInput
import bcrypt


class UserService(object):

    def __init__(self):
        self.dal = UserDal()

    def get_all_users(self):
        return self.dal.get_all_users()

    def create_user(self, user_schema: UserSchemaInput):
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user_schema.password.encode("utf-8"), salt)
        role_db = User(user_name=user_schema.user_name, role_id = user_schema.role_id, password=hashed_password)
        return self.dal.create_user(role_db)


    def update_user(self, user_schema: UserSchemaInput):
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user_schema.password.encode("utf-8"), salt).decode('utf-8')
        user_db = User(user_name=user_schema.user_name, role_id = user_schema.role_id, password=hashed_password)
        return self.dal.update_user(user_db)

    def delete_user(self, user_schema: UserSchemaInput):
        user_to_delete = User(user_name=user_schema.user_name, role_id = user_schema.role_id)
        self.dal.delete_user(user_to_delete)

    def get_user(self, user_schema: UserSchemaInput) -> User:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user_schema.password.encode("utf-8"), salt)
        user = User(user_name=user_schema.user_name, role_id=user_schema.role_id, password=hashed_password)
        return self.dal.get_user(user)

    def auth_user(self, user_name: str, password: str):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        user = User(user_name=user_name, password=hashed_password)
        return self.dal.get_user(user)


