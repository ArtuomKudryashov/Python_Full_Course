
class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def weight(self,width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def area_info(self):
        area = self.width*self.height
        print(f"Area of the Rectangle  = {area}")

    def perimetr_info(self):
        perimetr = (self.width + self.height)*2
        print(f"Area of the Rectangle  = {perimetr}")