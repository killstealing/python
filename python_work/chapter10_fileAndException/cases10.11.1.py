from pathlib import Path
import json

file1=Path('python/python_work/chapter10_fileAndException/like_number.txt')
content=file1.read_text()
number=json.loads(content)
print(f"I know your favorite number!It is {number}")