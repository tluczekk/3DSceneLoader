from math import pi, sqrt
import numpy as np

class Cone:
    def __init__(self, x, y, z, r, h):
        self.radius = r
        self.height = h
        self.position = np.array([x,y,z])

    def get_area(self):
        return pi*self.radius*(self.radius + sqrt(self.height*self.height + self.radius*self.radius))
    
