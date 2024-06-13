from room import Room


kitchen = Room("kitchen")
kitchen.description = "A dank and dirty room buzzing with flies"
ballroom = Room("ballroom")
ballroom.description = "A vast room with a shiny wooden floor"
dining_hall = Room("dining hall")
dining_hall.description = "A large room with ornate golden decorations"

kitchen.two_way_link(dining_hall, "south")
dining_hall.two_way_link(ballroom, "west")

dining_hall.get_details()