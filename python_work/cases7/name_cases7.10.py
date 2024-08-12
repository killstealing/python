holiday_resort={}
active=True
while active==True:
    name=input('what is your name?')
    resort=input('If you could visit one place in the world, where would you go?')
    holiday_resort[name]=resort
    another_people=input('would you like another people to do the survey?')
    if another_people!='y':
        active=False

print(holiday_resort)