from models.role import Role
from utils.db_connector import get_session


class RoleDal(object):

    def __init__(self):
        self.model = Role


    def get_all_roles(self):
        session = get_session()
        roles = session.query(self.model).all()
        session.close()
        return roles

