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