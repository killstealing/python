favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

need_to_check_list=['jen','sarah','Tim','Isaac']
for name in need_to_check_list:
    if name in favorite_languages:
        print('thanks for joinning the check')
    else:
        print('please join to do the check')