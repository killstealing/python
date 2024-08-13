class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print('The restaurant is currently open for business')
    def set_number_served(self,number_served):
        self.number_served=number_served
    def increment_number_served(self,num):
        self.number_served+=num