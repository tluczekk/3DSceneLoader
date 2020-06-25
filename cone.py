from math import pi, sqrt, sin, cos
import numpy as np
from triangle import Triangle, Vertex

class Cone:
    def __init__(self, x, y, z, r, h):
        self.radius = r
        self.height = h
        self.position = np.array([x,y,z])

    def get_area(self):
        return pi*self.radius*(self.radius + sqrt(self.height*self.height + self.radius*self.radius))

    def get_vertices(self):
        self.bottom_center = np.array([self.position[0], self.position[1]+self.height/2, self.position[2]])
        vert = []
        vert.append(Vertex(self.bottom_center[0], self.bottom_center[1], self.bottom_center[2],1))
        x = 20
        # using trigonometric parametrisation of the circle
        for i in range(x):
            vert.append(Vertex(self.radius * cos(2*pi*i/x) + self.bottom_center[0], self.bottom_center[1], \
                self.radius * sin(2 * pi * i / x) + self.bottom_center[2],1))
        # top
        vert.append(Vertex(self.position[0], self.position[1]-self.height/2, self.position[2],1))
        return vert
    
    def get_triangles(self, vert):
        # bottom triangles
        # first vertex in vert is the center of base, last being the top of the cone
        triangles = []
        for i in range(len(vert)-4):
            triangles.append(Triangle(vert[0], vert[i+1], vert[i+2]))
        triangles.append(Triangle(vert[0], vert[len(vert)-2], vert[1])) # we can safely assume vert[1] exists
        
        # side triangles
        for i in range(len(vert) - 4):
            triangles.append(Triangle(vert[i+1], vert[i+2], vert[len(vert)-1]))
        triangles.append(Triangle(vert[len(vert)-2], vert[1], vert[len(vert)-1]))

        return triangles