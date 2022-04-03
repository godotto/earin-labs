from time import sleep
import user_input as uin
import algorithm_functions as af
import os

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
    while (move < 1 or move > 9) or not move:
        print("Please pick a field from 1 to 9")
        move = uin.integer_input()

        if (move < 1 or move > 9) or not move:
            print("You have to pick a field between 1 and 9")
            sleep(1)
            clear_console()
        if board[move-1] != ' ':
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
    print("\t  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("\t     |     |")
    print("\n")    

def update_board(move, player, board):
    board[move-1]= player
    return board

def init_game():
    board = [' ' for _ in range(9)]
    (user_player, algorithm_player) = get_players()
    print(f"PLAYERS ARE: user: {user_player}, algorithm: {algorithm_player}")
    print_board(board)
    return board,user_player,algorithm_player 

def play_tic_tac_toe():
    
    #create board, pick x's and o's for players
    (board, user_player, algorithm_player) = init_game()

    #TODO: add algorithm moves and game loop

    # loop for moves (while no victory from either user or algorithm)
    board = update_board(get_user_move(board),user_player,board)
    print_board(board)



play_tic_tac_toe()
