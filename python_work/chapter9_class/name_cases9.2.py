class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print('The restaurant is currently open for business')

restaurant1=Restaurant('Wei duo li ya','jiudian')
restaurant2=Restaurant('Wan hao','jiudian')
restaurant3=Restaurant('Tian Fu lai','jiulou')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()