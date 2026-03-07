from collections import deque

def check_winner(board):
    win_positions = [
            (0,1,2),
            (3,4,5),
            (6,7,8),
            (0,3,6),
            (1,4,7),
            (2,5,8),
            (0,4,8),
            (2,4,6)
            ]

    for a,b,c in win_positions:
         if board[a]==board[b]==board[c]!=' ':
             return board[a]
         return None

def generate_states(board,player):
    states = []
    for i in range (9):
        if board[i] == ' ':
            new_board = board.copy()
            new_board[i] = player
            states.append(new_board)
    
    return states

def bfs():
    initial_board = [' '] *9
    
    queue = deque()

    queue.append((initial_board,'X'))

    while queue:
        board,player = queue.popleft()
        winner = check_winner(board)
        if winner:
            print("Winner found!")           
            print_board(board)
            return 

        new_player = 'O' if player =='X' else 'X'

        for state in generate_states(board,player):
            queue.append((state,new_player))
            
    print("NO winner found!")

def print_board(board):
    print("\nThe final configuration is\n")
    for i in range(0,9,3):
        print(board[i],"|",board[i+1],"|",board[i+2])
        if i < 6:
          print("---*---*---*")
    print()

bfs()



























