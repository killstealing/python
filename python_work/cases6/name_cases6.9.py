favorite_places={
    'jen':['dalian','shandong'],
    'sarah':['beijing','hefei'],
    'edward':['xian','chengdu','xiweiyi'],
    'phil':['xinjiang','xizang','sichuan']
}
for name,values in favorite_places.items():
    like_places=''
    for place in values:
        like_places+=place+" "
    print(f'{name} likes {like_places}')