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
                temp_con = Cone(cone['x'], cone['y'], cone['z'], cone['radius'], cone['height'], cone['density'])
                cones_arr.append(temp_con) 
        elif f['type'] == "cylinders":
            for cylinder in f['params']:
                temp_cylin = Cylinder(cylinder['x'], cylinder['y'], cylinder['z'], \
                    cylinder['radius'], cylinder['height'], cylinder['density'])
                cyli_arr.append(temp_cylin)
        elif f['type'] == "cuboids":
            for cuboid in f['params']:
                temp_cuboid = Cuboid(cuboid['x'], cuboid['y'], cuboid['z'], cuboid['a'], cuboid['b'], cuboid['c'])
                cub_arr.append(temp_cuboid)
        elif f['type'] == "spheres":
            for sphere in f['params']:
                temp_sphere = Sphere(sphere['x'], sphere['y'], sphere['z'], sphere['radius'], sphere['meridians'], sphere['parallels'])
                sphere_arr.append(temp_sphere)

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

T = np.eye(4)
T[3,1] = 0
T2 = np.eye(4)
T2[3,1] = 0
T2[3,2] = 5

camera = np.zeros(3)

cubvert = []
cubtoshow = cub_arr[0]
conetoshow = cones_arr[0]
cylitoshow = cyli_arr[0]
spheretoshow = sphere_arr[0]

pygame.display.flip()

def draw_triangle(x1,y1,x2,y2,x3,y3,color):
    pygame.draw.line(display_game, pygame.color.THECOLORS[color], (x1,y1), (x2,y2),1)
    pygame.draw.line(display_game, pygame.color.THECOLORS[color], (x2,y2), (x3,y3),1)
    pygame.draw.line(display_game, pygame.color.THECOLORS[color], (x3,y3), (x1,y1),1)

def redraw(x_rot, y_rot, z_rot):
    R_x = np.array([
        [1, 0, 0, 0],
        [0, cos(x_rot), sin(x_rot), 0],
        [0, -sin(x_rot), cos(x_rot), 0],
        [0, 0, 0, 1]
    ])

    R_y = np.array([
        [cos(y_rot), 0, -sin(y_rot), 0],
        [0,1,0,0],
        [sin(y_rot), 0, cos(y_rot),0],
        [0,0,0,1]
    ])

    R_z = np.array([
        [cos(z_rot), -sin(z_rot), 0, 0],
        [sin(z_rot), cos(z_rot), 0, 0],
        [0, 0, 1, 0],
        [0,0,0,1]
    ])

    the_matrix = np.eye(4).dot(T).dot(R_y).dot(R_x).dot(R_z).dot(T2)
    for point in cubvert:
        point = point.dot(the_matrix)
    display_game.fill((0,0,0))
    for conetoshow in cones_arr:
        for tri in conetoshow.get_triangles(conetoshow.get_vertices()):
            verts = tri.get_vertices()
            for i in range(3):
                verts[i] = verts[i].get_coords().dot(the_matrix)
            ctr = np.array([2.5, 1.5, 0, 0])
            for i in range(3):
                verts[i] = (verts[i].dot(M) / verts[i][2] + ctr) / 2
                verts[i] = verts[i].dot(S)
            draw_triangle(verts[0][0], verts[0][1], verts[1][0], verts[1][1], verts[2][0], verts[2][1], 'white')
    for cubtoshow in cub_arr:
        for tri in cubtoshow.get_triangles(cubtoshow.get_vertices()):
            verts = tri.get_vertices()
            for i in range(3):
                verts[i] = verts[i].get_coords().dot(the_matrix)
            ctr = np.array([2.5, 1.5, 0, 0])
            for i in range(3):
                verts[i] = (verts[i].dot(M) / verts[i][2] + ctr) / 2
                verts[i] = verts[i].dot(S)
            draw_triangle(verts[0][0], verts[0][1], verts[1][0], verts[1][1], verts[2][0], verts[2][1], 'blue')
    for cylitoshow in cyli_arr:
        for tri in cylitoshow.get_triangles(cylitoshow.get_vertices()):
            verts = tri.get_vertices()
            for i in range(3):
                verts[i] = verts[i].get_coords().dot(the_matrix)
            ctr = np.array([2.5, 1.5, 0, 0])
            for i in range(3):
                verts[i] = (verts[i].dot(M) / verts[i][2] + ctr) / 2
                verts[i] = verts[i].dot(S)
            draw_triangle(verts[0][0], verts[0][1], verts[1][0], verts[1][1], verts[2][0], verts[2][1], 'red')
    for spheretoshow in sphere_arr:
        for tri in spheretoshow.get_triangles(spheretoshow.get_vertices()):
            verts = tri.get_vertices()
            for i in range(3):
                verts[i] = verts[i].get_coords().dot(the_matrix)
            ctr = np.array([2.5, 1.5, 0, 0])
            for i in range(3):
                verts[i] = (verts[i].dot(M) / verts[i][2] + ctr) / 2
                verts[i] = verts[i].dot(S)
            draw_triangle(verts[0][0], verts[0][1], verts[1][0], verts[1][1], verts[2][0], verts[2][1], 'green')
    pygame.display.flip()

    

rot_const = pi/60
xR = 0
yR = 0
zR = pi
redraw(xR, yR, zR)
isRedraw = False
isLeft = False
isRight = False
isUp = False
isDown = False
isClose = False
isFar = False
isZooming = False
isOngoing = True
while isOngoing:
    for event in pygame.event.get():
        if event.type == QUIT:
            isOngoing = False
            pygame.display.quit()
            pygame.quit()
            break
        
        if event.type == KEYDOWN:
            if event.key == K_w:
                isUp = True
            if event.key == K_s:
                isDown = True
            if event.key == K_a:
                isLeft = True
            if event.key == K_d:
                isRight = True
            if event.key == K_z:
                isClose = True
            if event.key == K_x:
                isFar = True
            if event.key == K_q:
                if T2[3,2] > 2:
                    T2[3,2] -= 1
                    isZooming = True
            if event.key == K_e:
                T2[3,2] += 1
                isZooming = True
        
        if event.type == KEYUP:
            if event.key == K_w:
                isUp = False
            if event.key == K_s:
                isDown = False
            if event.key == K_a:
                isLeft = False
            if event.key == K_d:
                isRight = False
            if event.key == K_z:
                isClose = False
            if event.key == K_x:
                isFar = False
    
    if isUp:
        xR += rot_const
    elif isDown:
        xR -= rot_const
    if isLeft:
        yR -= rot_const
    elif isRight:
        yR += rot_const
    if isClose:
        zR += rot_const
    elif isFar:
        zR -= rot_const
    
    if isUp or isDown or isLeft or isRight or isClose or isFar or isZooming:
        redraw(xR, yR, zR)
        isZooming = False
    
    CLOCK.tick(30)



time.sleep(15)

exit(0)