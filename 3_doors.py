import random

class Door:
    def __init__(self, number, item):
        self.number = number
        self.item = item

def create_doors(choices_list, choices_doors):
    chosen_door_number = int(input("\nChoose a door: "))
    choices_doors.remove(chosen_door_number)
    global chosen_door, not_chosen1, not_chosen2
    chosen_door = Door(chosen_door_number, choices_list[random.randint(0,2)])
    choices_list.remove(chosen_door.item)

    not_chosen1 = Door(choices_doors[random.randint(0,1)], choices_list[random.randint(0,1)])
    choices_list.remove(not_chosen1.item)
    choices_doors.remove(not_chosen1.number)
    not_chosen2 = Door(choices_doors[0], choices_list[0])


choices_list = ['Goat', 'Goat', "1 million dollars"]
choices_doors = [1, 2, 3]

create_doors(choices_list, choices_doors)

if not_chosen1.item == 'Goat':
    print("\nThe goat is in door",not_chosen1.number)
    switch = not_chosen2
    
else:
    print("\nThe goat is in door",not_chosen2.number)
    switch = not_chosen1

decision = input("Stay or Switch? ")

if decision.lower == 'switch':
    chosen_door = switch