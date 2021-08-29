import numpy as np
import random

def print_lines(*lines):
    """
    Print `lines` centered in terminal.
    """
    for line in lines:
        print(line.center(TERMX))

class Sudoku():
    def __init__(self, grid_size):
        self.grid_size = grid_size

    def generate_board(self):
        """
        Print our current board state.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
    
        pass

    def solver(self):
        '''
        This function will solve the sudoku board upon request
        '''
        pass

    def remove_elements(self):
        pass

    def is_valid_solution(self):
        pass

    def play(self):
        pass

if __name__ == '__main__':
    sd = Sudoku(grid_size = 9)
    print('here')
