from time import sleep
import os

import numpy as np

import user_input as uin
import algorithm_functions as af
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
    while (move < 0 or move > 8) or not move:
        print("Please pick a field from 0 to 8")
        move = uin.integer_input()

        if (move < 0 or move > 8) or not move:
            print("You have to pick a field between 0 and 8")
            sleep(1)
            clear_console()
        if board.flat[move] != ' ':
            move = 0
            print("Field is already occupied. Try another one.")
            print_board(board)
            sleep(3)
            clear_console()
       
    return move   

     

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
    board.flat[move - 1] = player
    return board

def init_game():
    board = np.ndarray(shape=(3, 3), dtype="<U1")
    board[:] = ' '
    (user_player, algorithm_player) = get_players()
    print(f"PLAYERS ARE: user: {user_player}, algorithm: {algorithm_player}")
    print_board(board)
    return board, user_player, algorithm_player 

def play_tic_tac_toe():
    
    #create board, pick x's and o's for players
    board, user_player, algorithm_player = init_game()

    #TODO: add algorithm moves and game loop

    # loop for moves (while no victory from either user or algorithm)
    board = update_board(get_user_move(board), user_player, board)
    print_board(board)

    ai_turn_indicator = True

    while (minimax.heuristic_function(board) is None):
        if ai_turn_indicator:
            board = update_board(minimax.minimax(board, np.NINF, np.inf, True)[1], algorithm_player, board)
        else:
            board = update_board(get_user_move(board), user_player, board)
            
        print_board(board)
        ai_turn_indicator = not ai_turn_indicator


play_tic_tac_toe()
