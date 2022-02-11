from models.user import User, Role


class UserController:
    current_user: int | None = None
    users: list[User] = [User(1, "Jamie", "MacLean", "01.01.2000", "jamie", "123456", Role.ADMIN)]

    def __init__(self):
        pass

    def create_user(self, firstname, lastname, date_of_birth, username, password):
        user_id_list = [user.user_id for user in self.users]
        user_id = max(user_id_list, default=0) + 1
        user = User(user_id=user_id, firstname=firstname, lastname=lastname, date_of_birth=date_of_birth, username=username,
                    password=password, role=Role.USER)
        self.users.append(user)

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user.user_id
                return True
        return False

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def change_attribute(self, attribute, value):
        user = self.find_user(self.current_user)
        if user is not None:
            user.change_attribute(attribute, value)
            return True
        else:
            return False

    def view_account(self):
        user = self.find_user(self.current_user)
        return user

    def logout(self):
        self.current_user = None