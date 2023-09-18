import random

class Door:
    def __init__(self, number, item):
        self.number = number
        self.item = item

choices_list = ['Goat', 'Goat', "1 million dollars"]
choices_doors = ['1', '2', '3']


chosen_door = int(input("Choose a door: "))
choices_doors.remove(chosen_door)
chosen_door = Door(chosen_door, choices_list[random.randint(0,2)])
print(chosen_door.item)
choices_list.remove(chosen_door.item)

print(choices_list)
not_chosen1 = Door(choices_doors[random.randint(0,1)], choices_list[random.randint(0,1)])
print(not_chosen1.number)
choices_list.remove(not_chosen1.number)
choices_list.remove(not_chosen1.item)
not_chosen2 = Door(choices_doors[0], choices_list[0])

if not_chosen1.item == 'Goat':
    print("The goat is in door",not_chosen1.number)
else:
    print("The goat is in door",not_chosen2.number)