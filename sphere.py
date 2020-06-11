from math import pi
import numpy as np

class Sphere:
    def __init__(self, x, y, z, r):
        self.radius = r
        self.position = np.array([x, y, z])

    def get_area(self):
        return (4/3)*pi*self.radius*self.radius*self.radius