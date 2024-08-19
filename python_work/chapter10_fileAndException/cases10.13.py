from pathlib import Path
import json

def store_number():
    file1=Path('python/python_work/chapter10_fileAndException/like_number1.txt')
    number=input('pleaes enter your favorite number: ')
    content=json.dumps(number)
    file1.write_text(content)

def get_number():
    file1=Path('python/python_work/chapter10_fileAndException/like_number1.txt')
    content=file1.read_text()
    number=json.loads(content)
    return number
def greet_user():
    file1=Path('python/python_work/chapter10_fileAndException/like_number1.txt')
    if file1.exists():
        number=get_number()
        message=f'if this number {number} is correct?'
        reply=input(message)
        if reply=='Y':
            print(f"I know your favorite number!It is {number}")
        else:
            store_number()
            number=get_number()
            print(f"I know your favorite number!It is {number}")
    else:
        store_number()
        number=get_number()
        print(f"I know your favorite number!It is {number}")

greet_user()
        
        

