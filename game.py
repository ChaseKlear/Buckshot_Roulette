import random

ITEMS = ["Magnifying_Glass", "Beer_Can", "Hacksaw", "Cigarettes"]

SHOTGUN = []
SHOTGUN_DAMAGE = 1

TURN = "Player_1"
    
# class Player_1:
#     def __init__(self, name, health, inventory, opponent):
#         self.name = "Player_1"
#         self.health = 6
#         self.inventory = {"Magnifying_Glass":0, "Beer_Can":0, "Hacksaw":0, "Cigarettes":0}
#         self.opponent = "Player_2"

# class Player_2:
#     def __init__(self, name, health, inventory, opponent):
#         self.name = "Player_2"
#         self.health = 6
#         self.inventory = {"Magnifying_Glass":0, "Beer_Can":0, "Hacksaw":0, "Cigarettes":0}
#         self.opponent = "Player_1"

class Player:
    __slots__ = ["__name", "__health", "__inventory", "__opponent"]
    
    def __init__(self, name, health, inventory, opponent):
        self.__name = name
        self.__health = health
        self.__inventory = inventory
        self.__opponent = opponent
    
    def get_name(self, player):
        return player.__name
    def get_health(self, player):
        return player.__health
    def get_inventory(self, player):
        return player.__inventory
    def get_opponent(self, player):
        return player.__opponent

Player_1 = Player(input("Please enter your name: "), 6, {"Magnifying_Glass":0, "Beer_Can":0, "Hacksaw":0, "Cigarettes":0}, "Player_2")

Player_2 = Player(input("Please enter your name: "), 6, {"Magnifying_Glass":0, "Beer_Can":0, "Hacksaw":0, "Cigarettes":0}, "Player_1")

def intro():
    print("\n", "Welcome to Buckshot Roulette!", "\n")
    Player.get_name(Player_1) = input("Player 1 please enter your name: ")
    Player_2.name = input("Player 2 please enter your name: ")

def Magnifying_Glass():
    print("The round currently in the chamber is", SHOTGUN[-1])

def Beer_Can():
    print("Ejecting a", SHOTGUN.pop(), "round.")

def Hacksaw():
    SHOTGUN_DAMAGE = 2
    print("Shotgun damage doubled.")

def Cigarettes():
    if TURN.health < 6:
        TURN.health += 1
    print(TURN.name, "'s health is now ", TURN.health, sep = "")

def shoot(target):
    temp = SHOTGUN.pop()
    if temp == "live":
        target.health =- SHOTGUN_DAMAGE
        print('''"BANG!"''')
        print(target.name, "now has", target.health, "left.")
    elif temp == "blank":
        print('''"click"''')
        print("The round was blank.")
    SHOTGUN_DAMAGE = 1
    if target.health <= 0:
        end_game(target.opponent)

def end_game(winner):
    print(winner.name, "Wins!")
    exit()

def play_round():
    distribute_items(TURN)
    load_shotgun()
    TURN = TURN.opponent

def distribute_items(player):
    for _ in range(3):
        if check_total_items(player) < 8:
            player.inventory[ITEMS[random.randint(0,3)]]

def check_total_items(player):
    total = 0
    for x in range(4):
        total += player.inventory[ITEMS[x]]
    return total

def load_shotgun():
    num_of_live_rounds = random.randint(1,4)
    num_of_blank_rounds = random.randint(1,4)
    total_rounds = num_of_live_rounds + num_of_blank_rounds
    print("Loading", num_of_live_rounds, "live rounds and ", num_of_blank_rounds, "blank rounds.")
    SHOTGUN = ["live" for _ in range(total_rounds)]# if random.randint(0,1) == 0 else "live"]

def use_item(player, item):
    if player.inventory[item] > 0:
        player.inventory[item] -= 1
        item()
    else:
        print("No" + item + "in inventory.")

def main():
    intro()
    while True:
        play_round(TURN)

main()