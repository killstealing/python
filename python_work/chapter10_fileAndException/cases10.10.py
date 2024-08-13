from pathlib import Path

file1=Path('python/python_work/chapter10_fileAndException/gudengbao.txt')
content=file1.read_text()
print(content.lower().count('row'))