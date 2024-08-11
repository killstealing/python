values=[value**3 for value in range(1,11)]
for val in values:
    print(val)

print('The first three items in the list are:')
for val in values[:3]:
    print(val)

print('Three items from middle of the list are:')
for val in values[4:7]:
    print(val)

print('The last three items in the list are:')
for val in values[-3:]:
    print(val)