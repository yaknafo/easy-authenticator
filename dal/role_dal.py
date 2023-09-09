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

    def create_role(self, role: Role) -> Role:
        session = get_session()
        session.add(role)
        session.commit()
        role_db = session.query(self.model).filter_by(name=role.name).first()
        session.close()
        return role_db

    def update_role(self, role: Role) -> Role:
        session = get_session()

        # Check if the role with the same identifier (e.g., role name) exists
        existing_role = session.query(self.model).filter_by(name=role.name).first()
        if existing_role:
            # Update the attributes of the existing role with the new values
            existing_role.token = role.token  # Update other attributes as needed

            # Commit the changes to the database
            session.commit()
            updated_role = session.query(self.model).filter_by(name=role.name).first()
            session.close()

            return updated_role
        else:
            session.close()
            # Handle the case where the role doesn't exist (e.g., raise an exception or return an error message)
            raise Exception("Role not found")

    def delete_role(self, role: Role) -> None:
        session = get_session()

        # Query the database to find the role by its ID
        role = session.query(Role).filter_by(id=role.id, name=role.name ).first()

        if role:
            # Delete the role
            session.delete(role)

            # Commit the deletion
            session.commit()
            session.close()
        else:
            session.close()
            # Handle the case


