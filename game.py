class Game:
    def __init__(self, stick_total, player1, player2="none"):
        self.player1 = player1
        self.player2 = player2
        self.stick_total = stick_total
        self.stick_num = stick_total

    def __str__(self):
        return "This game is between {} and {} with {} sticks. ".format(self.player1, self.player2, self.stick_num)


    def __eq__(self, other):
        return (self.player1 == other.player1 and
               self.player2 == other.player2 and
               self.stick_num == other.stick_num)
