from itertools import product
import os
import time
import numpy as np

TERMX, TERMY = os.get_terminal_size()
DEFAULT_HEIGHT = 6
DEFAULT_WIDTH = 7
ANIMATION_DELAY = .1

def print_lines(*lines):
    """
    Print `lines` centered in terminal.
    """
    for line in lines:
        print(line.center(TERMX))


class ConnectFour():
    """
    ConnectFour! The first player to connect four checkers in a row wins!
    Notes:
    Our current_player is either 0 or 1, but the players are represented with 1 or 2 on our
    board (empty cells are 0).
    """
    current_move = None
    current_player = 0

    def __init__(self, height=DEFAULT_HEIGHT, width=DEFAULT_WIDTH):
        self.height, self.width = height, min(width, 35)
        self.labels = "1234567890abcdefghijklmnoprstuvwxyz"[:self.width]
        self.board = np.zeros((self.height, self.width), dtype=int)
        self.checkers_in_column = [0] * self.width

    def print_board(self):
        """
        Print our current board state.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

        header = f"╷{'╷'.join(self.labels)}╷"
        gutter = (f"│{'│'.join(' ●○'[value] for value in row)}│" for row in self.board)
        footer = f"╰{'─┴' * (self.width - 1)}─╯"

        print("\n" * ((TERMY - self.height - 5) // 2))  # Vertical Buffer
        print_lines(header, *gutter, footer)

    def is_move_valid(self):
        """
        Returns True if self.current_move is a valid move or 'q'.
        """
        if self.current_move is None:
            return False

        if self.current_move == 'q':
            return True

        if not (len(self.current_move) == 1 and self.current_move in self.labels):
            print_lines("Please input a valid column!")
            return False

        self.current_move = self.labels.find(self.current_move)

        # Check that a move is possible in given column.
        if self.checkers_in_column[self.current_move] < self.height:
            return True

        print_lines("No moves possible in that column!")
        return False

    def get_move(self):
        print_lines(f"{'●○'[self.current_player]}'s move, enter column or 'q' to quit:\n")
        self.current_move = input("".center(TERMX // 2)).lower()

    def animate_move(self):
        """
        Animate a checker falling into place.
        """
        for row in range(self.height - self.checkers_in_column[self.current_move] - 1):
            self.board[row, self.current_move] = self.current_player + 1
            self.print_board()
            self.board[row, self.current_move] = 0
            time.sleep(ANIMATION_DELAY)

    def update_board(self):
        """
        Add a checker to the board.
        """
        column = self.current_move
        self.checkers_in_column[column] += 1
        self.board[self.height - self.checkers_in_column[column], column] = self.current_player + 1

    def is_connect_four(self):
        """
        Returns True if a player has won.
        """
        # Location of our last checker
        row, column = self.height - self.checkers_in_column[self.current_move], self.current_move

        player = self.current_player + 1

        # Look down
        if row + 3 < self.height and (self.board[row:row + 4, column] == player).all():
            return True

        # Look right
        for x in (column - i for i in range(3) if column - i >= 0):
            if x + 3 < self.width and (self.board[row, x:x + 4] == player).all():
                return True

        # Look left
        for x in (column + i for i in range(3) if column + i < self.width):
            if x - 3 >= 0 and (self.board[row, x - 3:x + 1] == player).all():
                return True

        # Look on the up-left, up-right, down-left, down-right diagonals.
        if any(self._diagonal(y_step, x_step) for y_step, x_step in product((-1, 1), repeat=2)):
            return True

        return False

    def _diagonal(self, y_step, x_step):
        """
        If our cell is at the '1':
            O O O O X
            O O O X O
            O O 1 O O
            O 2 O O O
            3 O O O O
        and we're checking the diagonal in the direction of the 'X', we'll also check the
        same diagonal in the cell located at '2' and '3'.  This should cover cases where
        the last checker placed in a four-in-a-row is not at the ends.
        """
        row, column = self.height - self.checkers_in_column[self.current_move], self.current_move
        player = self.current_player + 1

        for y, x in ((row - y_step * i, column - x_step * i) for i in range(3)):

            #Check that either end of the diagonal is in bounds.
            if not all((0 <= y < self.height, 0 <= y + 3 * y_step < self.height,
                        0 <= x < self.width, 0 <= x + 3 * x_step < self.width)):
                continue

            if all(self.board[y + y_step * i, x + x_step * i] == player for i in range(4)):
                return True

        return False

    def run(self):
        '''
        This function will allow the user to play the game. It will execute valid moves and
        be aware if the user wants to quit playing the game through pressing the 'q' button.
        '''

        for _ in range(self.width * self.height):
            self.current_move = None

            self.print_board()

            while not self.is_move_valid():
                self.get_move()

            if self.current_move == "q":
                break

            self.animate_move()

            self.update_board()

            if self.is_connect_four():
                self.print_board()
                print_lines(f"{'●○'[self.current_player]} wins!")
                break

            self.current_player ^= 1

        else:
            self.print_board()
            print_lines("It's a draw!")


if __name__ == "__main__":
    ConnectFour().run()
