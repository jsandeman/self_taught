#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 08 17:59:04 2019

@author: jsandeman

Simple adventure game which prompts user to choose which room in a house
to move to. The user is told where there are, given a brief description,
and then given options for which room to choose next. Each room is
implemented as a class and contains a list of adjacent rooms which comprise
the user's options about where to move next. The rooms are then organized
into a list contained in the House class, which also tracks in which room
the user currenty is, ans also handles initiation of the rooms and to which
rooms they are connected.
"""


class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.adjacent_rooms = []

    def set_adjacent_rooms(self, adj_rms):
        self.adjacent_rooms = adj_rms

    def get_adjacent_rooms(self):
        return self.adjacent_rooms

    def __repr__(self):
        return self.description

    def __str__(self):
        return self.name


class House:

    def __init__(self):
        self.room_list = []

        attic = Room("Attic", "The dusty old attic, with many things covered in old, yellow sheets.")
        upstairs_hallway = Room("Upstairs Hallway", "A dimly lit hallway with peeling wallpaper.")
        master_bedroom = Room("Master Bedroom", "There is a stained carpet and posted bed covered in "
                                                "spider webs.")
        guest_bedroom = Room("Guest Bedroom", "You see a broken wing back chair.")
        living_room = Room("Living Room", "This large room contains a sofa, wooden chairs, and a fireplace.")
        dining_room = Room("Dining Room", "There is a long, oak table and elegant high-back chairs.")
        basement = Room("Basement", "The basement is piled with old decayed books, jars full of embalmed animals, "
                                    "and a damp, moldy smell.")

        # Set the connections between the rooms
        attic.set_adjacent_rooms([upstairs_hallway])
        upstairs_hallway.set_adjacent_rooms([master_bedroom, guest_bedroom, living_room, attic])
        master_bedroom.set_adjacent_rooms([upstairs_hallway])
        guest_bedroom.set_adjacent_rooms([upstairs_hallway])
        living_room.set_adjacent_rooms([upstairs_hallway, dining_room])
        dining_room.set_adjacent_rooms([living_room, basement])
        basement.set_adjacent_rooms([dining_room])

        # Add the rooms to the room list and set the current room to the
        # living room
        self.room_list.append(attic)
        self.room_list.append(upstairs_hallway)
        self.room_list.append(master_bedroom)
        self.room_list.append(guest_bedroom)
        self.room_list.append(living_room)
        self.room_list.append(dining_room)
        self.room_list.append(basement)
        self.current_room = living_room

    def __repr__(self):
        return "The ancient warlock's secret house"

    def __str__(self):
        return "The ancient warlock's secret house"


warlock_house = House()
print("Welcome to the Warlock's secret house!")

while True:
    curr_room = warlock_house.current_room
    print("\nYou are currently in the " + curr_room.name)
    print(curr_room.description + "\n")
    adj_rooms = curr_room.adjacent_rooms
    print("Where to next ('q' to quit):")
    for i, room in enumerate(adj_rooms):
        print(str(i + 1) + " - " + room.name)
    choice = input("--> ")
    if choice.lower() == 'q' or choice.lower() == "quit":
        break
    try:
        choice_num = int(choice) - 1
        new_room = adj_rooms[choice_num]
        warlock_house.current_room = new_room
    except ValueError:
        print("Pick a number from the list above!!\n")
    except IndexError:
        print("Stick to the listed options!\n")

print("Goodbye, come back soon!")
