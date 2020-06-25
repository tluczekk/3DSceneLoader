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

        vert.append(Vertex(self.position[0]-(self.a/2),
                           self.position[1]+(self.b/2),
                           self.position[2]-(self.c/2),1))

        vert.append(Vertex(self.position[0]+(self.a/2),
                           self.position[1]-(self.b/2),
                           self.position[2]-(self.c/2),1))

        vert.append(Vertex(self.position[0]+(self.a/2),
                           self.position[1]+(self.b/2),
                           self.position[2]-(self.c/2),1))

        vert.append(Vertex(self.position[0]-(self.a/2),
                           self.position[1]-(self.b/2),
                           self.position[2]+(self.c/2),1))

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
        # front
        triangles.append(Triangle(vert[0], vert[1], vert[2]))
        triangles.append(Triangle(vert[1], vert[2], vert[3]))
        # top
        triangles.append(Triangle(vert[1], vert[3], vert[7]))
        triangles.append(Triangle(vert[1], vert[5], vert[7]))
        # back
        triangles.append(Triangle(vert[4], vert[5], vert[7]))
        triangles.append(Triangle(vert[4], vert[6], vert[7]))
        # bottom
        triangles.append(Triangle(vert[0], vert[2], vert[4]))
        triangles.append(Triangle(vert[2], vert[4], vert[6]))
        # left 
        triangles.append(Triangle(vert[0], vert[1], vert[4]))
        triangles.append(Triangle(vert[1], vert[4], vert[5]))
        # right
        triangles.append(Triangle(vert[2], vert[3], vert[7]))
        triangles.append(Triangle(vert[2], vert[6], vert[7]))

        return triangles