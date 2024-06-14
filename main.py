from room import Room
from item import Item

kitchen = Room("kitchen")
kitchen.description = "A dank and dirty room buzzing with flies"
ballroom = Room("ballroom")
ballroom.description = "A vast room with a shiny wooden floor"
dining_hall = Room("dining hall")
dining_hall.description = "A large room with ornate golden decorations"

kitchen.two_way_link(dining_hall, "south")
dining_hall.two_way_link(ballroom, "west")

key = Item("key")
key.description = "A shiny key"
key.describe()

current_room = kitchen
while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)