import numpy as np
import random

class TicTacToe():
    def __init__(self, game_option, board_size):
        self.game_option = game_option
        self.board_size = board_size

        self.X = 5.
        self.O = 7.

        self.board = self.generate_board()
        self.moves = self.generate_available_moves()

        if self.game_option == 1:
            # play computer
            pass

    def generate_board(self):
        return np.zeros((self.board_size, self.board_size))

    def generate_available_moves(self):
        n = len(self.board)
        moves = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                moves.append([i,j])
        return moves

    def check_winner(self):
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
        return False

    def play(self):
        if self.game_option == 1:
            # versus computer
            continue_play = True
            while continue_play:
                pos = list(eval(input("Please enter in a list, the coordinate corresponding to your move: ")))
                if pos not in self.moves:
                    pos = list(eval(input("Please enter a legal move: ")))
                print(type(pos), pos)
                idx = self.moves.index(pos)
                del self.moves[idx]

                #update board
                self.board[pos[0] - 1][pos[1] - 1] = self.X

                if self.check_winner() != False:
                    continue_play = False

                cpu_pos = self.computer()
                cpu_idx = self.moves.index(cpu_pos)
                del self.moves[cpu_idx]

                #update board
                self.board[cpu_pos[0] - 1][cpu_pos[1] - 1] = self.O

                if self.check_winner() != False:
                    print(self.check_winner())
                    continue_play = False

                for row in self.board:
                    print(row)

    def computer(self):
        if len(self.moves) > 0:
            return random.choice(self.moves)

    def test(self):
        for row in self.board:
            print(row)
        print(self.moves)

def main():
    print(
        '''
        Welcome, you are now playing Tic Tac Toe.
        ---------------------------------------------
        Rules :

        ---------------------------------------------
        Game Options :


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
    T.test()
    T.play()

if __name__ == '__main__':
    main()
