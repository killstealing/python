guestArray=['Jim','Rick','Anthony']
print('Hello,'+guestArray[0]+', would you like to have dinner with me?')
print('Hello,'+guestArray[1]+', would you like to have dinner with me?')
print('Hello,'+guestArray[2]+', would you like to have dinner with me?')
print(f'I have invited {len(guestArray)} guests')

guestArray.remove('Jim')
print('remove:')
print(guestArray)

del guestArray[0]
print('del:')
print(guestArray)

popGuest=guestArray.pop()
print('popGuest:'+popGuest)
print(guestArray)

guestArray.append('dasha')
print('append:')
print(guestArray)

guestArray.insert(0,'dagen')
print('insert:')
print(guestArray)


