from math import pi, sin, cos
import numpy as np
from triangle import Triangle, Vertex

class Cylinder:
    def __init__(self, x, y, z, r, h,d):
        self.radius = r
        self.height = h
        self.position = np.array([x, y, z])
        self.density = d

    def get_area(self):
        return 2*pi*self.radius*(self.radius + self.height)

    def get_vertices(self):
        self.bottom_center = np.array([self.position[0], self.position[1]+self.height/2, self.position[2]])
        vert = []
        # bottom center
        vert.append(Vertex(self.bottom_center[0], self.bottom_center[1], self.bottom_center[2],1))
        d = self.density
        # bottom fill using trigonometric parametrisation of the circle
        for i in range(d):
            vert.append(Vertex(self.radius * cos(2*pi*i/d) + self.bottom_center[0], self.bottom_center[1], \
                self.radius * sin(2 * pi * i / d) + self.bottom_center[2],1))
        # top center
        self.top_center = np.array([self.position[0], self.position[1]-self.height/2, self.position[2]])
        vert.append(Vertex(self.position[0], self.position[1]-self.height/2, self.position[2],1))
        # top fill using the same method as above
        for i in range(d):
            vert.append(Vertex(self.radius*cos(2*pi*i/d) + self.top_center[0], self.top_center[1], \
                self.radius * sin(2*pi*i/d) + self.top_center[2], 1))
        return vert

    def get_triangles(self, vert):
        # bottom triangles
        d = self.density
        triangles = []
        # bottom arc 1-x, top arc 1+d+1 - 1 + 2d
        # bottom triangles 
        for i in range(d-2):
            triangles.append(Triangle(vert[0], vert[i+1], vert[i+2]))
        triangles.append(Triangle(vert[0], vert[d], vert[1])) # we can safely assume vert[1] exists
        
        # top triangles
        for i in range(d - 2):
            triangles.append(Triangle(vert[d+1], vert[i+d+2], vert[i+d+3]))
        triangles.append(Triangle(vert[d+1], vert[2*d + 1], vert[d+2]))

        # side triangles
        for i in range(d-1):
            triangles.append(Triangle(vert[i+1], vert[i+2], vert[i+d+2]))
            triangles.append(Triangle(vert[i+2], vert[i+d+2], vert[i+d+3]))
        triangles.append(Triangle(vert[d], vert[1], vert[2*d + 1]))
        triangles.append(Triangle(vert[1], vert[2*d+1], vert[d+2]))

        return triangles
