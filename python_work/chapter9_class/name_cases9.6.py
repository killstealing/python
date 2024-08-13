class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print('The restaurant is currently open for business')
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=flavors
    def describe_flavors(self):
        print(self.flavors)

ice=IceCreamStand('Mi xue bing cheng','Nai cha',['chocolate','vanilla','cream'])
ice.describe_flavors()