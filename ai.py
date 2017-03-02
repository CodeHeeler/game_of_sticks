from game import *
from random import choice

class AI:

    def __init__(self, game):
        self.temp_moves_list = []
        self.lose_bool = False
        # self.all_poss_moves_dict = enumerate([[1,2,3]] * game.stick_num, 1)
        self.all_poss_moves_dict = {x+1: [1,2,3] for x in range(game.stick_num)}


    def __str__(self):
        return "AI"

    def __eq__(self, other):
        return self.name == other.name and self.moves == other.moves

    def get_move(self, game):
        if game.stick_num > len(self.all_poss_moves_dict):
            for x in range(len(self.all_poss_moves_dict), game.stick_num + 4):
                self.all_poss_moves_dict[x]= [1,2,3]
        move = choice(self.all_poss_moves_dict[game.stick_num])
        self.temp_moves_list.append((game.stick_num,move))
        print("The computer picked up {} sticks.".format(move))
        print("temp_moves_list: {}".format(self.temp_moves_list))
        return move

    def save_moves(self):
        for chunk in self.temp_moves_list:
            self.all_poss_moves_dict[chunk[0]].append(chunk[1])
            self.temp_moves_list = []


        """dumb AI strategy"""

        # if game.stick_num < 3:
        #     move = choice([1,2])
        #     self.temp_moves_list.append(move)
        #     print("The computer picked up {} sticks.".format(move))
        #     return move
        # else:
        #     move = 3
        #     self.temp_moves_list.append(move)
        #     print("The computer picked up {} sticks.".format(move))
        #     return move
