import random
from tabulate import tabulate

def initialise_doors():
    doors = ['Goat', 'Goat', '1 million dollars']
    random.shuffle(doors)
    return doors

def play_part1(infomation, part, number_of_rounds, quick_summary):
    doors = initialise_doors()
    round = 1
    switch_wins, stay_wins = 0, 0

    for i in range(number_of_rounds):
        choices, goat_doors, round_infomation, switch_choice_list  = [1, 2 ,3], [], [], ['switch', 'stay']
        round_infomation.append(round)
        if part == 1:
            print(f"\nRound #{round}: Door 1 | Door 2 | Door 3")
        if part == 1:
            user_choice = int(input("\nChoose a door: "))
            if user_choice == 0:
                break
        else:
            user_choice = random.randint(1,3)

        choices.remove(user_choice)
        round_infomation.append(user_choice)

        for i in range(3):
            if doors[i] == 'Goat':
                goat_doors.append(i+1)

        if goat_doors[0] == user_choice:
            if part == 1:
                print(f"Goat is in Door {goat_doors[1]}")   
            choices.remove(goat_doors[1])
        else:
            if part == 1:
                print(f"Goat is in Door {goat_doors[0]}")
            choices.remove(goat_doors[0])

        if part == 1:
            switch_choice = input("\nStay or Switch? ").strip().lower()
        else:
            switch_choice = random.choice(switch_choice_list)

        round_infomation.append(switch_choice)
        if switch_choice == 'switch':
            user_choice = choices[0]

        if doors[user_choice-1] == '1 million dollars':
            if part == 1:
                print(f"You switched to Door {user_choice + 1} ... You WIN!")
            round_infomation.append('Win')
        else:
            if part == 1:
                print(f"You switched to Door {user_choice + 1} ... You lose!")
            round_infomation.append('Lose')

        round += 1
        infomation.append(round_infomation)

    print_summary(infomation, stay_wins, switch_wins, quick_summary, round)

def print_summary(info, stay_wins, switch_wins, quick_summary, rounds):
    for game_round in info[1:]:
        if game_round[2] == "switch" and game_round[3] == "Win":
            switch_wins += 1
        elif game_round[2] == "stay" and game_round[3] == "Win":
            stay_wins += 1
    if quick_summary:
        print(f"{rounds-1}         {(switch_wins/(switch_wins+stay_wins))*100}%      {(stay_wins/(switch_wins+stay_wins))*100}%")
        if rounds-1 == 1000:
            output_file = open('part2_random.txt', 'w')
            table = tabulate(info, tablefmt="fancy_grid", headers="firstrow")
            output_file.write(table)
            output_file.close()
    else:
        print("\n       **Summary**\nResults Table")
        table = tabulate(info, tablefmt="fancy_grid", headers="firstrow")
        print(table)
        print(f"\nWins with switching = {switch_wins}\nWins with staying = {stay_wins}")
        print(f"\n\nPr(Winning with switch) = {(switch_wins/(switch_wins+stay_wins))*100}\nPr(Winning with stay) = {(stay_wins/(switch_wins+stay_wins))*100}\n")

infomation = [["Round","Choice","Action","Outcome"]]

which_part = int(input("\nWhat part do you want to run"))

if which_part == 1:
    play_part1(infomation, 1, 9999999, False)

elif which_part == 2:
    print("Just simulated 50 rounds with random switching.")
    play_part1(infomation, 2, 50, False)
    print("\nThe rest were simulated silently...\n\n\nRounds     Pr(Win with Switch)    Pr(Win with Stay)")
    play_part1(infomation, 2, 50, True)
    play_part1(infomation, 2, 100, True)
    play_part1(infomation, 2, 1000, True)
    play_part1(infomation, 2, 5000, True)
    play_part1(infomation, 2, 10000, True)