# Jakub Tłuczek 2020
from cone import Cone
from cuboid import Cuboid
from cylinder import Cylinder
from sphere import Sphere
from triangle import Vertex, Triangle
import json
import pygame
from pygame.locals import *
import time
import numpy as np
from math import pi, sin, cos

# sources
#
# trimesh tutorial and slides
# https://en.wikipedia.org/wiki/3D_projection
# https://en.wikipedia.org/wiki/Transformation_matrix
# Botsch, Kobbelt, Pauly, Alliez, Leby "Polygonal Mesh Processing"
# Khan Academy videos on youtube
# javidx9 "3d graphics engine course" on youtube
# https://medium.com/swlh/understanding-3d-matrix-transforms-with-pixijs-c76da3f8bd8


# program parameters
FILE = "pajacyk.json"
width = 1200
height = 600
SPEED = 1/60
FPS = 60

# Setting up pygame
# https://pythonprogramming.net/pygame-python-3-part-1-intro/
pygame.init()
pygame.display.set_caption('3D Scene loader - provide JSON to visualize - controls in README')
display_game = pygame.display.set_mode((width, height))
CLOCK = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 36)
CLOCK.tick(FPS)
pygame.display.flip()
time.sleep(2)

# figure arrays
cones_arr = []
cyli_arr = []
cub_arr = []
sphere_arr = []

# draw triangle utility
def draw_triangle(p1,p2,p3,color):
    try:
        pygame.draw.line(display_game, pygame.color.THECOLORS[color], (p1[0],p1[1]), (p2[0],p2[1]),1)
    except Exception:
        pass

    try:
        pygame.draw.line(display_game, pygame.color.THECOLORS[color], (p2[0],p2[1]), (p3[0],p3[1]),1)
    except Exception:
        pass

    try:
        pygame.draw.line(display_game, pygame.color.THECOLORS[color], (p1[0],p1[1]), (p3[0],p3[1]),1)
    except Exception:
        pass

# transform vertex function
def transform_vert(vert, matr):
    tmp = vert.get_coords().dot(matr)
    tmp = ((tmp.dot(M) / tmp[2] + C) / 2).dot(S)
    return tmp

# parsing JSON file
with open(FILE) as json_file:
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
                temp_sphere = Sphere(sphere['x'], sphere['y'], sphere['z'], sphere['radius'], \
                    sphere['meridians'], sphere['parallels'])
                sphere_arr.append(temp_sphere)

# Global variables, matrices, and triggers
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

S = np.eye(4)
# I've chosen 450 by trying several values and it looks to be the optimal choice
S[0,0] = 450
S[1,1] = 450

# since we start to look at the origin, T is just an identity matrix
T = np.eye(4)

# zoom set to 30 (away)
Z = np.eye(4)
Z[3,2] = 30

camera = np.zeros(3)

# same as in S matrix - 2,1,.. seems t0o little, 3,2,.. however is too much
C = np.array([2.5, 1.5, 0, 0])

isRedraw = False
isLeft = False
isRight = False
isUp = False
isDown = False
isCounterclockwise = False
isClockwise = False
isZooming = False
isOngoing = True

pygame.display.flip()

