import random

class RockPaperScissors():
    def __init__(self, game_option, rounds):
        '''
        This class initiates the Rock Paper Scissors game between a user and a computer
        or between two users based on the input parameters specified.

        params:
            game_option (Integer) : 1 if you want to verse a computer, 2 if you want to
                                    verse another player
            rounds (Integer) : An positive odd integer

        example:
            rps = RockPaperScissors(game_option = 1, rounds = 5)
            rps.play()
        '''
        self.game_option = game_option
        self.max_rounds = rounds
        self.max_wins = self.max_rounds // 2 + 1
        self.moves = ["rock", "paper", "scissors"]

    def play(self):
        '''
        This function will play the Rock Paper Scissors game with a user versus
        a computer or a user versus another user
        '''

        p1_rounds_won = 0
        p2_rounds_won = 0

        continue_play = True
        while continue_play:
            valid_move = True
            while valid_move:
                user_move = input("Enter a choice (rock, paper, scissors): ")
                if user_move.lower().rstrip().lstrip() in self.moves:
                    valid_move = False
                else:
                    print("Please enter a valid move.")
            if self.game_option == 1:
                # play against computer
                p2_move = self.computer()
            else:
                # play against user
                valid_move = True
                while valid_move:
                    p2_move = input("Enter a choice (rock, paper, scissors): ")
                    if p2_move.lower().rstrip().lstrip() in self.moves:
                        valid_move = False
                    else:
                        print("Please enter a valid move.")
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
        '''
        This function will identify the winner associated to a game of
        rock paper scissors being played.

        params:
            move1 (String) : rock / paper / scissors
            move2 (String) : rock / paper / scissors

        returns:
            It will return the winning move or draw if both moves are
            the same
        '''
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
        '''
        This function will randomly generate moves for the computer to make
        if the player chose option 1
        '''
        return random.choice(self.moves)
