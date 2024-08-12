age=''
while age!='quit':
    age=input('Please input Pizza toppings:')
    if age=='quit':
        break
    if int(age)<3:
        print('you can have free vote')
    elif int(age)>=3 and int(age)<12:
        print('the price of vote is $10')
    else:
        print('the price of vote is 15')