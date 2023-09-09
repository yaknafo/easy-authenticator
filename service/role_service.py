from dal.role_dal import RoleDal
from models.models import Role
from schema.role import RoleSchemaInput


class RoleService(object):

    def __init__(self):
        self.dal = RoleDal()

    def get_all_roles(self):
        return self.dal.get_all_roles()

    def get_role_by_name(self, name: str) -> Role:
        assert name
        return self.dal.get_role_by_name(name)

    def create_role(self, role_schema: RoleSchemaInput):
        role_db = Role(name=role_schema.name, token=role_schema.token)
        return self.dal.create_role(role_db)

    def update_role(self, role_schema: RoleSchemaInput):
        role_db = Role(name=role_schema.name, token=role_schema.token)
        return self.dal.update_role(role_db)

    def delete_role(self, role_schema: RoleSchemaInput):
        role_db = Role(id=role_schema.id, name=role_schema.name, token=role_schema.token)
        self.dal.delete_role(role_db)

