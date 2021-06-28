class Car:

    _test = "test"
    __private = "don't touch me!"

    def __init__(self, make, model, door_count = 4):
        self.make = make
        self.model = model
        self.door_count = door_count

        self._protected = "this value is not for your eyes"

    def __str__(self):
        return f"{self.make} {self.model}"

    def __repr__(self):
        return f"this is instance of Car with values: make - {self.make}, model - {self.model}"

new_car = Car("vw", "up!", 3)
# new_car.door_count = 333
print(new_car.make, new_car.model, new_car.door_count)
print(new_car._protected)
print(new_car._test)
print(new_car._Car__private)
# print(Car.__private)

print(str(new_car))
print(repr(new_car))