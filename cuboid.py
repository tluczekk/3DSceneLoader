import numpy as np

class Cuboid:
    def __init__(self, x, y, z, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.position = np.array([x,y,z])
    
    def get_area(self):
        return 2*(self.a*self.b + self.a*self.c + self.b*self.c)