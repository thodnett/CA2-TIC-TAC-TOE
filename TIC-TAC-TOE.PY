"""Draws the board"""
game_board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    """Inserts the given letter in the given position.
    """
    game_board[pos] = letter

def spaceIsFree(pos):
    """Checks if board space is free.
    """
    return game_board[pos] == ' '

def showBoard(game_board):
    """Prints the board.
    """
    print('   |   |')
    print(' ' + game_board[7] + ' | ' + game_board[8] + ' | ' + game_board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + game_board[4] + ' | ' + game_board[5] + ' | ' + game_board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + game_board[1] + ' | ' + game_board[2] + ' | ' + game_board[3])
    print('   |   |')

def isWin(bo, le):
    """Given a board and a player’s letter, this function returns True if that player has won.
    """
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def humanMove():
    """Function which handles human players moves.
    """
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!') 

