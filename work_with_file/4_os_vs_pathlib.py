import os
from os import path
from pathlib import Path

print(path.curdir)
print((os.getcwd()))
print(path.abspath('.'))

print("<<<<<<<<<<<Pathlib>>>>>>>>>>>>>>>")
print(type(Path))

cwd=Path('.')
print(cwd)
print(cwd.__str__())
print(isinstance(cwd,Path))
print(type(cwd))
print(Path.__subclasses__())

print("<<<<<<<<<<<Attributes>>>>>>>>>>>>>>>")
print(dir(cwd))
print(cwd.absolute())

cwd = Path('D:/').joinpath("Python").joinpath('Python_Bogdan').joinpath('work_with_file')
print(1)
print(cwd)
print(2)
print(Path.cwd())
print(3)
print(Path.cwd().exists())
print(4)
print(Path.cwd().is_file())
print(5)
print(Path.cwd().is_dir())
print(6)
print(Path('../work_with_file').exists())

print("<<<<<<<Create new folder")
cwd = Path('D:/').joinpath("Python").joinpath('Python-Bogdan').joinpath('work_with_file').joinpath("Create Artuom23")

print(cwd.mkdir(parents=True, exist_ok=True))


if cwd.exists() and cwd.is_dir():
    print(f"Directory '{cwd}' created successfully.")
else:
    print(f"Failed to create directory '{cwd}'.")
print(cwd.is_dir())
print(cwd.is_file())

# if not cwd.exists():
#     cwd.mkdir()

# if cwd.exists():
#     cwd.rmdir()
print("Absolute path to a folder on Windows")
print(Path('.'))
print(Path.cwd())
print(Path('.').cwd())
print(type(Path('.')))