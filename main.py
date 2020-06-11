from cone import Cone
from cuboid import Cuboid
from cylinder import Cylinder
from sphere import Sphere
import json

cone1 = Cone(3, 4)
cuboid1 = Cuboid(3,4,5)
cylinder1 = Cylinder(5,6)
sphere1 = Sphere(3)

print(cone1.get_area())
print(cuboid1.get_area())
print(cylinder1.get_area())
print(sphere1.get_area())

with open('examp.json') as json_file:
    data = json.load(json_file)
    for f in data['figures']:
        if f['type'] == "cones":
            for cone in f['params']:
                temp_con = Cone(cone['radius'], cone['height'])
                print("Cone's area: " + str(temp_con.get_area())) 
        elif f['type'] == "cylinders":
            for cylinder in f['params']:
                temp_cylin = Cylinder(cylinder['radius'], cylinder['height'])
                print("Cylinder's area: " + str(temp_cylin.get_area()))
        elif f['type'] == "cuboids":
            for cuboid in f['params']:
                temp_cuboid = Cuboid(cuboid['a'], cuboid['b'], cuboid['c'])
                print("Cuboid's area: " + str(temp_cuboid.get_area()))
        elif f['type'] == "spheres":
            for sphere in f['params']:
                temp_sphere = Sphere(sphere['radius'])
                print("Sphere's area: " + str(temp_sphere.get_area()))