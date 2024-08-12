sandwich_orders=['sandwich1','pastrami','sandwich2','pastrami','sandwich3','pastrami']
finished_sandwich=[]
pastrami='pastrami'
print(f'{pastrami} is out of stock')
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    if sandwich!=pastrami:
        finished_sandwich.append(sandwich)

print(f'sandwich_orders is {sandwich_orders}')
print(f'finished_sandwich is {finished_sandwich}')