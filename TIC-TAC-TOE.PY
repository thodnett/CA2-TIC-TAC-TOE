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

def compMove():
    """Function that handles AI player moves.
    """
    possibleMoves = [x for x, letter in enumerate(game_board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = game_board[:]
            boardCopy[i] = let
            if isWin(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

def selectRandom(li):
    """Selects a random move from the possible moves.
    """
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(game_board):
    """Checks if the board is full
    """
    if game_board.count(' ') > 1:
        return False
    else:
        return True

def main():
    """Main function for gameplay.
    """
    print('Welcome to Tic Tac Toe!')
    showBoard(game_board)

    while not(isBoardFull(game_board)):
        if not(isWin(game_board, 'O')):
            humanMove()
            showBoard(game_board)
        else:
            print('Sorry, O\'s won this time!')
            break
        
        if not(isWin(game_board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                showBoard(game_board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(game_board):
        print('Tie Game!')

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        game_board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        print("Maybe another time!")
        break
