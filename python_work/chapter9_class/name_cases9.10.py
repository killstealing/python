from restaurant import Restaurant
        
restaurant=Restaurant('Wei duo li ya','jiudian')
print(restaurant.number_served)
restaurant.set_number_served(20)
print(restaurant.number_served)
restaurant.increment_number_served(30)
print(restaurant.number_served)