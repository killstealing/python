from pathlib import Path
import json

file1=Path('python/python_work/chapter10_fileAndException/like_number.txt')
number=input('pleaes enter your favorite number: ')
content=json.dumps(number)
file1.write_text(content)