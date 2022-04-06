


# minimax with alpha-beta pruning
def mini_max(board, depth, alfa, beta, player,  is_max):
    # if state  == terminal state 
   if is_victory(board,player) and is_max == True:
       return 1
   elif is_victory(board, player) and is_max == False:
       return -1
   elif is_draw(board, player):
       return 0

   if depth == 0:
       # evaluate and return heuristic 
    return heuristic(board, player, is_max)   

    #recursive action with alpha-beta



   pass



def is_draw(board, player):
    pass

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

def heuristic(board, player, is_max):
    pass

def are_equal(arr1, arr2):
    if arr1.size != arr2.size:
        return False

    for i in arr1.size:
        if arr2[i] != arr1[i]:
            return False

    return True           

def get_algorithm_move():
    pass
