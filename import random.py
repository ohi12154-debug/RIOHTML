import random
attemts_list = []
def show_score():
if len(attempts_list) <= 0:

    print("there is currently no high score, it is yours for the taking!")
else:
    print("the current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("hey there! welcome to the game of gusses!")
    player_name = input("enter your name")
    wanna_play = input("hi {} would you like to play the gussing game? (enter yes/no)".formate(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guss = input("pick a number betwen 1 and 10")
            if int(guss) < 1 or int(guss) >10:
                raise valueError("please guess a number withen the given range")
            if int(guess) == random_number:
                print("congrats you gussed it right!")
                attempts += 1
            attempts_list.append(attempts)
            print("it took you {} attemps".fomat(attempts))
            play_again = input("would you like to play this again? (enter yes/no)")
            attemts = 0
            show_score()
            random_number = int(random.randint(1, 10))
            if play_again.lower() == "no"
            print("have a nice day!")
            break
    elif int(guess) < random_nuber:
print("it is lower")
attempts += 1
elif int(guess) > random_number:
print(it is higher)
attempts += 1
except valueError ar err:
print("oh, that is not a valid value. try again...")
print("({})".format(err))
else:
print("that is cool, have a nice day!")
if _name_ == '_main_':
    start_game()