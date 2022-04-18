from time import sleep
import os

import numpy as np

import user_input as uin
import minimax

def clear_console():
    """
    Clears console's output.
    """
    # if OS is *nix
    clear_command = "clear"

    # if OS is Windows
    if os.name == "nt":
        clear_command = "cls"

    os.system(clear_command)

def is_user_first():
    clear_console()

    user_choice = ''
    while (user_choice !='y' and user_choice !='n') or not user_choice:
        print("Pick if you want to play first: 'y' if yes or 'n' if no")
        user_choice = uin.char_input()

        if  (user_choice !='y' and user_choice !='n') or not user_choice:
            print("You have to type either 'y' or 'n'")
            sleep(1)
            clear_console()

    if user_choice=='y': 
       return True
    else:
        return False    

def get_players():
 
    clear_console()

    user_player = ''
    while (user_player !='o' and user_player !='x') or not user_player:
        print("Pick which do you want to play with: x or o")
        user_player = uin.char_input()

        if  (user_player !='o' and user_player !='x') or not user_player:
            print("You have to type either 'x' or 'o'")
            sleep(1)
            clear_console()
    algorithm_player = ''
    if user_player=='o': 
       algorithm_player = 'x'
    else:
        algorithm_player = 'o'     

    return user_player, algorithm_player

def get_user_move(board):

    move = 0
    while (move < 1 or move > 9) or not move:
        print("Please pick a field from 1 to 9")
        move = uin.integer_input()

        if (move < 1 or move > 9) or not move:
            print("You have to pick a field between 1 and 9")
            sleep(1)
            clear_console()
            print_board(board)
        if board.flat[move-1] != ' ':
            move = 0
            print("Field is already occupied. Try another one.")
            print_board(board)
            sleep(3)
            clear_console()
            print_board(board)

    return move   

def get_game_mode():
    clear_console()

    game_mode = ''
    while (game_mode !='m' and game_mode !='a') or not game_mode:
        print("Pick game mode: for user vs bot type 'm' (manual), for bot vs bot type 'a' (automatic)")
        game_mode = uin.char_input()

        if (game_mode !='m' and game_mode !='a') or not game_mode:
            print("You have to type either 'm' or 'a'")
            sleep(1)
            clear_console()

    return game_mode


def is_x_bot_first():
    clear_console()

    user_choice = ''
    while (user_choice !='y' and user_choice !='n') or not user_choice:
        print("Pick if x bot starts first: 'y' if yes or 'n' if no")
        user_choice = uin.char_input()

        if  (user_choice !='y' and user_choice !='n') or not user_choice:
            print("You have to type either 'y' or 'n'")
            sleep(1)
            clear_console()

    if user_choice=='y': 
       return True
    else:
        return False    


def print_board(board):
    print("\n")
    print("\t  CURRENT BOARD \t")
    print("\t     |     |")
    print(f"\t  {board[0, 0]}  |  {board[0, 1]}  |  {board[0, 2]}")
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print(f"\t  {board[1, 0]}  |  {board[1, 1]}  |  {board[1, 2]}")
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print(f"\t  {board[2, 0]}  |  {board[2, 1]}  |  {board[2, 2]}")
    print("\t     |     |")
    print("\n")    

def update_board(move, player, board):
    board.flat[move-1] = player
    return board

def init_game():
    board = np.ndarray(shape=(3, 3), dtype="<U1")
    board[:] = ' '
    (user_choice, algorithm_player) = get_players()
    print(f"PLAYERS ARE: user: {user_choice}, algorithm: {algorithm_player}")
    print_board(board)
    return board, user_choice, algorithm_player 


def user_vs_bot():

    board, user_player, algorithm_player = init_game()

    is_maximizing = True if algorithm_player == 'x' else False 
    is_ai_turn = not is_user_first()

    # loop for moves (while no victory from either user or algorithm)
    while (minimax.heuristic_function(board) is None):
        if is_ai_turn:
            board = update_board(minimax.minimax(board, np.NINF, np.inf, is_maximizing)[1]+1, algorithm_player, board)
        else:
            board = update_board(get_user_move(board), user_player, board)

        print_board(board)
        is_ai_turn = not is_ai_turn

    return minimax.heuristic_function(board)    


def bot_vs_bot():
    board = np.ndarray(shape=(3, 3), dtype="<U1")
    board[:] = ' '

    is_x_turn = True if is_x_bot_first() else False

    # loop for moves (while no victory from either user or algorithm)
    while (minimax.heuristic_function(board) is None):
        if is_x_turn:
            board = update_board(minimax.minimax(board, np.NINF, np.inf, True)[1]+1, 'x', board)
        else:
            board = update_board(minimax.minimax(board, np.NINF, np.inf, False)[1]+1, 'o', board)

        print_board(board)
        sleep(2)
        is_x_turn = not is_x_turn

    return minimax.heuristic_function(board) 

def play_noughts_and_crosses():

    game_mode = get_game_mode()
    game_result = user_vs_bot() if game_mode == 'm' else bot_vs_bot()

    if game_result==1:
        print("Crosses win!")
    elif game_result==-1:
        print("Noughts win!") 
    else:
        print("It's a draw!")
