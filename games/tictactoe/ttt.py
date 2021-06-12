import numpy as np
import random

class TicTacToe():
    def __init__(self, game_option, board_size):
        '''
        This class will create the tic tac toe game in terminal for the users to play.

        params:
            game_option (Integer) : 1 if you want to play with a computer, 2 if you
                                    want to play with a friend
            board_size (Integer)  : A value between 3 and 7 corresponding to the size
                                    of the matrix you will play on

        example:
            T = TicTacToe(game_option = 1, board_size = 3)
            T.play()
        '''
        
        self.game_option = game_option
        self.board_size = board_size

        self.X = 5.
        self.O = 7.

        self.board = self.generate_board()
        self.moves = self.generate_available_moves()

        self.move_counter = 0
        self.max_moves = len(self.moves)

    def generate_board(self):
        '''
        This function will generate an NxN matrix corresponding to the board_size
        the user specified
        '''
        return np.zeros((self.board_size, self.board_size))

    def generate_available_moves(self):
        '''
        This function will find all the legal moves availalbe for the user and computer
        to make given the board size
        '''
        n = len(self.board)
        moves = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                moves.append([i,j])
        return moves

    def check_winner(self):
        '''
        This function will determine whether a player is a winner or not. It will be ran
        after every move is made to know whether the game should be continued to play.

        A winner is determined if they have an entire row, column or the diagonal(s)
        filled with their value.
        '''
        n = self.board_size
        winning_x_vals = set([self.X] * n)
        winning_o_vals = set([self.O] * n)

        # check horizontals
        for row in self.board:
            if (set(row) == winning_x_vals) | (set(row) == winning_o_vals):
                print("Winner")
                return

        # check verticals
        for col in self.board.T:
            if (set(col) == winning_x_vals) | (set(col) == winning_o_vals):
                print("winner")
                return

        # check diagonals
        d = set(np.diag(self.board))
        if (d == winning_x_vals) | (d == winning_o_vals):
            print("Winner")
            return

        d2 = set(np.diag(np.fliplr(self.board)))
        if (d2 == winning_x_vals) | (d2 == winning_o_vals):
            print("Winner")
            return

        if self.move_counter == self.max_moves:
            print("Draw")
            return

        return False

    def play(self):
        '''
        This function will initiate the game play of tick tac toe. If this is the first options
        the player will verse a computer, if the second option is chosen then it will play against
        another player.
        '''

        for row in self.board:
            print(row)

        if self.game_option == 1:
            # versus computer
            continue_play = True
            while continue_play:
                pos = list(eval(input("Please enter in a list, the coordinate corresponding to your move: ")))
                if pos not in self.moves:
                    pos = list(eval(input("Please enter a legal move: ")))

                idx = self.moves.index(pos)
                del self.moves[idx]

                #update board
                self.board[pos[0] - 1][pos[1] - 1] = self.X
                self.move_counter += 1

                if self.check_winner() != False:
                    continue_play = False
                    break

                cpu_pos = self.computer()
                cpu_idx = self.moves.index(cpu_pos)
                del self.moves[cpu_idx]

                #update board
                self.board[cpu_pos[0] - 1][cpu_pos[1] - 1] = self.O
                self.move_counter += 1

                if self.check_winner() != False:
                    continue_play = False
                    break

                for row in self.board:
                    print(row)
        else:
            # versus player
            continue_play = True
            while continue_play:
                p1_pos = list(eval(input("Player 1, enter the coordinate corresponding to your move: ")))
                if p1_pos not in self.moves:
                    p1_pos = list(eval(input("Please enter a legal move: ")))

                p1_idx = self.moves.index(p1_pos)
                del self.moves[p1_idx]

                # update board
                self.board[p1_pos[0] - 1][p1_pos[1] - 1] = self.X
                self.move_counter += 1

                if self.check_winner() != False:
                    continue_play = False

                for row in self.board:
                    print(row)

                p2_pos = list(eval(input("Player 2, enter the coordinate corresponding to your move: ")))
                if p2_pos not in self.moves:
                    p2_pos = list(eval(input("Please enter a legal move: ")))

                p2_idx = self.moves.index(p2_pos)
                del self.moves[p2_idx]

                # update board
                self.board[p2_pos[0] - 1][p2_pos[1] - 1] = self.O
                self.move_counter += 1

                if self.check_winner() != False:
                    continue_play = False
                    break

                for row in self.board:
                    print(row)

    def computer(self):
        '''
        This function will randomly generate moves for the computer to make
        if the player chose option 1
        '''
        if len(self.moves) > 0:
            return random.choice(self.moves)

def main():
    print(
        '''
        Welcome, you are now playing Tic Tac Toe.
        -----------------------------------------------------------------
        Rules :
            1) Each player takes turns one after the other
            2) Moves can not be over written
            3) A winner is determined when the entire row, column or
               diagonal is covered with their corresponding symbol
               'x' or 'o'
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
            board_sz = int(input("Please specify the size of the board you wish to play in: "))
            if (board_sz >= 3) & (board_sz <= 7):
                check_input = False
        except ValueError:
            print("Please make sure the value you enter is an integer between 3 and 7")
            check_input = True

    T = TicTacToe(game_option = game_op, board_size = board_sz)
    T.play()

if __name__ == '__main__':
    main()
