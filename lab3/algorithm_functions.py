


# minimax with alpha-beta pruning
from cmath import inf


def mini_max(board, alpha, beta, player, is_maximizing):

    #TODO: rewrite this start part so that it returns a pair - score and move
    # if state  == terminal state 
    if is_victory(board,player) and is_maximizing == True:
       return 1
    elif is_victory(board, player) and is_maximizing == False:
       return -1
    elif is_draw(board, player):
       return 0

    #recursive action with alpha-beta
    if(is_maximizing):
        best_move = -1
        best_score = -inf
        for i in board.size:
            if board[i]==' ':
                # set current field to ai player
                board[i]=player
                # calculate score
                curr_score = mini_max(board, alpha,beta, not is_maximizing)
                # restore board value
                board[i]=' '
                move = i
                if curr_score > best_score:
                    best_score = curr_score
                    best_move = move
                alpha = max(best_score,alpha)
                if alpha >= beta:
                    break

        return (best_move, best_score)

    else:
        if player=='o': 
            other_player='x' 
        else: 
            other_player='o'

        best_move = -1
        best_score = -inf
        for i in board.size:
            if board[i]==' ':
                # set current field to ai player
                board[i]=other_player
                # calculate score
                curr_score = mini_max(board, alpha,beta, not is_maximizing)
                # restore board value
                board[i]=' '
                move = i
                if curr_score < best_score:
                    best_score = curr_score
                    best_move = move
                beta = max(best_score,alpha)
                if alpha >= beta:
                    break

    return (best_move, best_score)


def is_draw(board):
    for i in board.size:
        if board[i]!=' ':
            return False
    return True        

def is_victory(board, player):
    terminal_states  = [
    { 0, 1, 2 },
    { 3, 4, 5 },
    { 6, 7, 8 },
    { 0, 3, 6 },
    { 1, 4, 7 },
    { 2, 5, 8 },
    { 0, 4, 8 },
    { 2, 4, 6 }
    ]

    player_fields = []

    for i in board.size:
        if board[i]== player:
            player_fields.append(i)

    for i in terminal_states.size:
        if are_equal(player_fields,terminal_states[i]):
            return True

    return False   


def are_equal(arr1, arr2):
    if arr1.size != arr2.size:
        return False

    for i in arr1.size:
        if arr2[i] != arr1[i]:
            return False

    return True           

def get_algorithm_move():
    pass
