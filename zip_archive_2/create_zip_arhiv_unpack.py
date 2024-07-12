from zipfile import ZipFile
from pathlib import Path

with ZipFile('my-files.zip') as my_zip_file:
    # my_zip_file.extractall('my-files-unzipped')
    print( my_zip_file.infolist())
    for info in my_zip_file.infolist():

        print('<<<<<<>>>>>>>')
        print(f"Filename: {info.filename}")
        print(f"Compressed size: {info.compress_size} bytes")
        print(f"Uncompressed size: {info.file_size} bytes")
        # Extract file permissions
        filemode = info.external_attr >> 16
        print(f"File mode: {oct(filemode)}")
        print()

with ZipFile('Create Artuom23.zip') as my_zip_file_art:
    my_zip_file_art.extractall('Create Artuom23-unzipped')