def redraw(x_alfa, y_alfa, z_alfa):
    # rotation matrices
    R_x = np.array([
        [1, 0, 0, 0],
        [0, cos(x_alfa), sin(x_alfa), 0],
        [0, -sin(x_alfa), cos(x_alfa), 0],
        [0, 0, 0, 1]
    ])

    R_y = np.array([
        [cos(y_alfa), 0, -sin(y_alfa), 0],
        [0,1,0,0],
        [sin(y_alfa), 0, cos(y_alfa),0],
        [0,0,0,1]
    ])

    R_z = np.array([
        [cos(z_alfa), -sin(z_alfa), 0, 0],
        [sin(z_alfa), cos(z_alfa), 0, 0],
        [0, 0, 1, 0],
        [0,0,0,1]
    ])

    # all needed matrices combined in one
    # first we have to muliply by rotation of y, then by rotation of x
    # First I tried to multiply them in the order from "trimesh" instruction
    # but movement of camera was not the way I wanted it to be
    # zoom has to be applied at the end
    # T here is redundant, however if someone would like to change translation matrix
    # it has to be done before rotations
    the_matrix = np.eye(4).dot(T).dot(R_y).dot(R_x).dot(R_z).dot(Z)

    # main part of redrawing
    # clearing screen before redrawing
    display_game.fill((0,0,0))
    # transforming and redrawing each figures array
    # each class has get_triangles method which returns all triangles, formed by 
    # vertices in get_vertices() method, passed as an argument
    for conetoshow in cones_arr:
        for tri in conetoshow.get_triangles(conetoshow.get_vertices()):
            verts = tri.get_vertices()
            for i in range(3):
                verts[i] = transform_vert(verts[i], the_matrix)
            draw_triangle(verts[0], verts[1], verts[2], 'white')
    for cubtoshow in cub_arr:
        for tri in cubtoshow.get_triangles(cubtoshow.get_vertices()):
            verts = tri.get_vertices()
            for i in range(3):
                verts[i] = transform_vert(verts[i], the_matrix)
            draw_triangle(verts[0], verts[1], verts[2], 'blue')
    for cylitoshow in cyli_arr:
        for tri in cylitoshow.get_triangles(cylitoshow.get_vertices()):
            verts = tri.get_vertices()
            for i in range(3):
                verts[i] = transform_vert(verts[i], the_matrix)
            draw_triangle(verts[0], verts[1], verts[2], 'red')
    for spheretoshow in sphere_arr:
        for tri in spheretoshow.get_triangles(spheretoshow.get_vertices()):
            verts = tri.get_vertices()
            for i in range(3):
                verts[i] = transform_vert(verts[i], the_matrix)
            draw_triangle(verts[0], verts[1], verts[2], 'green')
    pygame.display.flip()

rot_const = pi * SPEED
xR = 0
yR = 0
zR = pi
# initial image
redraw(xR, yR, zR)
# standard pygame routine
# https://stackoverflow.com/questions/46594447/pygame-event-handling-key-events
# https://riptutorial.com/pygame/example/18046/event-loop
while isOngoing:
    for event in pygame.event.get():
        if event.type == QUIT:
            isOngoing = False
            pygame.quit()
            break
        
        elif event.type == KEYDOWN:
            if event.key == K_w:
                isUp = True
            elif event.key == K_s:
                isDown = True
            elif event.key == K_a:
                isLeft = True
            elif event.key == K_d:
                isRight = True
            elif event.key == K_z:
                isCounterclockwise = True
            elif event.key == K_x:
                isClockwise = True
            elif event.key == K_ESCAPE:
                isOngoing = False
                pygame.quit()
                break
            elif event.key == K_q:
                if Z[3,2] > 1:
                    Z[3,2] -= 1
                    isZooming = True
            elif event.key == K_e:
                if Z[3,2] < 100:
                    Z[3,2] += 1
                    isZooming = True
        
        elif event.type == KEYUP:
            if event.key == K_w:
                isUp = False
            elif event.key == K_s:
                isDown = False
            elif event.key == K_a:
                isLeft = False
            elif event.key == K_d:
                isRight = False
            elif event.key == K_z:
                isCounterclockwise = False
            elif event.key == K_x:
                isClockwise = False
    
    if isUp:
        xR -= rot_const
    elif isDown:
        xR += rot_const
    if isLeft:
        yR += rot_const
    elif isRight:
        yR -= rot_const
    if isCounterclockwise:
        zR += rot_const
    elif isClockwise:
        zR -= rot_const
    
    if isUp is True or isDown is True or isLeft is True or isRight is True or \
        isCounterclockwise is True or isClockwise is True or isZooming is True:
        redraw(xR, yR, zR)
        isZooming = False
    
    CLOCK.tick(FPS)
