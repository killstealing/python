class User:
    def __init__(self,first_name,last_name,age,location):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.location=location
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} {self.age} {self.location}")
    def greet_user(self):
        print(f'How are you? {self.last_name}')

user1=User('wang','dasha',20,'dalian')
user1.describe_user()
user1.greet_user()
user2=User('Zhang','Isaac',45,'shanghai')
user2.describe_user()
user2.greet_user()
user3=User('Lin','lechao',35,'beijing')
user3.describe_user()
user3.greet_user()