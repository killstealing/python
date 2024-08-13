from pathlib import Path

file1=Path('python/python_work/chapter10_fileAndException/guest.txt')
name=input('please input your name:')
content=file1.write_text(name)