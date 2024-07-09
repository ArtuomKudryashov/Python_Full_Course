from pathlib import Path
my_file = Path('second.txt')
test_new_file = open(my_file,'w')
test_new_file.close()
if my_file.exists():
    my_file.unlink()
    print("File is deleted")
else:
    print('File was deleted')
