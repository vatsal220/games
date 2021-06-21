import random

class RockPaperScissors():
    def __init__(self, game_option, rounds):
        self.game_option = game_option
        self.max_rounds = rounds
        self.max_wins = self.max_rounds // 2 + 1
        self.moves = ["rock", "paper", "scissors"]

    def play(self):

        p1_rounds_won = 0
        p2_rounds_won = 0

        continue_play = True
        while continue_play:

            user_move = input("Enter a choice (rock, paper, scissors): ")
            if self.game_option == 1:
                # play against computer
                p2_move = self.computer()
            else:
                # play against user
                p2_move = input("Enter a choice (rock, paper, scissors): ")
            # self.round += 1
            outcome = self.winner(user_move, p2_move)
            if outcome == 'draw':
                continue
            if outcome == user_move:
                p1_rounds_won += 1
                # self.score['player'] += 1
            else:
                p2_rounds_won += 1
                # self.score['computer'] += 1

            if (p1_rounds_won == self.max_wins):
                print("Player 1 Wins!")
                continue_play = False
            if (p2_rounds_won == self.max_wins):
                print("Player 2 Wins!")
                continue_play = False
        return

    def winner(self, move1, move2):
        m1 = 'Player 1'
        m2 = 'Player 2'
        if move1 == move2:
            print(f"Both players selected {move1}. It's a tie!")
            return 'draw'
        elif move1 == "rock":
            if move2 == "scissors":
                print("Rock smashes scissors! {} wins, {} loses".format(m1, m2))
                return move1
            else:
                print("Paper covers rock! {} wins, {} loses".format(m2, m1))
                return move2
        elif move1 == "paper":
            if move2 == "rock":
                print("Paper covers rock! {} wins, {} loses".format(m1, m2))
                return move1
            else:
                print("Scissors cuts paper! {} wins, {} loses.".format(m2, m1))
                return move2
        elif move1 == "scissors":
            if move2 == "paper":
                print("Scissors cuts paper! {} wins, {} loses!".format(m1, m2))
                return move1
            else:
                print("Rock smashes scissors! {} wins, {} loses.".format(m2, m1))
                return move2

    def computer(self):
        return random.choice(self.moves)
