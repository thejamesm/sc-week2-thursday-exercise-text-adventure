from item import Item

class Character:
    def __init__(self, char_name, char_description) -> None:
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.item = None

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name) -> None:
        self.__name = new_name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, new_description) -> None:
        self.__description = new_description

    @property
    def conversation(self) -> str:
        return self.__conversation

    @conversation.setter
    def conversation(self, new_conversation) -> None:
        self.__conversation = new_conversation

    @property
    def item(self) -> Item:
        return self.__item

    @item.setter
    def item(self, new_item) -> None:
        if isinstance(new_item, Item) or new_item is None:
            self.__item = new_item
        else:
            raise TypeError("Character item must be of Item class")

    def describe(self) -> None:
        print(self.name, "is here!")
        print(self.description)

    def talk(self) -> None:
        if self.conversation is not None:
            print(f"[{self.name} says]:", self.conversation)
        else:
            print(self.name, "doesn't want to talk to you")

    def fight(self, combat_item) -> tuple[bool, Item | None]:
        print(self.name, "doesn't want to fight with you")
        return True, None

    def steal(self) -> Item | None:
        if self.item:
            theft_item = self.item
            self.item = None
            print(f"You steal a {theft_item.name} from {self.name}")
            return theft_item
        else:
            print(f"{self.name} isn't carrying anything")
            return None


class Enemy(Character):
    def __init__(self, char_name, char_description) -> None:
        super().__init__(char_name, char_description)
        self.weakness = None

    @property
    def weakness(self) -> Item | None:
        return self.__weakness

    @weakness.setter
    def weakness(self, item_weakness) -> None:
        if isinstance(item_weakness, Item) or item_weakness is None:
            self.__weakness = item_weakness
        else:
            raise TypeError("Weakness must be an Item")

    def fight(self, combat_item) -> tuple[bool, Item | None]:
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item.name}")
            if self.item:
                print(f"{self.name} drops a {self.item.name}")
            return True, self.item
        else:
            print()
            print(f"{self.name} crushes  you, puny adventurer")
            return False, None


class Friend(Character):
    def __init__(self, char_name, char_description) -> None:
        super().__init__(char_name, char_description)

    def hug(self) -> None:
        print(f"You give {self.name} a big hug")

    def fight(self, combat_item) -> tuple[bool, Item | None]:
        print("You would never fight a friend!")
        return True, None