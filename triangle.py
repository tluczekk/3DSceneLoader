import numpy as np

class Vertex:
    def __init__(self, x, y, z, n):
        self.point = np.array([x, y, z])
        self.norm = n
    def get_coords(self):
        return np.array([self.point[0], self.point[1], self.point[2], 1])

class Triangle:
    def __init__(self, a, b, c):
        self.vertices = [a, b, c]

    def get_vertices(self):
        return np.array([self.vertices[0], self.vertices[1], self.vertices[2], 1])
    
    def get_vertexes(self):
        return self.vertices
    
    