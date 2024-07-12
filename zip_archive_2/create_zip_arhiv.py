from zipfile import ZipFile
from pathlib import Path

# Path('my-files').mkdir()
# print(Path.cwd())

# cwd = Path('D:/').joinpath("Python").joinpath('Python-Bogdan').joinpath('zip_archive_2').joinpath("Create Artuom23")
# print(cwd.mkdir())
#
# with open("my-files/first.txt","w") as  my_file:
#     my_file.write("This is first file")
# #
# with open("my-files/second.txt", 'w')as my_file:
#     my_file.write("This is second file")
#
# Path('my-files2').mkdir()
# with open("my-files2/first.txt","w") as  my_file2:
#     my_file2.write("This is first file")
#
# with open("my-files2/second.txt", 'w')as my_file2:
#     my_file2.write("This is second file")

with open('Create Artuom23/first.txt','w') as file_ca:
    file_ca.write("This is first file")

with open('Create Artuom23/second.py','w') as file_ca:
    file_ca.write("#This is second file")


