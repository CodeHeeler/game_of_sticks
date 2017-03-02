from player import *
from game import *
from ai import AI
#import system.io

def user_turn(name, game):
    print("\nSticks remaining: {}".format(game.stick_num))
    move = name.get_move(game)
    game.stick_num -= move
    if game.stick_num <= 0:
        name.lose_bool = True


def main():
    #system.io.clear()
    print("Welcome to the game of sticks!\n\n")
    while True:
        choice = int(input("How many players? (1 or 2) "))
        if choice == 1:
            player1_name = input("What is Player 1's name? ")
            break
        elif choice == 2:
            player1_name = input("What is Player 1's name? ")
            player2_name = input("What is Player 2's name? ")
            break
        else:
            print("That was not a correct choice. Try again")

    # input loop
    if choice == 2:
        while  True:
            stick_total = int(input("How many sticks are on the table initially (10-100)? "))
            if stick_total >= 10 and stick_total <= 100:
                break
        this_game = Game(stick_total, player1_name, player2_name)
        player1 = Player(player1_name)
        player2 = Player(player2_name)

        # game loop
        while this_game.stick_num > 0:
            user_turn(player1, this_game)
            if player1.lose_bool:
                break
            user_turn(player2, this_game)


        if player1.lose_bool:
            print("\n\nGame Over!  Congrats, {}, you win! Better luck next time, {}.\n".format(player2.name, player1.name))
        else:
            print("\n\nGame Over!  Congrats, {}, you win! Better luck next time, {}.\n".format(player1.name, player2.name))
    else:
        while  True:
            stick_total = int(input("How many sticks are on the table initially (10-100)? "))
            if stick_total >= 10 and stick_total <= 100:
                break
        this_game = Game(stick_total, player1_name)
        ai = AI(this_game)
        player1 = Player(player1_name)

        while(True):
            #game_loop
            # game loop
            while this_game.stick_num > 0:
                user_turn(player1, this_game)
                if this_game.stick_num == 0:
                    break
                user_turn(ai, this_game)

            if player1.lose_bool:
                print("\n\nGame Over!  The computer won! Better luck next time, {}.\n".format(player1.name))
                ai.save_moves()
                play_again = input("Do you want to play again? [Y/n] ")
                if play_again == 'Y':
                    player1.lose_bool = False
                    ai.lose_bool = False
                    while this_game.stick_num < 10 or this_game.stick_num > 100:
                        this_game.stick_num = int(input("How many sticks are on the table initially (10-100)? "))
                        if stick_total >= 10 and stick_total <= 100:
                            break
                else:
                    break
            else:
                print("\n\nGame Over!  Congrats, {}, you beat the computer!\n".format(player1.name))
                play_again = input("Do you want to play again? [Y/n] ")
                if play_again == 'Y':
                    player1.lose_bool = False
                    ai.lose_bool = False
                    while this_game.stick_num < 10 or this_game.stick_num > 100:
                        this_game.stick_num = int(input("How many sticks are on the table initially (10-100)? "))
                        if stick_total >= 10 and stick_total <= 100:
                            break
                else:
                    break
            print("\n\nDid we learn anything: {}".format(ai.all_poss_moves_dict))


main()
