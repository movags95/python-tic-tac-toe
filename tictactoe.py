import os
import time
import random

def clear_screen(sleep=0):
    time.sleep(sleep)
    os.system('clear')

def display_board(board):
    print('  ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-------------')
    print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-------------')
    print('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def player_input():
    marker = ''

    while not(marker == 'X' or marker == 'O'):
        marker = input('Please select a marker for player 1 (X/O): ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker
    

def check_if_board_full(board):
    if ' ' in board[1:]:
        return False
    else: 
        return True

def check_space(board, postion):
    if board[postion] == ' ':
        return True
    else:
        return False
    
def player_choice(board):
    position = 0
    while position not in [i for i in range(1, 10)] or not(check_space(board,position)):
        position = int(input('Please enter a position to put your marker (1-9): '))

    return position

def choose_first():
    x = random.randint(0,1)
    if x == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def replay():
    return input('Do you want to play again?\n').lower().startswith('y')

def game_won(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #top 3
            (board[4] == mark and board[5] == mark and board[6] == mark) or #middle 3
            (board[7] == mark and board[8] == mark and board[9] == mark) or #botton 3
            (board[1] == mark and board[4] == mark and board[7] == mark) or #first column
            (board[2] == mark and board[5] == mark and board[8] == mark) or #second column
            (board[3] == mark and board[6] == mark and board[9] == mark) or #third column
            (board[1] == mark and board[5] == mark and board[9] == mark) or #diagonal 1
            (board[3] == mark and board[5] == mark and board[7] == mark)   #diagonal 2
            )

if __name__ == '__main__':
    while True:
        test_board = [' ']*10

        print('Welcome to TicTacHoes')
        player1_marker, player2_marker = player_input()

        turn = choose_first()
        print(f'{turn} will go first.')

        gameon = input('Are you ready to play the game. Yes or no?').lower().startswith('y')

        while gameon:
            if turn == 'Player 1':
                display_board(test_board)
                position = player_choice(test_board)
                place_marker(test_board,player1_marker,position)

                if game_won(test_board, player1_marker):
                    display_board(test_board)
                    print('Congratulations, player 1 has won.')
                    gameon = False
                elif check_if_board_full(test_board):
                    display_board(test_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

            else: 
                #player 2 turn
                display_board(test_board)
                position = player_choice(test_board)
                place_marker(test_board, player2_marker, position)

                if game_won(test_board, player2_marker):
                    print('Congratulations, player 2 has won.')
                    gameon = False
                elif check_if_board_full(test_board):
                    display_board(test_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

        if not(replay()):
            break
