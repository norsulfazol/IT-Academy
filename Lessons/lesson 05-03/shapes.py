import shapes_utilits as su
import abc

class BasicShape(abc.ABC):

    @abc.abstractmethod
    def __init__(self, x):
        pass

    @abc.abstractmethod
    def get_x(self):
        pass

    @classmethod
    def set_description(cls, description):
        cls.__description = description

    @classmethod
    def get_description(cls):
        return cls.__description

    def set_alt_descr(self, descr):
        BasicShape.__alt_descr = descr

    def get_alt_descr(self):
        return BasicShape.__alt_descr

class Circle(BasicShape): pass

    # def __init__(self, x):
    #     super().__init__(x)

    # def get_x(self):
    #     return super().get_x()

class Square(BasicShape): pass

    # def __init__(self, x):
    #     super().__init__(x)

    # def get_x(self):
    #     return super().get_x()

class Rectangle(BasicShape):

    def __init__(self, x, y):
        super().__init__(x)
        self.__y = y

    # def get_x(self):
    #     return super().get_x()

    def get_y(self):
        return self.__y


c = Circle(5)
c.set_description("This a circle shape")
print(c.get_description())
c2 = Circle(2)
print(c2.get_description())
s = su.ShapesUtilits.circle_square(c)
print(s)