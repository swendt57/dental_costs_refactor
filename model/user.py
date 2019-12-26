from flask_login import UserMixin


class User(UserMixin):

    first_name = ''
    last_name = ''
    username = ''
    role = ''

    @staticmethod
    def test():
        return "working!"

    # @staticmethod
    # def is_authenticated(self):
    #     return True
    #
    # @staticmethod
    # def is_active():
    #     return True
    #
    # @staticmethod
    # def is_anonymous():
    #     return True
    #
    # @staticmethod
    # def get_id():
    #     return "something"
