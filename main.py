# Tic Tac Toe :A Python based game

"""
Algorithm:
1.Creating a board
2.insertLetter()
3.spaceIsFree()
4.printBoard()
5.isWinner()
6.main()
7.isBoardFull()
8.playerMove()
9.computerMove()
10.selectRandom()
"""

# creates an empty board
board = [' ' for x in range(10)]


# inserts given letter at the given position
def insert_letters(letter, pos):
    board[pos] = letter


# public interface
def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


# returns a boolean value true, if empty, and false otherwise
def is_free_space(pos):
    return board[pos] == ' '


# decides winner of the game, satisfying particular condition
def is_winner(board, letter):
    return (board[7] == letter and
            board[8] == letter and
            board[9] == letter) or (board[4] == letter and
                                    board[5] == letter and
                                    board[6] == letter) or (board[1] == letter and
                                                            board[2] == letter and
                                                            board[3] == letter) or (board[1] == letter and
                                                                                    board[4] == letter and
                                                                                    board[7] == letter) or (
                       board[2] == letter and
                       board[5] == letter and
                       board[8] == letter) or (board[3] == letter and
                                               board[6] == letter and
                                               board[9] == letter) or (board[1] == letter and
                                                                       board[5] == letter and
                                                                       board[9] == letter) or (board[3] == letter and
                                                                                               board[5] == letter and
                                                                                               board[7] == letter)


'''
This logic will decide when and how player will move i.e if run variable is set true, it's player's turn.
Further, the input value for move has will have constraints such as

* It should be an integer type

* It should be within 0 to 10 (excluding 0 and 10)

* Space should be free to insert

'''


def player_move():
    run = True
    while run:
        move = input('Please enter a position to insert \'X\':(1-9)')
        try:
            move = int(move)
            if 0 < move < 10:
                if is_free_space(move):
                    run = False
                    insert_letters('X', move)
                else:
                    print("Sorry, this space is occupied!")
            else:
                print('Type number within this range.')
        except TypeError:
            print('Please enter a number.')


'''
This logic looks for possible moves for computer and when it finds one, it returns that 
particular move. We’ll look for corners(1,3,7 or 9), edges(2,4,6 or 8) and the middle(5). 
If found empty, the machine will insert appropriate letter(i.e X)
'''


def computer_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move
    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move
    if 5 in possible_moves:
        move = 5
        return move
    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)
    return move


# It returns a random move from a list of possible moves
def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


# Returns boolean true if board is full, and false otherwise
def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


'''
This logic represents working of the game. As long as the board is not full,
we'll check if computer won, if yes, then we'll print winning message and break
from the loop; otherwise we'll ask user to play it's turn. Similarly,
if user won the game, we'll print winning message; otherwise, we'll ask computer 
to play its turn.

After all, if board is full, we'll print a tie message.
'''


def main():
    print('Welcome to Tic Tac Toe!')
    print_board(board)
    while not is_board_full(board):
        if not is_winner(board, 'O'):
            player_move()
            print_board(board)
        else:
            print('\'O\' won this time.')
            break
        if not is_winner(board, 'X'):
            move = computer_move()
            if move == 0:
                print(" ")
            else:
                insert_letters('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                print_board(board)
        else:
            print('\'X\' won this time')
            break
    if is_board_full(board):
        print('Tie game!')


# We'll use a while loop to control flow of statement i.e. if we want to continue the game or not
answer = 'y'
name = input('Enter your name:')
print(f'Hi {name}')
while answer.lower() == 'y' or answer.upper() == 'Y':
    board = [' ' for x in range(10)]
    print('--------------------------')
    main()
    answer = input('Do you want to play again?(y/n) ')
    