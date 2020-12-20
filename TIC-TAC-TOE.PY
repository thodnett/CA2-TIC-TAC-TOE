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

def showBoard(board):
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
