from room import Room
from item import Item
from character import Enemy, Friend

player_items = []

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
dave.weakness = "cheese"
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
            combat_item = input("> ")
            combat_result, dropped_item = inhabitant.fight(combat_item)
            if combat_result:
                if isinstance(inhabitant, Enemy):
                    current_room.character = None
                    if dropped_item:
                        player_items.append(dropped_item)
            else:
                print()
                print("~~~ You lose! ~~~")
                print()
                exit()
        else:
            print("There's nobody here")
    elif command == "steal":
        if inhabitant:
            stolen_item = inhabitant.steal()
            if stolen_item:
                player_items.append(stolen_item)
        else:
            print("There's nobody here")
    elif command == "hug":
        if inhabitant and isinstance(inhabitant, Friend):
            inhabitant.hug()
        else:
            print("There's nobody here that you want to hug")
    elif command in ("quit", "exit"):
        exit()
    else:
        print(f"I don't understand \"{command}\"")