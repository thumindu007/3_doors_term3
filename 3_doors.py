import random

def initialise_doors():
    doors = ['Goat', 'Goat', '1 million dollars']
    random.shuffle(doors)
    return doors

def part1(infomation, part):
    doors = initialise_doors()
    print(doors)
    round = 1
    switch_wins, stay_wins = 0, 0
    goat_doors = []

    while True:

        print(f"Round #{round}: Door 1 | Door 2 | Door 3")
        user_choice = int(input("Choose a door: "))
        if user_choice == 0:
            break

        for i in range(3):
            if doors[i] == 'Goat':
                goat_doors.append(i+1)
            else:
                prize_door = i+1
        print(goat_doors)
        print(prize_door)
        if goat_doors[0] == user_choice:
            print(f"Goat is in Door {goat_doors[1]}")
            
        else:
            print(f"Goat is in Door {goat_doors[0]}")
        
        switch_choice = input("Stay or Switch? ").strip().lower()
        if 


def finishing_p1(info, stay_wins, switch_wins):
    print("\n**Summery**")
    column_widths = [max(len(str(item)) for item in col) for col in info]

    # Determine the number of rows in the table
    num_rows = len(info)  # Use len(info) to get the number of rows

    # Print the table vertically
    for i in range(num_rows):
        formatted_row = [str(row[i]).ljust(column_widths[i]) for row in info]
        print(" | ".join(formatted_row))

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


infomation = [["Round"],["Choice"],["Action"],["Outcome"]]


which_part = int(input("What part do you want to run"))

if which_part == 1: part1(infomation, 1)