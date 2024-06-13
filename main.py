from room import Room
from player import Player

kitchen = Room("kitchen")
kitchen.description = "A dank and dirty room buzzing with flies"
ballroom = Room("ballroom")
ballroom.description = "A vast room with a shiny wooden floor"
dining_hall = Room("dining hall")
dining_hall.description = "A large room with ornate golden decorations"

kitchen.two_way_link(dining_hall, "south")
dining_hall.two_way_link(ballroom, "west")

player_name = input("Enter player name: ")
player = Player(player_name, kitchen)

while True:
    player.describe()
    player.location.get_details()
    direction = input("Which direction do you want to move? ").lower()
    try:
        player.move(direction)
    except ValueError:
        print("!!Invalid direction!!")