#################
# Object module #
#################

from abc import ABC, abstractmethod


class RoomSide:
    locations = ('left', 'right', 'top', 'bottom')

    def __init__(self, **kwds):
        self.__location = self.locations[0]
        self._location(kwds.get('location'))
        self.__lenght = 40
        self._lenght(kwds.get('lenght'))
        self.__is_wall = True
        self._is_wall(kwds.get('is_wall'))

    def _location(self, location=None):
        if isinstance(location, str) and location in self.locations:
            self.__location = location
        return self.__location

    def _lenght(self, lenght=None):
        if isinstance(lenght, int):
            self.__lenght = lenght
        return self.__lenght

    def _is_wall(self, is_wall=None):
        if is_wall is not None:
            self.__is_wall = bool(is_wall)
        return self.__is_wall


class Room:
    def __init__(self, **kwds):
        self.__sides = {i: RoomSide(location=i, lenght=kwds.get('side_lenght')) for i in RoomSide.locations}
        self.__coords = (0, 0)
        self.coords(kwds.get('coords'))
        self.__available_rooms = {}
        self.available_rooms(available_rooms=kwds.get('available_rooms'), update=False)

    def __str__(self):
        return f'Room at {self.__coords}'

    def coords(self, coords=None):
        if isinstance(coords, (list, tuple)):
            self.__coords = tuple(coords)
        return self.__coords

    def side_lenght(self, lenght=None):
        if isinstance(lenght, int):
            for v in self.__sides.values():
                v._lenght(lenght)
        return self.__sides[list(self.__sides.keys())[0]]._lenght()

    def side_is_wall(self, location=None, is_wall=None):
        if isinstance(location, str) and location in self.__sides:
            if is_wall is not None:
                self.__sides[location]._is_wall(is_wall)
            return self.__sides[location]._is_wall()
        # ! return None = False

    def get_walls_locations(self):
        return [k for k, v in self.__sides.items() if v._is_wall()]

    def available_rooms(self, available_rooms=None, update=True):
        if isinstance(available_rooms, dict):
            if update:
                self.__available_rooms.update(available_rooms)
            else:
                self.__available_rooms = available_rooms
        return self.__available_rooms

    def get_available_room_location(self, available_room=None):
        if isinstance(available_room, Room):
            if available_room in self.__available_rooms.values() and self in available_room.available_rooms().values():
                return list(self.__available_rooms)[list(self.__available_rooms.values()).index(available_room)]
        # ! return None


class ObjInRoom(ABC):
    shapes = ('random', 'turtle', 'arrow', 'classic', 'circle', 'square', 'triangle')
    colors = ('random', 'blue', 'red', 'yellow', 'orange', 'green', 'purple', 'white', 'grey', 'black')

    def __init__(self, **kwds):
        self.__current_room = None
        self.current_room(kwds.get('current_room'))

    @abstractmethod
    def __str__(self):
        pass

    def current_room(self, current_room=None):
        if isinstance(current_room, Room):
            self.__current_room = current_room
        return self.__current_room


class Artifact(ObjInRoom):
    shapes = ('random', 'circle', 'square', 'triangle')
    colors = ('random', 'white', 'grey', 'black')

    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.__value = 0
        self.value(kwds.get('value'))

    @abstractmethod
    def __str__(self):
        pass

    def value(self, value=None):
        if isinstance(value, int):
            self.__value = value
        return self.__value


class Strength(Artifact):
    def __str__(self):
        return f'Artifact "strength" [+{self.value()}] in {self.current_room()}'.capitalize().replace('+-', '-')


class Hero(ObjInRoom):
    shapes = ('random', 'turtle', 'arrow', 'classic')
    colors = ('random', 'blue', 'red', 'yellow', 'orange', 'green', 'purple')

    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.__num_moves_at_time = 1
        self.num_moves_at_time(kwds.get('num_moves_at_time'))
        self.__strength = 0
        self.strength(kwds.get('strength'))

    @abstractmethod
    def __str__(self):
        pass

    def num_moves_at_time(self, num_moves_at_time=None):
        if isinstance(num_moves_at_time, int):
            self.__num_moves_at_time = num_moves_at_time
        return self.__num_moves_at_time

    def strength(self, strength=None):
        if isinstance(strength, int):
            self.__strength = strength
        return self.__strength


class PositiveHero(Hero):
    def __str__(self):
        return f'Positive hero [strength {self.strength()}]'


class NegativeHero(Hero):
    def __str__(self):
        return f'Negative hero [strength {self.strength()}]'
