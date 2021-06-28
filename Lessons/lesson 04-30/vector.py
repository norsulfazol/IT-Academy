class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # def sum(self, other):
    #     return Vector(self.x + other.x, self.y + other.y)

def my_sum(self, other):
    return "test"

v1 = Vector(2, -3)
v2 = Vector(3, 7)
l = [(2,3), (v1, v2), (2, "test")]
for t in l:
    print(t)
    print(t[0]+t[1])
