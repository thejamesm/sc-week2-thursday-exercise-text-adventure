from room import Room
from character import Enemy, Friend
from inventory import Inventory

class Game:
    command_aliases: dict[str, str] = {
        "n": "north",
        "e": "east",
        "s": "south",
        "w": "west",
        "rob": "steal",
        "take": "steal",
        "open": "unlock",
        "inv": "inventory",
        "i": "inventory",
        "items": "inventory",
        "pockets": "inventory",
        "pocket": "inventory",
        "bag": "inventory",
        "exit": "quit"
    }

    def __init__(self, start_room: Room) -> None:
        self.__room: Room = start_room
        self.__inventory: Inventory = Inventory()
        self.commands: dict[str, function] = {
            "move": self.move,
            "talk": self.talk,
            "fight": self.fight,
            "steal": self.steal,
            "hug": self.hug,
            "unlock": self.unlock,
            "inventory": self.list_inventory,
            "quit": self.quit
        }
        self.game_loop()

    def game_loop(self) -> None:
        while True:
            print()
            self.__room.get_details()
            if self.__room.character:
                self.__room.character.describe()
            command = input("> ").lower()
            print()
            self.execute_command(command)

    def execute_command(self, command: str) -> None:
        if command in Game.command_aliases:
            command = Game.command_aliases[command]
        if command in Room.directions:
            self.move(command)
        elif command in self.commands:
            self.commands[command]()
        else:
            print(f"I don't understand \"{command}\"")

    def move(self, direction: str) -> None:
        self.__room = self.__room.move(direction)

    def talk(self) -> None:
        if self.__room.character:
            self.__room.character.talk()
        else:
            print("There's nobody here")

    def fight(self) -> None:
        character = self.__room.character
        if character:
            print("What will you fight with?")
            combat_item = self.__inventory.choose_item()
            if combat_item:
                combat_result, dropped_item = character.fight(combat_item)
                if combat_result:
                    if isinstance(character, Enemy):
                        self.__room.character = None
                        if dropped_item:
                            self.__inventory.add_item(dropped_item)
                else:
                    print()
                    print("~~~ You lose! ~~~")
                    print()
                    exit()
            else:
                print("You decide it would be better not to fight right now")
        else:
            print("There's nobody here")

    def steal(self) -> None:
        if self.__room.character:
            stolen_item = self.__room.character.steal()
            if stolen_item:
                self.__inventory.add_item(stolen_item)
        else:
            print("There's nobody here")

    def hug(self) -> None:
        character = self.__room.character
        if character and isinstance(character, Friend):
            character.hug()
        else:
            print("There's nobody here that you want to hug")

    def unlock(self) -> None:
        current_room = self.__room
        locked_doors = current_room.locked_doors
        if len(locked_doors) > 0:
            if len(locked_doors) > 1:
                direction = ""
                while direction not in locked_doors:
                    print("Which door do you want to unlock?")
                    direction = input("> ")
            else:
                direction = tuple(locked_doors.keys())[0]
            print("What will you use?")
            key_item = self.__inventory.choose_item()
            if key_item:
                return locked_doors[direction].unlock(key_item)
            else:
                print("You decide to go somewhere else instead")
                return False
        else:
            print("There are no locked doors here")
            return False

    def list_inventory(self) -> None:
        self.__inventory.list_inventory()

    def quit(self) -> None:
        exit()