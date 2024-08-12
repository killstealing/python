def make_car(producer,model,**accessory):
    accessory['producer']=producer
    accessory['model']=model
    return accessory

car=make_car('subaru','outback',color='red',tow_package=True,country='China')
print(car)