from dal.role_dal import RoleDal
from models.role import Role


class RoleService(object):

    def __init__(self):
        self.dal = RoleDal()

    def get_all_roles(self):
        return self.dal.get_all_roles()

    def get_role_by_name(self, name: str) -> Role:
        assert name
        return self.dal.get_role_by_name(name)
