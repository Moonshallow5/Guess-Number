import random


def write():
    print("--------------------------------------------------------------------------")
    print("Do you want to choose how many tries you get? ")
    print("Enter Y to choose the number of tries and N to guess with infinite tries")
    print("Please enter -1 if you want to concede")
    print("--------------------------------------------------------------------------")



def number():
    global computer
    computer = random.randrange(0, 100)



def input_more(player_input):
    if player_input < computer:
        print("Go higher")
        return True


def pick_less(player_input):
    if player_input > computer:
        print("Go lower")
        return True


def pick_equal(player_input):
    if player_input == computer:
        return True


def pick_loop(tries=0):
    write()
    number()
    i = 0
    while i == 0:
        print(computer)
        player_input = int(input("Enter: "))
        if input_more(player_input):
            tries += 1
        if pick_less(player_input):
            tries += 1
        if pick_equal(player_input):
            print("Well done")
            tries += 1
            print("Ties: " + str(tries))
            break
    play = input("Would u play again? Type Y to play again ")
    if play == "Y":
        pick_loop()
    else:
        print("Good game")


pick_loop()
