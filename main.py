from cone import Cone
from cuboid import Cuboid
from cylinder import Cylinder
from sphere import Sphere
import json

# parsing JSON file
with open('examp.json') as json_file:
    data = json.load(json_file)
    for f in data['figures']:
        if f['type'] == "cones":
            for cone in f['params']:
                temp_con = Cone(cone['x'], cone['y'], cone['z'], cone['radius'], cone['height'])
                print("Cone's position: [" + str(temp_con.position[0]) + ", " + \
                    str(temp_con.position[1]) + ", " + str(temp_con.position[2]) + "]") 
                print("Cone's area: " + str(temp_con.get_area())) 
        elif f['type'] == "cylinders":
            for cylinder in f['params']:
                temp_cylin = Cylinder(cylinder['x'], cylinder['y'], cylinder['z'], \
                    cylinder['radius'], cylinder['height'])
                print("Cylinder's area: " + str(temp_cylin.get_area()))
        elif f['type'] == "cuboids":
            for cuboid in f['params']:
                temp_cuboid = Cuboid(cuboid['x'], cuboid['y'], cuboid['z'], cuboid['a'], \
                    cuboid['b'], cuboid['c'])
                print("Cuboid's area: " + str(temp_cuboid.get_area()))
        elif f['type'] == "spheres":
            for sphere in f['params']:
                temp_sphere = Sphere(sphere['x'], sphere['y'], sphere['z'], sphere['radius'])
                print("Sphere's area: " + str(temp_sphere.get_area()))