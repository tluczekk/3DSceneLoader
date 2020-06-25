from math import pi, sin, cos
import numpy as np
from triangle import Triangle, Vertex

class Cylinder:
    def __init__(self, x, y, z, r, h):
        self.radius = r
        self.height = h
        self.position = np.array([x, y, z])

    def get_area(self):
        return 2*pi*self.radius*(self.radius + self.height)

    def get_vertices(self):
        self.bottom_center = np.array([self.position[0], self.position[1]+self.height/2, self.position[2]])
        vert = []
        # bottom center
        vert.append(Vertex(self.bottom_center[0], self.bottom_center[1], self.bottom_center[2],1))
        x = 20
        # bottom fill using trigonometric parametrisation of the circle
        for i in range(x):
            vert.append(Vertex(self.radius * cos(2*pi*i/x) + self.bottom_center[0], self.bottom_center[1], \
                self.radius * sin(2 * pi * i / x) + self.bottom_center[2],1))
        # top center
        self.top_center = np.array([self.position[0], self.position[1]-self.height/2, self.position[2]])
        vert.append(Vertex(self.position[0], self.position[1]-self.height/2, self.position[2],1))
        # top fill using the same method as above
        for i in range(x):
            vert.append(Vertex(self.radius*cos(2*pi*i/x) + self.top_center[0], self.top_center[1], \
                self.radius * sin(2*pi*i/x) + self.top_center[2], 1))
        return vert

    def get_triangles(self, vert):
        # bottom triangles
        x = 20
        triangles = []
        # bottom arc 1-x, top arc 1+x+1 - 1 + 2x
        # bottom triangles 
        for i in range(x-2):
            triangles.append(Triangle(vert[0], vert[i+1], vert[i+2]))
        triangles.append(Triangle(vert[0], vert[x], vert[1])) # we can safely assume vert[1] exists
        
        # top triangles
        for i in range(x - 2):
            triangles.append(Triangle(vert[x+1], vert[i+x+2], vert[i+x+3]))
        triangles.append(Triangle(vert[x+1], vert[2*x + 1], vert[x+2]))

        # side triangles
        for i in range(x-1):
            triangles.append(Triangle(vert[i+1], vert[i+2], vert[i+x+2]))
            triangles.append(Triangle(vert[i+2], vert[i+x+2], vert[i+x+3]))
        triangles.append(Triangle(vert[x], vert[1], vert[2*x + 1]))
        triangles.append(Triangle(vert[1], vert[2*x+1], vert[x+2]))

        return triangles
