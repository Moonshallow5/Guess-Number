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
        print(i)
        print("Go higher")
        return True


def pick_less(player_input):
    if player_input > computer :
        print(i)
        print("Go lower")
        return True


def pick_equal(player_input):
    if player_input == computer:
        return True


score_computer = 0
score_human = 0
tries = 0


def pick_tries():
    number()
    global i
    i = 0
    global tries
    global score_computer
    global score_human

    while i < z:
        print(computer)
        player_input = int(input("Enter: "))
        if input_more(player_input):
            tries += 1
            i += 1
        if pick_less(player_input):
            tries += 1
            i += 1
        if pick_equal(player_input):
            print("Well done")
            tries += 1
            print("Your number of tries is " + str(tries))
            score_human += 1
            print("Score of computer is " + str(score_computer) + " and score of human is " + str(score_human))
            break
    if i >= z:
        print("You have exceeded the number of guesses which is " + str(z))
        score_computer += 1
        print("Score of computer is " + str(score_computer) + " and score of human is " + str(score_human))
    play = input("Would u play again? Type Y to play again ")
    if play == "Y":
        start()
    else:
        print("Good game")


def pick_loop():
    number()
    i = 0
    global tries
    tries = 0
    while i == 0:
        print(computer)
        player_input = int(input("Enter: "))
        if player_input == -1:
            break
        if input_more(player_input):
            tries += 1
        if pick_less(player_input):
            tries += 1
        if pick_equal(player_input):
            print("Well done")
            tries += 1
            print("Your number of tries is : " + str(tries))
            break
    play = input("Would u play again? Type Y to play again ")
    if play == "Y":
        start()
    else:
        print("Good game")


def start():
    global x
    write()
    x = input("Enter Y or N ")
    if x == "Y":
        global z
        z = int(input("How many tries would you want: "))
        pick_tries()
    else:
        pick_loop()


start()
