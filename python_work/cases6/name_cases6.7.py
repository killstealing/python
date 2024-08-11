person={
    'first_name':'First name',
    'last_name':'Last name',
    'age':12,
    'city':'dalian'
}
person1={
    'first_name':'First name1',
    'last_name':'Last name1',
    'age':13,
    'city':'dalian1'
}
person2={
    'first_name':'First name2',
    'last_name':'Last name2',
    'age':14,
    'city':'dalian2'
}
people=[person,person1,person2]
for value in people:
    print('\n')
    for item,val in value.items():
        print(f'{item} is {val}')