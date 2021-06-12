from games import *

def tictactoe_game():
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
