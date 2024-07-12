from zipfile import ZipFile
from pathlib import Path


#
# with ZipFile ('my-files.zip', mode ='w') as my_zip_file:
#     print(my_zip_file)
#     for file in Path('my-files').iterdir():
#         print(file)
#         my_zip_file.write(file, arcname= file.name)



with ZipFile ('Create Artuom23.zip', mode ='w') as my_zip_file_art:
    print(my_zip_file_art)
    for file in Path('Create Artuom23').iterdir():
        print(file)
        my_zip_file_art.write(file, arcname= file.name)
