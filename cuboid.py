import numpy as np
from triangle import Vertex, Triangle

class Cuboid:
    def __init__(self, x, y, z, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.position = np.array([x,y,z])
    
    def get_area(self):
        return 2*(self.a*self.b + self.a*self.c + self.b*self.c)

    def get_vertices(self):
        vert = []
        vert.append(Vertex(self.position[0]-(self.a/2),
                           self.position[1]-(self.b/2),
                           self.position[2]-(self.c/2),1))
        vert.append(Vertex(self.position[0]+(self.a/2),
                           self.position[1]-(self.b/2),
                           self.position[2]-(self.c/2),1))
        vert.append(Vertex(self.position[0]-(self.a/2),
                           self.position[1]+(self.b/2),
                           self.position[2]-(self.c/2),1))
        vert.append(Vertex(self.position[0]-(self.a/2),
                           self.position[1]-(self.b/2),
                           self.position[2]+(self.c/2),1))
        vert.append(Vertex(self.position[0]+(self.a/2),
                           self.position[1]+(self.b/2),
                           self.position[2]-(self.c/2),1))
        vert.append(Vertex(self.position[0]-(self.a/2),
                           self.position[1]+(self.b/2),
                           self.position[2]+(self.c/2),1))
        vert.append(Vertex(self.position[0]+(self.a/2),
                           self.position[1]-(self.b/2),
                           self.position[2]+(self.c/2),1))
        vert.append(Vertex(self.position[0]+(self.a/2),
                           self.position[1]+(self.b/2),
                           self.position[2]+(self.c/2),1))
        return vert
    
    def get_triangles(self, vert):
        triangles = []
        for i in range(len(vert)-3):
            triangles.append(Triangle(vert[i], vert[i+1], vert[i+2]))
        triangles.append(Triangle(vert[len(vert)-2], vert[len(vert)-1], vert[0]))
        triangles.append(Triangle(vert[len(vert)-1], vert[0], vert[1]))
        return triangles