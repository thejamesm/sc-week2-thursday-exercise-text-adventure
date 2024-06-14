class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

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
        return True