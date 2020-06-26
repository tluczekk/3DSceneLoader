from math import pi, sin, cos
import numpy as np
from triangle import Triangle, Vertex

class Sphere:
    def __init__(self, x, y, z, r):
        self.radius = r
        self.position = np.array([x, y, z])

    def get_area(self):
        return (4/3)*pi*self.radius*self.radius*self.radius

    def get_vertices(self):
        n = 10
        m = 10
        # south pole
        south_pole = np.array([self.position[0], self.position[1]+self.radius, self.position[2]])
        vert = []
        vert.append(Vertex(south_pole[0], south_pole[1], south_pole[2], 1))
        for i in range(n):
            for j in range(m):
                vert.append(Vertex(self.position[0]+self.radius*cos(2*pi/m*(j-1))*sin(pi/(n+1)*i), \
                                   self.position[1]+self.radius*cos(pi/(n+1)*i), \
                                   self.position[2]+self.radius*sin(2*pi/m*(j-1))*sin(pi/(n+1)*i),1))
        # north pole
        vert.append(Vertex(self.position[0], self.position[1]-self.radius, self.position[2], 1))
        
        return vert

    def get_triangles(self, vert):
        triangles = []
        m = 10
        n = 10
        for i in range(m-1):
            triangles.append(Triangle(vert[0], vert[i+1], vert[i+2]))
            triangles.append(Triangle(vert[m*n+1], vert[(n-1)*m+i+1], vert[(n-1)*m+i+2]))
        triangles.append(Triangle(vert[0], vert[1], vert[m]))
        triangles.append(Triangle(vert[m*n+1], vert[m*n], vert[(n-1)*m+1]))
        
        for i in range(n-1):
            for j in range(m):
                if j+1 == m:
                    triangles.append(Triangle(vert[(i+1)*m], vert[i*m+1], vert[(i+1)*m+1]))
                else:
                    triangles.append(Triangle(vert[i*m+j+1], vert[i*m+j+2], vert[(i+1)*m+j+2]))

        for i in range(n-1):
            for j in range(m):
                if j+1 == m:
                    triangles.append(Triangle(vert[(i+1)*m], vert[(i+1)*m+1], vert[(i+2)*m]))
                else:
                    triangles.append(Triangle(vert[i*m+j+1], vert[(i+1)*m+j+2], vert[(i+1)*m+j+1]))
        
        return triangles
