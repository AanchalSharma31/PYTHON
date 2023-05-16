class Rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return area

class Cube(Rect):
    def __init__(self,length, width, height):
        super().__init__(length, width)
        self.height = height

    def vol(self):
        volume = self.height * super().area()
        return volume  



re = Rect(2,7)
cu = Cube(2,4,5)
print(cu.vol())