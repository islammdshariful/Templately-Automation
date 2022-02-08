
class User:
    def __init__(self, read_credentials, email="", password=""):
        self.cred = read_credentials
        self.email = email
        self.password = password

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def set_email(self, usr):
        if usr.__eq__("user_1"):
            self.email = self.cred["user_1"]["email"]
        elif usr.__eq__("user_2"):
            self.email = self.cred["user_2"]["email"]
        else:
            pass

    def set_password(self, usr):
        if str(usr).__eq__("user_1"):
            self.password = self.cred["user_1"]["password"]
        elif str(usr).__eq__("user_2"):
            self.password = self.cred["user_2"]["password"]
        else:
            pass

    def set_usr(self, usr):
        self.set_email(usr)
        self.set_password(usr)
