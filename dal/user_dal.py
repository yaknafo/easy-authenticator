from models.user import User
from utils.db_connector import get_session


class UserDal(object):

    def __init__(self):
        self.model = User

    def get_all_users(self):
        session = get_session()
        roles = session.query(self.model).all()
        session.close()
        return roles