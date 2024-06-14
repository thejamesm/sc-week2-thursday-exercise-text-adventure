class Item:
    def __init__(self, item_name):
        self.name = item_name
        self.description = None

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