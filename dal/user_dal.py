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

    def update_user(self, user: User) -> User:
        session = get_session()

        # Check if the user with the same identifier (e.g., user name) exists
        existing_user = session.query(self.model).filter_by(user_name=user.user_name).first()
        if existing_user:
            # Update the attributes of the existing role with the new values
            existing_user.password = user.password  # Update other attributes as needed

            # Commit the changes to the database
            session.commit()
            updated_role = session.query(self.model).filter_by(user_name=user.user_name).first()
            session.close()

            return updated_role
        else:
            session.close()
            # Handle the case where the user doesn't exist (e.g., raise an exception or return an error message)
            raise Exception("User not found")

    def delete_user(self, user: User) -> None:
        session = get_session()

        # Query the database to find the user by its ID
        user = session.query(self.model).filter_by(id=user.id, user_name=user.user_name).first()

        if user:
            # Delete the role
            session.delete(user)

            # Commit the deletion
            session.commit()
            session.close()
        else:
            session.close()
            # Handle the case
