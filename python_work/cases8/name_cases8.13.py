def build_profile(first,last,**user_info):
    user_info['fisrt_name']=first
    user_info['last_name']=last
    return user_info

user_profile=build_profile('albert','einstein',location='princeton',field='physics',age=35,country='China')
print(user_profile)