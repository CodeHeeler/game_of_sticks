from player import *
from game import *
#import system.io

def user_turn(name, sticks):
    print("\nSticks remaining: {}".format(sticks))
    move = name.get_move()
    sticks -= move
    if sticks == 0:
        name.lose_bool == True
    return sticks


def main():
    #system.io.clear()
    print("Welcome to the game of sticks!\n\n")
    player1_name = input("What is Player 1's name? ")
    player2_name = input("What is Player 2's name? ")
    stick_total = 0
    remaining_sticks = 0

    # input loop
    while stick_total < 10 or stick_total > 100:
        stick_total = int(input("How many sticks are on the table initially (10-100)? "))

    # this_game = Game(player1_name, player2_name, stick_total)
    remaining_sticks = stick_total
    player1 = Player(player1_name)
    player2 = Player(player2_name)

    # game loop
    while remaining_sticks > 0:
        remaining_sticks = user_turn(player1, remaining_sticks)
        if player1.lose_bool:
            break
        remaining_sticks = user_turn(player2, remaining_sticks)


    if player1.lose_bool:
        print("\n\nGame Over!  Congrats, {}, you win! Better luck next time, {}.\n".format(player2.name, player1.name))
    else:
        print("\n\nGame Over!  Congrats, {}, you win! Better luck next time, {}.\n".format(player1.name, player2.name))


main()
