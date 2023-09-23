import random

class Door:
    def __init__(self, number, item):
        self.number = number
        self.item = item

def create_doors(choices_list, choices_doors, infomation):
    chosen_door_number = int(input("\nChoose a door: "))
    if chosen_door_number == 0:
        print("exiting...\n")
        return True
    else:
        infomation[1].append(chosen_door_number)
        choices_doors.remove(chosen_door_number)
        global chosen_door, not_chosen1, not_chosen2
        chosen_door = Door(chosen_door_number, choices_list[random.randint(0,2)])
        choices_list.remove(chosen_door.item)

        not_chosen1 = Door(choices_doors[random.randint(0,1)], choices_list[random.randint(0,1)])
        choices_list.remove(not_chosen1.item)
        choices_doors.remove(not_chosen1.number)
        not_chosen2 = Door(choices_doors[0], choices_list[0])
        return False

def part1(infomation):
    choices_list = ['Goat', 'Goat', "1 million dollars"]
    choices_doors = [1, 2, 3]
    
    tf = create_doors(choices_list, choices_doors, infomation)
    if tf is True:
        return True
    else:
        infomation[0].append(len(infomation[0]))
        if not_chosen1.item == 'Goat':
            print("\nThe goat is in door",not_chosen1.number)
            switch = not_chosen2

        else:
            print("\nThe goat is in door",not_chosen2.number)
            switch = not_chosen1

        decision = input("\nStay or Switch? ")
        infomation[2].append(decision)
        if decision.lower() == 'switch':
            if switch.item == 'Goat':
                print("You switched to",switch.number,"You lose!")
                infomation[3].append("Lose")
            else:
                print("You switched to",switch.number,"You WIN!")
                infomation[3].append("Win")
        else:
            if chosen_door.item == 'Goat':
                print("You switched to",chosen_door.number,"You lose!")
                infomation[3].append("Lose")
            else:
                print("You switched to",chosen_door.number,"You WIN!")
                infomation[3].append("Win")
        return False


def finishing_p1(info, stay_wins, switch_wins):
    print("\n**Summery**")
    column_widths = [max(len(str(item)) for item in col) for col in zip(*info)]
    for row in info:
        formatted_row = [str(item).ljust(width) for item, width in zip(row, column_widths)]
        print("    ".join(formatted_row))

    info[3].remove('Outcome')
    info[2].remove('Action')
    switch_wins = win_count(info, 'switch', switch_wins)
    stay_wins = win_count(info, 'stay', stay_wins)
    winpercentage(info, switch_wins)
    winpercentage(info, stay_wins)

def win_count(info, choice, count):
    for i in range(len(info[2])):
        if info[2][i] == choice and info[3][i] == 'Win':
            count += 1
    print("\nWins with",choice,":",count)
    return count

def winpercentage(info, wins):
    print("\nPr(Winning with switch) =",(wins/len(info[3])*100))

global exit
exit = False
infomation = [["Round"],["Choice"],["Action"],["Outcome"]]
switch_wins = 0
stay_wins = 0

while exit is False:
    exit = part1(infomation)

finishing_p1(infomation, stay_wins, switch_wins)
