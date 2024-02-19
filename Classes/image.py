class Image:
    def __init__(self, resolution, title, extension):
        self.resolution= resolution
        self.title = title
        self.extension =extension


    def resize(self, new_resolution):
        self.resolution = new_resolution


first_img =Image('1920x1080',"My dog", 'jpg')
print(first_img.resolution)
print(first_img.title)
print(first_img.extension)