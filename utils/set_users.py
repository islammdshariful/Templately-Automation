
class User:
    def __init__(self, config, email="", password=""):
        self.config = config
        self.email = email
        self.password = password

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def set_email(self, usr):
        if usr.__eq__("user_1"):
            self.email = self.config["user_1"]["email"]
        elif usr.__eq__("user_2"):
            self.email = self.config["user_2"]["email"]
        else:
            pass

    def set_password(self, usr):
        if str(usr).__eq__("user_1"):
            self.password = self.config["user_1"]["password"]
        elif str(usr).__eq__("user_2"):
            self.password = self.config["user_2"]["password"]
        else:
            pass

    def set_usr(self, usr):
        self.set_email(usr)
        self.set_password(usr)
