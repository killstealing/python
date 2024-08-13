from pathlib import Path

file1=Path('python/python_work/chapter10_fileAndException/learning_python.txt')
content=file1.read_text()
print(content)

file_content_array=content.splitlines()
for line in file_content_array:
    print(line)