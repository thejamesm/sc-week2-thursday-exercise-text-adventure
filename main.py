from room import Room
from item import Item
from inventory import Inventory
from character import Enemy, Friend

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

    if command in ("north", "east", "south", "west"):
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant:
            inhabitant.talk()
        else:
            print("There's nobody here")
    elif command == "fight":
        if inhabitant:
            print("What will you fight with?")
            combat_item = inventory.choose_item()
            if combat_item:
                combat_result, dropped_item = inhabitant.fight(combat_item)
                if combat_result:
                    if isinstance(inhabitant, Enemy):
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
    elif command == "steal":
        if inhabitant:
            stolen_item = inhabitant.steal()
            if stolen_item:
                inventory.add_item(stolen_item)
        else:
            print("There's nobody here")
    elif command == "hug":
        if inhabitant and isinstance(inhabitant, Friend):
            inhabitant.hug()
        else:
            print("There's nobody here that you want to hug")
    elif command == "unlock":
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
    elif command in ("inventory", "items", "pockets", "bag"):
        inventory.list_inventory()
    elif command in ("quit", "exit"):
        exit()
    else:
        print(f"I don't understand \"{command}\"")