from math import pi

class Sphere:
    def __init__(self, r):
        self.radius = r

    def get_area(self):
        return (4/3)*pi*self.radius*self.radius*self.radius