from dal.role_dal import RoleDal


class RoleService(object):

    def __init__(self):
        self.dal = RoleDal()

    def get_all_roles(self):
        return self.dal.get_all_roles()