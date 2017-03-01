

class Player:

    def __init__(self, name, lose_bool=False):
        self.name = name
        self.moves_list = []
        self.lose_bool = lose_bool

    def __str__(self):
        return "Player 1: {}".format(self.name)

    def __eq__(self, other):
        return self.name == other.name and self.moves == other.moves

    def get_move(self):
        move = 0
        move = int(input("\nHow many sticks do you want to pick up, {}? (1-3)".format(self.name)))
        while move < 1 or move > 3:
            print("That wasn't a valid choice, {}".format(self.name))
            move = int(input("\nHow many sticks do you want to pick up, {}? (1-3)".format(self.name)))
        self.moves_list.append(move)
        return move
