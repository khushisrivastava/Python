import os
import random

def clear_screen():
    os.system('cls')

def print_board(board):
    clear_screen()
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |   ')

def player_input():
    marker=' '
    while marker!='X' and marker!='O':
        marker=input('player1 choose X or O: ').upper()
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return(player1,player2)

def place_marker(board,marker,position):
    board[position]=marker

def check_win(marker):
    if (board[1]==marker and board[2]==marker and board[3]==marker)or(board[4]==marker and board[5]==marker and board[6]==marker)or(board[7]==marker and board[8]==marker and board[9]==marker)or(board[1]==marker and board[4]==marker and board[7]==marker)or(board[2]==marker and board[5]==marker and board[8]==marker)or(board[3]==marker and board[6]==marker and board[9]==marker)or(board[3]==marker and board[5]==marker and board[7]==marker)or(board[1]==marker and board[5]==marker and board[9]==marker):
        return True
    else:
        return False

def choose_first():
    turn=random.randint(0,1)
    if turn==0:
        return('player1')
    else:
        return('player2')

def space_check(board,position):
    if board[position]== ' ':
        return True

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    choice=int(input('Enter the position: '))
    if space_check(board,choice) and choice in range(1,10):
        return choice
    else:
        choice=int(input('Space not available...Enter another position '))

def replay():
    replay= input("Play Again? Enter Yes or No").lower()
    return replay=='yes'

print('WELCOME TO TIC TAC TOE!!!')
play=True
while play:
    Board=' '*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+' will go first')
    play_game=input('ready to play?..Y or N').lower()

    if play_game=='y':
        game_on=True
    else:
        game_on=False

    while game_on:
        if turn=='player1':
            print_board(Board)
            position=player_choice(Board)
            place_marker(Board,player1_marker,position)

            if check_win(player1_marker):
                print('PLAYER 1 WON!!')
                game_on=False
            else:
                if full_board_check(Board):
                    print_board(Board)
                    print('GAME TIED!!')
                    game_on=False
                else:
                    turn='player2'
        else:
            print_board(Board)
            position=player_choice(Board)
            place_marker(Board,player2_marker,position)

            if check_win(player2_marker):
                print('PLAYER 2 WON!!')
                game_on=True
            else:
                if full_board_check(Board):
                    print_board(Board)
                    print('GAME TIED!!')
                    game_on=true
                else:
                    turn='player1'
    play=replay()

else:
    print('Thanks for playing!!!')
