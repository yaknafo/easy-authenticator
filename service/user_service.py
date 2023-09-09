from dal.user_dal import UserDal
from models.role import User
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
        return self.dal.create_role(role_db)
