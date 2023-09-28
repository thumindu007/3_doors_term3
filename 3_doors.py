import random
from tabulate import tabulate

def initialise_doors():
    doors = ['Goat', 'Goat', '1 million dollars']
    random.shuffle(doors)
    return doors

def play_part1(infomation, part):
    doors = initialise_doors()
    round = 1
    switch_wins, stay_wins = 0, 0
    
    while True:
        choices = [1, 2 ,3]
        goat_doors = []
        round_infomation = []
        round_infomation.append(round)

        print(f"\nRound #{round}: Door 1 | Door 2 | Door 3")
        user_choice = int(input("\nChoose a door: "))
        if user_choice == 0:
            break
        choices.remove(user_choice)
        round_infomation.append(user_choice)

        for i in range(3):
            if doors[i] == 'Goat':
                goat_doors.append(i+1)

        if goat_doors[0] == user_choice:
            print(f"Goat is in Door {goat_doors[1]}")   
            choices.remove(goat_doors[1])
        else:
            print(f"Goat is in Door {goat_doors[0]}")
            choices.remove(goat_doors[0])
        
        switch_choice = input("\nStay or Switch? ").strip().lower()
        round_infomation.append(switch_choice)
        if switch_choice == 'switch':
            user_choice = choices[0]
        
        if doors[user_choice-1] == '1 million dollars':
            print(f"You switched to Door {user_choice + 1} ... You WIN!")
            round_infomation.append('Win')
        else:
            print(f"You switched to Door {user_choice + 1} ... You lose!")
            round_infomation.append('Lose')

        round += 1
        infomation.append(round_infomation)

    print_summary(infomation, stay_wins, switch_wins)

def print_summary(info, stay_wins, switch_wins):
    print("\n       **Summary**\nResults Table")
    table = tabulate(info, tablefmt="fancy_grid", headers="firstrow")
    print(table)
    for game_round in info[1:]:
        if game_round[2] == "switch" and game_round[3] == "Win":
            switch_wins += 1
        elif game_round[2] == "stay" and game_round[3] == "Win":
            stay_wins += 1
    print(f"\nWins with switching = {switch_wins}\nWins with staying = {stay_wins}")
    print(f"\n\nPr(Winning with switch) = {(switch_wins/(switch_wins+stay_wins))*100}\nPr(Winning with stay) = {(stay_wins/(switch_wins+stay_wins))*100}")

infomation = [["Round","Choice","Action","Outcome"]]

which_part = int(input("\nWhat part do you want to run"))

if which_part == 1: play_part1(infomation, 1)