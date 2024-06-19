class Item:
    def __init__(self, item_name: str, item_description: str) -> None:
        self.name = item_name
        self.description = item_description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, new_description: str) -> None:
        self.__description = new_description

    def describe(self) -> None:
        print(self.description)