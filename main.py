from room import Room
from item import Item
from character import Enemy

kitchen = Room("kitchen")
kitchen.description = "A dank and dirty room buzzing with flies"
ballroom = Room("ballroom")
ballroom.description = "A vast room with a shiny wooden floor"
dining_hall = Room("dining hall")
dining_hall.description = "A large room with ornate golden decorations"

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.conversation = "Brrlgrh... rgrhl... brains..."
dave.weakness = "cheese"

dining_hall.character = dave

current_room = kitchen
while True:
    print()
    current_room.get_details()

    inhabitant = current_room.character
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")
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
            inhabitant.fight(combat_item)
        else:
            print("There's nobody here")
    else:
        print(f"I don't understand \"{command}\"")