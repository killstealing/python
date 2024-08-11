person={
    'Tom':1,
    'Jim':2,
    'Hellon':12,
    'Diana':13,
    'Celin':14
}
for name,age in person.items():
    print(f'{name}:{age}')

person['dasha']=20
person['ersha']=30
for name,age in person.items():
    print(f'{name}:{age}')