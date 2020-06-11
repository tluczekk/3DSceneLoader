from cone import Cone
from cuboid import Cuboid
from cylinder import Cylinder
from sphere import Sphere

cone1 = Cone(3, 4)
cuboid1 = Cuboid(3,4,5)
cylinder1 = Cylinder(5,6)
sphere1 = Sphere(3)

print(cone1.get_area())
print(cuboid1.get_area())
print(cylinder1.get_area())
print(sphere1.get_area())