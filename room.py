class Room:
    def __init__(self, room_name):
        self.set_name(room_name)
        self.set_description(None)
        self.linked_rooms = {}

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_description(self):
        return self.__description

    def set_description(self, new_description):
        self.__description = new_description

    def describe(self):
        print(self.get_description())

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.get_name())
        print("-------------------------")
        print(self.get_description())
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")