import random

class RockPaperScissors():
    def __init__(self, game_option, rounds):
        self.game_option = game_option
        self.max_rounds = rounds
        self.round = 0
        self.max_rounds = self.round // 2 + 1
        self.moves = ["rock", "paper", "scissors"]
        self.score = {}

    def play(self):
        if self.game_option == 1:
            # play against computer
            self.score['player'] = 0
            self.socre['computer'] = 0
            p1_rounds_won = 0
            p2_rounds_won = 0

            continue_play = True
            while continue_play:
                user_move = input("Enter a choice (rock, paper, scissors): ")
                comp_move = self.computer()
                self.round += 1
                self.winner(user_move, comp_move)
                if (p1_rounds_won == self.max_rounds):
                    print("Player 1 Wins!")
                    continue_play = False
                if (p2_rounds_won == self.max_rounds):
                    print("Player 2 Wins!")
                    continue_play = False
        return

    def winner(self, move1, move2):
        if move1 == move2:
            print(f"Both players selected {move1}. It's a tie!")
        elif move1 == "rock":
            if move2 == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif move1 == "paper":
            if move2 == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif move1 == "scissors":
            if move2 == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

    def computer(self):
        return random.choice(self.moves)


def main():
    print(
        '''
        Welcome, you are now playing Rock Paper Scissors.
        -----------------------------------------------------------------
        Rules :
            - Each player takes turns one after the other
            - Each player has an option of playing Rock, Paper or Scissors
            - Rock beats Scissors
            - Paper beats Rock
            - Scissors beats Paper
            - If both players choose the same move then it is a draw
            - The player with the most wins wins the game.
        -----------------------------------------------------------------
        Game Options :
            Option 1 :
                Play against a computer
            Option 2 :
                Play against another player

        Good Luck
        '''
        )

    check_input = True
    while check_input:
        try:
            game_op = int(input("Please specify game option 1 or 2: "))
            if (game_op == 1) | (game_op == 2):
                check_input = False
        except ValueError:
            print("Please make sure the value you enter is an integer corresponding to one of the options specified")
            check_input = True

    check_input = True
    while check_input:
        try:
            n_rounds = int(input("Please specify the number of rounds you want to play (odd int): "))
            if (n_rounds > 0) & (n_rounds % 2 != 0):
                check_input = False
        except ValueError:
            print("Please make sure the value you enter is an positive odd integer: ")
            check_input = True

    rps = RockPaperScissors(game_option = game_op, rounds = n_rounds)
    rps.play()


if __name__ == '__main__':
    main()
