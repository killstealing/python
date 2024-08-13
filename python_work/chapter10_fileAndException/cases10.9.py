from pathlib import Path

dogs_file=Path('python/python_work/chapter10_fileAndException/dogs.txt')
try:
    print(dogs_file.read_text())
except FileNotFoundError:
    pass

cats_file=Path('python/python_work/chapter10_fileAndException/cats.txt')
try:
    print(cats_file.read_text())
except FileNotFoundError:
    pass
