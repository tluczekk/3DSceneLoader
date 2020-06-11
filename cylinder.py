from math import pi
import numpy as np

class Cylinder:
    def __init__(self, x, y, z, r, h):
        self.radius = r
        self.height = h
        self.position = np.array([x, y, z])

    def get_area(self):
        return 2*pi*self.radius*(self.radius + self.height)