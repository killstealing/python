rivers={
    'nile':'egypt',
    'nile2':'egypt2',
    'nile3':'egypt3',
    'nile4':'egypt4',
    'nile5':'egypt5'
}
for name,city in rivers.items():
    print(f'The {name.title()} runs through {city.title()}')

for name in rivers.keys():
    print(name)

for city in rivers.values():
    print(city)