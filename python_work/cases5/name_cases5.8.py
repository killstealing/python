users=['Jim','Tom','Hello','Jack','admin']
for user in users:
    if user=='admin':
        print(f'Hello {user}, would you like to see a status report?')
    else:
        print(f'hello, {user}, thank you for logging in again.')
