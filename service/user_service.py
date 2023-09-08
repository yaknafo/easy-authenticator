from dal.user_dal import UserDal


class UserService(object):

    def __init__(self):
        self.dal = UserDal()

    def get_all_users(self):
        return self.dal.get_all_users()
