class Room:
    dir_opposites = {
        "north": "south",
        "east": "west",
        "south": "north",
        "west": "east"
    }

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.__linked_rooms = {}

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

    def describe(self):
        print(self.description)

    @property
    def linked_rooms(self):
        return self.__linked_rooms

    def link_room(self, room_to_link, direction):
        self.__linked_rooms[direction] = room_to_link

    def two_way_link(self, room_to_link, direction):
        self.link_room(room_to_link, direction)
        room_to_link.link_room(self, Room.dir_opposites[direction])

    def get_details(self):
        print(self.name)
        print("-------------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print(f"The {room.name} is {direction}")