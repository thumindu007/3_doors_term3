import random
from tabulate import tabulate

def initialise_doors(part):
    doors = ['Goat', 'Goat', '1 million dollars']
    if part == 5:
        doors = ['Goat', 'Goat', 'Goat', 'Goat', 'Goat', 'Goat', 'Goat', 'Goat', 'Goat', '1 million dollars']
    random.shuffle(doors)
    return doors

def game_loop(infomation, part, number_of_rounds):
    round, switch_wins, stay_wins, game_mode = 1, 0, 0, ['User switch','Random switch','Always stay','Always switch','Always switch with 10 doors']
    print('Running game for mode ', game_mode[0], ' with ', number_of_rounds, ' rounds')
    for _ in range(number_of_rounds):
        doors, choices, goat_doors, round_infomation, switch_choice_list  = initialise_doors(part), [1, 2 ,3], [], [], ['switch', 'stay']
        if part == 5:
            choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        round_infomation.append(round)
#       **Play starts from here**
        if part == 1:
            print(f"\nRound #{round}: Door 1 | Door 2 | Door 3")
            while True:
                user_choice = input("\nChoose a door: ")
                if user_choice in ['0', '1', '2', '3']:
                    break
            user_choice = int(user_choice)
            if user_choice == 0:
                break
        else:
            user_choice = random.randint(1,3)
            if part == 5:
                user_choice = random.randint(1,10)
        choices.remove(user_choice)
        round_infomation.append(user_choice)

        counter = 1
        for i in doors:
            if i == 'Goat':
                goat_doors.append(counter)
            counter += 1
        # else:
        #     for i in doors:
        #         if i == 'Goat':
        #             goat_doors.append(counter)
        #         counter += 1
        if part == 5:
            choices = []
            for i in range(1, 11):
                if i != user_choice and i not in goat_doors:
                    choices.append(i)
        else:
            if goat_doors[0] == user_choice:
                if part == 1:   print(f"Goat is in Door {goat_doors[1]}")
                choices.remove(goat_doors[1])
            else:
                if part == 1:   print(f"Goat is in Door {goat_doors[0]}")
                choices.remove(goat_doors[0])

        if part == 1:
            while True:
                switch_choice = input("\nstay or switch? ")
                if switch_choice == 'stay' or switch_choice == 'switch':
                    break
        elif part == 3:   switch_choice = 'stay'
        elif part == 4 or part == 5:   switch_choice = 'switch'
        else:   switch_choice = random.choice(switch_choice_list)
        round_infomation.append(switch_choice)

        if doors[user_choice-1] == '1 million dollars' and part == 5:   round_infomation.append('Lose')
        else:
            if switch_choice == 'switch':   user_choice = choices[0]   
            if doors[user_choice-1] == '1 million dollars':
                if part == 1:   print(f"You switched to Door {user_choice + 1} ... You WIN!")
                round_infomation.append('Win')
            else:
                if part == 1:   print(f"You switched to Door {user_choice + 1} ... You lose!")
                round_infomation.append('Lose')
        round += 1
        infomation.append(round_infomation)
    return stay_wins, switch_wins


# Winning percentage is calculated by amount of times won by switching or staying / total number of rounds
def print_summary(info, stay_wins, switch_wins, quick_summary, rounds, part):
    for game_round in info[1:]:
        if game_round[2] == "switch" and game_round[3] == "Win":   switch_wins += 1
        elif game_round[2] == "stay" and game_round[3] == "Win":   stay_wins += 1

    if quick_summary:
        quick_sum_list = [["Rounds", "Pr(Win with Switch)", "Pr(Win with Stay)"],[rounds, (f"{(switch_wins/(rounds))*100}%"), (f'{(stay_wins/(rounds))*100}%')]]
        quick_summary_print = tabulate(quick_sum_list, tablefmt="fancy_grid", headers="firstrow")
        print(quick_summary_print)
        if rounds == 1000:
            if part == 2:    output_file = open('part2_random.txt', 'w')
            elif part == 3:  output_file = open('part3_stay.txt', 'w')
            elif part == 4:  output_file = open('part4_switch.txt', 'w')
            elif part == 5:  output_file = open('part5_ten_doors.txt', 'w')
            table = tabulate(info, tablefmt="fancy_grid", headers="firstrow")
            output_file.write(table)
            output_file.close()
    else:
        print("\n       **Summary**\nResults Table")
        print(tabulate(info, tablefmt="fancy_grid", headers="firstrow"))
        print(f"\nWins with switching = {switch_wins}\nWins with staying = {stay_wins}")
        print(f"\n\nPr(Winning with switch) = {(switch_wins/(rounds))*100}\nPr(Winning with stay) = {(stay_wins/(rounds))*100}\n")

infomation, part2_rounds = [["Round","Choice","Action","Outcome"]], [50, 100, 1000, 5000, 10000]
which_part = int(input("\nWhat mode do you want to run the game (1-5) "))

stay_wins, switch_wins, rounds, print_quick_summary, = 0, 0, 1000, True
if which_part == 1:
    rounds = 9999999
    wins = game_loop(infomation, 1, rounds)
    print_quick_summary = False

elif which_part == 2:
    print("Simulating 50 rounds with random switching.")
    rounds = 50
    game_loop(infomation, 2, rounds)
    print_summary(infomation, stay_wins, switch_wins, print_quick_summary, rounds, which_part)
    print("\nSimulating silently...\n\n")
    for i in part2_rounds:
        game_loop(infomation, 2, i)

elif which_part == 3:
    wins = game_loop(infomation, 3, rounds)

elif which_part == 4:
    wins = game_loop(infomation, 4, rounds)

elif which_part == 5:
    wins = game_loop(infomation, 5, rounds)

if which_part !=2:
    stay_wins, switch_wins = wins[0], wins[1]
    print_summary(infomation, stay_wins, switch_wins, print_quick_summary, rounds, which_part)
