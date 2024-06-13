from room import Room

class Player:
    def __init__(self, player_name, player_location):
        self.name = player_name
        self.location = player_location

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) == 0:
            raise ValueError("Zero-length names not permitted")
        self.__name = new_name

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, new_location):
        if not isinstance(new_location, Room):
            raise TypeError("Location must be a Room")
        self.__location = new_location

    def description(self):
        return f"> {self.name} is in the {self.location.name}"

    def describe(self):
        print(self.description())

    def move(self, direction):
        if direction not in self.location.linked_rooms:
            raise ValueError("Not a valid exit from the current location")
        self.location = self.location.linked_rooms[direction]
        print(f"> {self.name} moves {direction} to the {self.location.name}")