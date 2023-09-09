from models.role import User
from utils.db_connector import get_session


class UserDal(object):

    def __init__(self):
        self.model = User

    def get_all_users(self):
        session = get_session()
        users = session.query(self.model).all()
        session.close()
        return users

    def create_role(self, user: User) -> User:
        session = get_session()
        session.add(user)
        session.commit()
        new_user = session.query(self.model).filter_by(user_name=user.user_name).first()
        session.close()
        return new_user
