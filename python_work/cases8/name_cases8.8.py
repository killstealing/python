def make_album(singer,album):
    return {'singer':singer,'album':album}

while True:
    print('enter "q" at any time to quit:')
    singer=input('Please enter singer name:')
    if singer=='q':
        break
    album=input('Please enter album:')
    if album=='q':
        break
    print(make_album(singer,album))