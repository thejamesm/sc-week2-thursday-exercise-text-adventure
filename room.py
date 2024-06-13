class Room:
    def __init__(self, room_name):
        self.set_name(room_name)
        # self.name = room_name
        self.set_description(None)
        # self.description = None
        self.linked_rooms = {}

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    # @property
    # def name(self):
    #     return self.__name

    def get_description(self):
        return self.__description

    def set_description(self, new_description):
        self.__description = new_description

    # @property
    # def description(self):
    #     return self.__description

    def describe(self):
        print(self.get_description())

    # def describe(self):
    #     print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)