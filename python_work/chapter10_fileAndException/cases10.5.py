from pathlib import Path

file1=Path('python/python_work/chapter10_fileAndException/guests.txt')
active=True
name=""
while active:
    print('if you want to exit, please enter q\n')
    current_name=input('please input your name:')
    if current_name=='q':
        active=False
    else:
        name+=current_name+'\n'
file1.write_text(name)

