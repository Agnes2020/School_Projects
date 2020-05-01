# this class contains all functions to be passed by the admin user class.
class MainUser:
    def __init__(self, password, username):
        self.password = password
        self.username = username

    def set_user_name_and_password(self):
        self.username = input("Please enter your username: ")
        self.password = input("Please enter your password")

    def info(self):
        return self.username

    def login(self, input_user, input_password):
        if self.username == input_user and self.password == input_password:
            return True
        else:
            return False

    def logout(self):
        self.password = ""
        self.username = ""
        return "Logged Out"
