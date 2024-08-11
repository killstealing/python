current_users=['Jim','Tom','Hello','Jack','admin']
current_users1=[value.lower() for value in current_users[:]]

new_users=['JIM','TOM','Isaac','Diana','Celin']
for new_user in new_users:
    if new_user.lower() in current_users1:
        print(f'user name {new_user} is already existed, please enter a new name')
    else:
        print(f'this user name {new_user} is not used in the system')


