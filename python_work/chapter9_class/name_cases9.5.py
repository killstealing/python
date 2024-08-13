class User:
    def __init__(self,first_name,last_name,age,location,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.location=location
        self.login_attempts=login_attempts
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} {self.age} {self.location}")
    def greet_user(self):
        print(f'How are you? {self.last_name}')
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0

user1=User('wang','dasha',20,'dalian',20)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
