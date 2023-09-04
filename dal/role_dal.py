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

    def get_role_by_name(self, name: str) -> Role:
        session = get_session()
        role = session.query(self.model).filter(self.model.name == name).first()
        session.close()
        return role

