import random
import numpy as np
import curses
from curses import wrapper

class Snake():
    def __init__(self, grid_size):
        '''
        params:
            grid_size (List) : The list holds the number the rows and columns
        '''
        self.grid_size = grid_size

    def generate_map(self):
        '''
        This function will generate the map for the snake to move on
        '''
        try:
            map = np.zeros(grid_size)
            return map
        except:
            raise ValueError("Please enter valid grid size dimensions")

    def move_user(self):
        pass

    def play(self):
        pass

    def generate_apple(self):
        pass

if __name__ == '__main__':
    print('snake game testing')
