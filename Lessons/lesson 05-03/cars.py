class Engine:

    def __init__(self, volume, power, torque):
        self.__volume = volume
        self.__power = power
        self.__torque = torque
    
    def get_volume(self):
        return self.__volume

    def get_power(self):
        return self.__power

    def get_torque(self):
        return self.__torque

class Car_Composition:

    def __init__(self, make, model, volume, power, torque):
        self.__make = make
        self.__model = model
        self.__engine = Engine(volume, power, torque)

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_volume(self):
        return self.__engine.get_volume()

    def get_power(self):
        return self.__engine.get_power()

    def get_torque(self):
        return self.__engine.get_torque()

class Car_Aggregation():

    def __init__(self, make, model, engine):
        self.__make = make
        self.__model = model
        self.__engine = engine

compose = Car_Composition("audi", "a4", 2.0, 249, 350)
compose.get_power()

engine = Engine(2.0, 249, 350)
aggr = Car_Aggregation("audi", "a4", engine)

engine.get_power()