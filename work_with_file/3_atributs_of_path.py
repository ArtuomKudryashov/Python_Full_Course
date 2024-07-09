from pathlib import Path
import os

file_path = Path('test.txt')
print([m for m in dir(file_path) if not m.startswith('_')])

print("path  to current derectory")

print(Path.cwd())

#way Mac and Unix
print(Path('usr').joinpath('local').joinpath('bin'))
print(Path('usr') / 'local' / 'bin')

#windows
print(Path('C:/').joinpath('Users').joinpath('Artuom'))
print(Path('C:/') / 'Users' / 'Artuom')

print("<<<Check  the directory or file exists>>>")
print(Path('main.py').exists())
print(Path('/Users/bogdan/Desktop').exists())
print(Path('other.py').exists())
print(Path.cwd())
print(Path(r'D:\Python\Python-Bogdan\work_with_file').exists())
print(Path('D:\\Python\\Python-Bogdan\\work_with_file').exists())
print(Path('D:/Python/Python-Bogdan/work_with_file').exists())
print(Path.cwd())
print(Path('1_my_os.py').exists())
print(Path('work_with_file').exists())

print("Verification/check can only be done from the parent directory")
os.chdir('D:/Python/Python-Bogdan')
print(Path('work_with_file').exists())
print(Path('1_my_os.py').exists())
os.chdir('D:/Python/Python-Bogdan/work_with_file')
print(Path('1_my_os.py').exists())
print(Path('../work_with_file').exists())
print(Path('1_my_os.py').exists())
print(Path('work_with_file').exists())
print(Path('../work_with_file').exists())

print("<<<Check  is this  directory or file>>>")
print(Path("1_my_os.py").is_file())
print(Path("1_my_os.py").is_dir())
print(Path('D:/Python/Python-Bogdan/work_with_file').is_dir())
print(Path('D:/Python/Python-Bogdan/work_with_file').is_file())

print()
print("<<<<<<List of files in the directory>>>>>>")
for f in Path('.').iterdir():
    print(f)


