guestArray=['Jim','Rick','Anthony']
print('Hello,'+guestArray[0]+', would you like to have dinner with me?')
print('Hello,'+guestArray[1]+', would you like to have dinner with me?')
print('Hello,'+guestArray[2]+', would you like to have dinner with me?')

name='Jim'
print(name+" can't have dinner with me")
guestArray.remove(name)
guestArray.append('Karthik')
print('Hello,'+guestArray[0]+', would you like to have dinner with me?')
print('Hello,'+guestArray[1]+', would you like to have dinner with me?')
print('Hello,'+guestArray[2]+', would you like to have dinner with me?')

print('I find a bigger desk , which can accommodate more people')

guestArray.insert(0,'Mohan')
guestArray.insert(2,'Sakthi')
guestArray.append('Adam')

print('Hello,'+guestArray[0]+', would you like to have dinner with me?')
print('Hello,'+guestArray[1]+', would you like to have dinner with me?')
print('Hello,'+guestArray[2]+', would you like to have dinner with me?')
print('Hello,'+guestArray[3]+', would you like to have dinner with me?')
print('Hello,'+guestArray[4]+', would you like to have dinner with me?')
print('Hello,'+guestArray[5]+', would you like to have dinner with me?')

print('\n hello all, I can only invite two people to have dinner with me')
delGuest=guestArray.pop()
print('Sorry, '+delGuest+" I can't have dinner with you")
delGuest=guestArray.pop()
print('Sorry, '+delGuest+" I can't have dinner with you")
delGuest=guestArray.pop()
print('Sorry, '+delGuest+" I can't have dinner with you")
delGuest=guestArray.pop()
print('Sorry, '+delGuest+" I can't have dinner with you")

print('\n Hello, '+guestArray[0]+' , you are still in the queue')
print('\n Hello, '+guestArray[1]+' , you are still in the queue')

del guestArray[0]
del guestArray[0]
print(guestArray)

