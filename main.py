from game import Game
from room import Room
from item import Item
from character import Enemy, Friend

kitchen = Room("kitchen", "A dank and dirty room buzzing with flies")
ballroom = Room("ballroom", "A vast room with a shiny wooden floor")
dining_hall = Room("dining hall",
                   "A large room with ornate golden decorations")
garden = Room("garden", "You made it to the garden. You win!")

kitchen.two_way_link(dining_hall, "south")
dining_hall.two_way_link(ballroom, "west")
dining_hall.two_way_link(garden, "east")

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

game = Game(start_room=kitchen)