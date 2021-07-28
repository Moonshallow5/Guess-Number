import random

def write():
    print("--------------------------------------------------------------------------")
    print("Do you want to choose how many tries you get? ")
    print("Enter Y to choose the number of tries and N to guess with infinite tries")
    print("Please enter -1 if you want to concede")
    print("--------------------------------------------------------------------------")


write()


def number():
    computer_number = random.randrange(0, 100)
    return computer_number


computer = number()


def input_more(player_input):
    if player_input < computer:
        print("Go higher")


def pick_less(player_input):
    if player_input > computer:
        print("Go lower")


def pick_equal(player_input):
    if player_input == computer:
        return True


def pick_loop():
    i = 0
    print(computer)
    while i == 0:
        player_input = int(input("Enter: "))
        print(player_input)
        input_more(player_input)
        pick_less(player_input)
        if pick_equal(player_input):
            print("Well done")
            break


pick_loop()
