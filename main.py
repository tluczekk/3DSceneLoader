from cone import Cone
from cuboid import Cuboid
from cylinder import Cylinder
from sphere import Sphere
from triangle import Vertex, Triangle
import json
import pygame
from pygame.locals import *
from sys import exit
import time
import numpy as np
from math import pi, sin, cos

# Setting up pygame
# https://pythonprogramming.net/pygame-python-3-part-1-intro/
width = 1200
height = 600
pygame.init()
pygame.display.set_caption('3D Scene loader - provide JSON to visualize')
display_game = pygame.display.set_mode((width, height))
CLOCK = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 36)
# display_game.fill((0,0,139))
# pygame.draw.line(display_game, pygame.color.THECOLORS['white'], (600,0), (600,600), 100)
# pygame.draw.line(display_game, pygame.color.THECOLORS['white'], (0,300), (1200,300), 100)
# pygame.draw.line(display_game, pygame.color.THECOLORS['white'], (0,0), (1200,600), 60)
# pygame.draw.line(display_game, pygame.color.THECOLORS['white'], (0,600), (1200,0), 60)
# pygame.draw.line(display_game, pygame.color.THECOLORS['red'], (600,0), (600,600), 60)
# pygame.draw.line(display_game, pygame.color.THECOLORS['red'], (0,300), (1200,300), 60)
# pygame.draw.line(display_game, pygame.color.THECOLORS['red'], (0,0), (1200,600), 26)
# pygame.draw.line(display_game, pygame.color.THECOLORS['red'], (0,600), (1200,0), 26)
CLOCK.tick(30)
pygame.display.flip()
time.sleep(5)

cones_arr = []
cyli_arr = []
cub_arr = []
sphere_arr = []

# parsing JSON file
with open('examp.json') as json_file:
    data = json.load(json_file)
    for f in data['figures']:
        if f['type'] == "cones":
            for cone in f['params']:
                temp_con = Cone(cone['x'], cone['y'], cone['z'], cone['radius'], cone['height'])
                cones_arr.append(temp_con) 
        elif f['type'] == "cylinders":
            for cylinder in f['params']:
                temp_cylin = Cylinder(cylinder['x'], cylinder['y'], cylinder['z'], \
                    cylinder['radius'], cylinder['height'])
                cyli_arr.append(temp_cylin)
        elif f['type'] == "cuboids":
            for cuboid in f['params']:
                temp_cuboid = Cuboid(cuboid['x'], cuboid['y'], cuboid['z'], cuboid['a'], cuboid['b'], cuboid['c'])
                cub_arr.append(temp_cuboid)
        elif f['type'] == "spheres":
            for sphere in f['params']:
                temp_sphere = Sphere(sphere['x'], sphere['y'], sphere['z'], sphere['radius'])
                sphere_arr.append(temp_sphere)

for con in cones_arr:
    print("cone: " + str(con.get_area()))
for cyl in cyli_arr:
    print("cylinder: " + str(cyl.get_area()))
for cub in cub_arr:
    print("cuboid: " + str(cub.get_area()))
    print(cub.get_triangles(cub.get_vertices()))
for sph in sphere_arr:
    print("sphere: " + str(sph.get_area()))

aspect = width / height
FOV = cos(pi/4) / sin (pi/4)

close = 0.1
far = 1000

M = np.array([
    [aspect*FOV, 0, 0, 0],
    [0, FOV, 0,0],
    [0,0,far/(far-close), 1],
    [0,0,(-far*close)/(far-close), 0]
])

f = 400
S = np.eye(4)
S[0,0] *= f
S[1,1] *= f

cubvert = []
cubtoshow = cub_arr[0]
conetoshow = cones_arr[0]
cylitoshow = cyli_arr[0]

# # cuboid
# for triangle in cubtoshow.get_triangles(cubtoshow.get_vertices()):
#     for v in triangle.get_vertices():
#         vertmult = np.array([v.point[0], v.point[1], v.point[2], 1])
#         cubvert.append(vertmult.dot(M))

# # cone
# for triangle in conetoshow.get_triangles(conetoshow.get_vertices()):
#     for v in triangle.get_vertices():
#         vertmult = np.array([v.point[0], v.point[1], v.point[2], 1])
#         cubvert.append(vertmult.dot(M))

# cylinder
for triangle in cylitoshow.get_triangles(cylitoshow.get_vertices()):
    for v in triangle.get_vertices():
        vertmult = np.array([v.point[0], v.point[1], v.point[2], 1])
        cubvert.append(vertmult.dot(M))

for i in range(len(cubvert)-2):
    pygame.draw.line(display_game, pygame.color.THECOLORS['white'], (cubvert[i][0] + width/2, cubvert[i][1] + height/2), (cubvert[i+1][0]+width/2, cubvert[i+1][1]+height/2), 1)
pygame.draw.line(display_game, pygame.color.THECOLORS['white'], (cubvert[len(cubvert)-1][0] + width/2, cubvert[len(cubvert)-1][1] + height/2), (cubvert[0][0]+width/2, cubvert[0][1]+height/2), 1)

pygame.display.flip()
time.sleep(15)

exit(0)