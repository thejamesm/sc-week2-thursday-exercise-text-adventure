from item import Item

class Room:
    directions = ("north", "east", "south", "west")
    dir_opposites = {
        "north": "south",
        "east": "west",
        "south": "north",
        "west": "east"
    }

    def __init__(self, room_name, room_description):
        self.name = room_name
        self.description = room_description
        self.__linked_rooms = {}
        self.locked = False
        self.key = None
        self.character = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @property
    def locked(self):
        return self.__locked

    @locked.setter
    def locked(self, lock_status):
        self.__locked = lock_status

    @property
    def locked_doors(self):
        return {direction: room
                for direction, room in self.linked_rooms.items()
                if room.locked}

    @property
    def key(self):
        return self.__key

    @property
    def character(self):
        return self.__character

    @character.setter
    def character(self, new_character):
        self.__character = new_character

    @key.setter
    def key(self, key_item):
        if isinstance(key_item, Item) or key_item is None:
            self.__key = key_item
        else:
            raise TypeError("Key must be an Item")

    def lock(self, key_item):
        self.locked = True
        self.key = key_item

    def unlock(self, key_item):
        if isinstance(key_item, Item):
            if key_item == self.key:
                self.locked = False
                print(f"You open the door with the {key_item.name}")
                return True
            else:
                print(f"The {key_item.name} doesn't open this door")
                return False
        else:
            raise TypeError("Key must be an Item")

    def describe(self):
        print(self.description)

    @property
    def linked_rooms(self):
        return self.__linked_rooms

    def link_room(self, room_to_link, direction):
        if not isinstance(room_to_link, Room):
            raise TypeError("Rooms can only link to other Rooms")
        if direction not in Room.directions:
            raise ValueError(f"Not a permitted direction {Room.directions}")
        if room_to_link == self:
            raise ValueError("Room cannot link to itself")
        else:
            self.__linked_rooms[direction] = room_to_link

    def two_way_link(self, room_to_link, direction):
        self.link_room(room_to_link, direction)
        room_to_link.link_room(self, Room.dir_opposites[direction])

    def get_details(self):
        print(self.name)
        print("----------------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print(f"The {room.name} is {direction}")

    def move(self, direction):
        if direction in self.linked_rooms:
            destination = self.linked_rooms[direction]
            if destination.locked:
                print(f"The door to the {destination.name} is locked")
                return self
            else:
                return destination
        else:
            print("You can't go that way")
            return self