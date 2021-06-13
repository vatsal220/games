import random

class RockPaperScizor():
    def __init__(self, game_option, rounds):
        self.game_option = game_option
        self.max_rounds = rounds
        self.moves = ["rock", "paper", "scissors"]
        self.score = {}

    def play(self):
        
        pass

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
        pass

    def computer(self):
        return random.choice(self.moves)


def main():

    user_action = input("Enter a choice (rock, paper, scissors): ")

    pass

if __name__ == '__main__':
    main()
