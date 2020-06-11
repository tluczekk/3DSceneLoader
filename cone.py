from math import pi, sqrt

class Cone:
    def __init__(self, r, h):
        self.radius = r
        self.height = h

    def get_area(self):
        return pi*self.radius*(self.radius + sqrt(self.height*self.height + self.radius*self.radius))
    
