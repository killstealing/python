from pathlib import Path

file1=Path('python/python_work/chapter10_fileAndException/learning_python.txt')
content=file1.read_text()
for line in content.splitlines():
    print(line.replace('Python','C 语言'))