from item import Item

class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.item = None

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
    def conversation(self):
        return self.__conversation

    @conversation.setter
    def conversation(self, new_conversation):
        self.__conversation = new_conversation

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, new_item):
        if isinstance(new_item, Item) or new_item is None:
            self.__item = new_item
        else:
            raise TypeError("Character item must be of Item class")

    def describe(self):
        print(self.name, "is here!")
        print(self.description)

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]:", self.conversation)
        else:
            print(self.name, "doesn't want to talk to you")

    def fight(self, combat_item):
        print(self.name, "doesn't want to fight with you")
        return True, None

    def steal(self):
        if self.item:
            theft_item = self.item
            self.item = None
            print(f"You steal a {theft_item.name} from {self.name}")
            return theft_item
        else:
            print(f"{self.name} isn't carrying anything")
            return None


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    @property
    def weakness(self):
        return self.__weakness

    @weakness.setter
    def weakness(self, item_weakness):
        if isinstance(item_weakness, Item) or item_weakness is None:
            self.__weakness = item_weakness
        else:
            raise TypeError("Weakness must be an Item")

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item.name}")
            if self.item:
                print(f"{self.name} drops a {self.item.name}")
            return True, self.item
        else:
            print(f"{self.name} crushes  you, puny adventurer")
            return False, None


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def hug(self):
        print(f"You give {self.name} a big hug")

    def fight(self, combat_item):
        print("You would never fight a friend!")
        return True, None