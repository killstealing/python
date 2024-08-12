sandwich_orders=['sandwich1','sandwich2','sandwich3']
finished_sandwich=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print(f'I made your {sandwich}')
    finished_sandwich.append(sandwich)
print(f'sandwich_orders is {sandwich_orders}')
print(f'finished_sandwich is {finished_sandwich}')