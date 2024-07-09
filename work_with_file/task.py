import os
from pathlib import Path

files_dir_path = Path('files3')
files_dir_path.mkdir(exist_ok=True)

first_file = Path(files_dir_path / 'first.txt')
second_file = Path(files_dir_path / 'second.txt')
third_file = Path(files_dir_path / 'third.txt')

with open(first_file, 'w') as f:
    # with open(files_dir_path/'first.txt','w') as f:
    f.write('First raw\n')
    f.write('Second raw\n')
    f.write('Third raw\n')

with open(second_file, 'w') as f2:
    f2.write('  Fourth raw\n')
    f2.write(' Fifth raw\n')
    f2.write('Sixth raw')

with open(files_dir_path / 'third.txt', 'w') as f3:
    lines = ["First line in the third file",
             "Second line in the third file",
             "last line in the second file"
             ]
    for line in lines:
        f3.write(line + '\n')

with open(files_dir_path / 'first.txt') as f:
    print(f.read())

with open(files_dir_path / 'second.txt') as f2:
    for line in f2.readlines():
        print(line.strip())

with open(second_file) as f2a:
    while True:
        line = f2a.readline()
        if not line:
            break
        print(line.strip())

print("<<<<<<Delete files and folder>>>>>>")
# os.chdir('files2')
print(Path.cwd())

files_dir_path2 = Path.cwd()
print(f"Working in directory: {files_dir_path2}")
print(f"Working in directory: {Path.cwd()}")

first_file2 = Path(files_dir_path2 / 'first.txt')
second_file2 = Path(files_dir_path2 / 'second.txt')
third_file2 = Path(files_dir_path2 / 'third.txt')
print('<<<<<<<<<<<<<Transfer to current folder>>>>>>>>>>>>>>>>')

if first_file2.exists() and second_file2.exists() and third_file2.exists():
    third_file2.unlink()
    first_file2.unlink()
    second_file2.unlink()

    print("first_files2 and second_files2 are deleted")
else:
    print("The files were deleted")
# os.chdir('..')

# files_dir_path2.rmdir()

files_dir_path1 = Path('files')

# Пытаемся удалить директорию files
try:
    files_dir_path1.rmdir()
    print("Directory 'files' is deleted")
except OSError as e:
    print(f"Error: {e}")

