import os
import time
from os import  path
from pathlib import  Path
print(path.curdir)
print(path.abspath('.'))

print()
print(type(Path))
cwd = Path('.')
print(cwd)
print(cwd.__str__())
print((isinstance(cwd,Path)))
print(type(cwd))
print(Path.__subclasses__())
print(cwd.absolute())
print()

cwd = Path('D:/').joinpath("Python").joinpath('Python_Bogdan').joinpath('work_with_file')
print(cwd)
print(Path.cwd())
print(Path.cwd().exists())
print(Path.cwd().is_file())
print(Path.cwd().is_dir())
print(Path('work_with_file').exists())

print("<<<<<<<Create new folder")
cwd = Path('D:/').joinpath("Python").joinpath('Python-Bogdan').joinpath('work_with_file').joinpath("Create Artuom")

print(cwd.mkdir(parents=True, exist_ok=True))
if cwd.exists() and cwd.is_dir():
    print(f"Directory '{cwd}' created successfully.")
else:
    print(f"Failed to create directory '{cwd}'.")
#
# if not cwd.exists():
#     cwd.mkdir()

# if cwd.exists():
#     cwd.rmdir()

print("Absolute path to a folder on Windows")
print(Path('.'))
print(Path.cwd())
print(Path('.').cwd())
print(type(Path('.')))