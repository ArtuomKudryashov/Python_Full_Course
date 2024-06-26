class Image:
    def __init__(self, resolution, title, extension):
        self.resolution= resolution
        self.title = title
        self.extension =extension


    def resize(self, new_resolution):
        self.resolution = new_resolution

    def new_extension(self, new_ext):
        self.extension =new_ext

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"{self.title}.{self.extension}"




first_img =Image('1920x1080',"My dog", 'jpg')
print(first_img.resolution)
print(first_img.title)
print(first_img.extension)
print(first_img.__dict__)
change_res=first_img.resize("4040x2160")
print(first_img.resolution)
print(first_img.__dict__)
first_img.new_extension("bmp")
print((first_img.__dict__))


print(first_img)
print(repr(first_img))


