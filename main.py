from room import Room
from item import Item

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

key = Item("key")
key.description = "A shiny key"
key.describe()

current_room = kitchen
while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)