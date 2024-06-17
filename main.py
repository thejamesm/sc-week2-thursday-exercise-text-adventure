from room import Room
from item import Item
from inventory import Inventory
from character import Enemy, Friend


def move(direction):
    global current_room
    current_room = current_room.move(direction)

def talk(character):
    if character:
        character.talk()
    else:
        print("There's nobody here")

def fight(character):
    global current_room, inventory
    if character:
        print("What will you fight with?")
        combat_item = inventory.choose_item()
        if combat_item:
            combat_result, dropped_item = character.fight(combat_item)
            if combat_result:
                if isinstance(character, Enemy):
                    current_room.character = None
                    if dropped_item:
                        inventory.add_item(dropped_item)
            else:
                print()
                print("~~~ You lose! ~~~")
                print()
                exit()
        else:
            print("You decide it would be better not to fight right now")
    else:
        print("There's nobody here")

def steal(character):
    global inventory
    if character:
        stolen_item = character.steal()
        if stolen_item:
            inventory.add_item(stolen_item)
    else:
        print("There's nobody here")

def hug(character):
    if character and isinstance(character, Friend):
        character.hug()
    else:
        print("There's nobody here that you want to hug")

def unlock():
    global current_room
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
        key_item = inventory.choose_item()
        if key_item:
            if locked_doors[direction].unlock(key_item):
                current_room = current_room.move(direction)
        else:
            print("You decide to go somewhere else instead")
    else:
        print("There are no locked doors here")

def list_inventory():
    global inventory
    inventory.list_inventory()


command_aliases = {
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

inventory = Inventory()

kitchen = Room("kitchen")
kitchen.description = "A dank and dirty room buzzing with flies"
ballroom = Room("ballroom")
ballroom.description = "A vast room with a shiny wooden floor"
dining_hall = Room("dining hall")
dining_hall.description = "A large room with ornate golden decorations"
garden = Room("garden")
garden.description = "You made it to the garden. You win!"

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(garden, "east")
ballroom.link_room(dining_hall, "east")
garden.link_room(dining_hall, "west")

cheese = Item("cheese", "A pungent block of cheese")
key = Item("key", "A shiny silver key")

dave = Enemy("Dave", "A smelly zombie")
dave.conversation = "Brrlgrh... rgrhl... brains..."
dave.weakness = cheese
dave.item = key

catrina = Friend("Catrina", "A friendly skeleton")
catrina.conversation = "Hi, how are you?"
catrina.item = cheese

dining_hall.character = dave
ballroom.character = catrina

garden.lock(key)

current_room = kitchen
while True:
    print()
    current_room.get_details()

    inhabitant = current_room.character
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ").lower()
    print()

    if command in command_aliases:
        command = command_aliases[command]

    if command in ("north", "east", "south", "west"):
        move(command)
    elif command == "talk":
        talk(inhabitant)
    elif command == "fight":
        fight(inhabitant)
    elif command == "steal":
        steal(inhabitant)
    elif command == "hug":
        hug(inhabitant)
    elif command == "unlock":
        unlock()
    elif command == "inventory":
        list_inventory()
    elif command == "quit":
        exit()
    else:
        print(f"I don't understand \"{command}\"")