

def display_start_screen():
    user_input = input("To get started, please select one of the following options\n(type and enter the corresponding number): \n 1. Start \n 2. Rules \n 3. Options \n 4. Credits")
    if user_input == 4:
        display_credits()
    elif user_input == 3:
        open_options()
    elif user_input == 2:
        display_rules()
    elif user_input == 1:
        player_selection()

def player_selection():
    pass

def display_rules():
    with open("rules.txt") as page:
        for line in page:
            print(line)
    # print("full list of rules for the game")
    if input("type RETURN to exit.") == "RETURN":
        display_start_screen()
    else:
        pass

def open_options():
    pass

def display_credits():
    with open("credits.txt") as page:
        for line in page:
            print(line)
    # print("full list of credits from both this game and the original buckshot roulette")
    if input("type RETURN to exit.") == "RETURN":
        display_start_screen()
    else:
        pass

def main():
    print("\nWelcome to Buckshot Roulette!")
    display_start_screen()

if __name__ == "__main__":
    main()