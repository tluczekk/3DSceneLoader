import numpy as np

class Vertex:
    def __init__(self, x, y, z, n):
        self.point = np.array([x, y, z])
        self.norm = n

class Triangle:
    def __init__(self, a, b, c):
        self.vertices = [a, b, c]
    