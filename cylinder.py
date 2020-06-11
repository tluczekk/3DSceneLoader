from math import pi

class Cylinder:
    def __init__(self, r, h):
        self.radius = r
        self.height = h

    def get_area(self):
        return 2*pi*self.radius*(self.radius + self.height)