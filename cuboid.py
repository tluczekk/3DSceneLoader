class Cuboid:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def get_area(self):
        return 2*(self.a*self.b + self.a*self.c + self.b*self.c)