import math

class ShapesUtilits:

    @staticmethod
    def circle_square(circle):
        r = circle.get_x()
        return math.pi*r*r

    @staticmethod
    def square_square(square):
        s = square.get_x()
        return s*s

    @staticmethod
    def rectangle_square(rectangle):
        side1 = rectangle.get_x()
        side2 = rectangle.get_y()
        return side1*side2