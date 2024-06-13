class Room:
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

    def link_room(self, room_to_link, direction):
        self.__linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print("-------------------------")
        print(self.description)
        for direction in self.__linked_rooms:
            room = self.__linked_rooms[direction]
            print(f"The {room.name} is {direction}")