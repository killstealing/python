from user9_12_1 import User
class Privileges:
    def __init__(self,privileges):
        self.privileges=privileges
    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self,first_name,last_name,age,location,privileges):
        super().__init__(first_name,last_name,age,location)
        self.privileges=Privileges(privileges)