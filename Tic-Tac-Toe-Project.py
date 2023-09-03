print("-------------------------: Tic Tac Toe Game :------------------------")

board = []

for i in range(9):
    board.append(" ")

# print(board)

def struct_board():  
    print(" "+ board[0] +" | "+ board[1] +" | "+ board[2] )
    print("---|---|---")
    print(" "+ board[3] +" | "+ board[4] +" | "+ board[5] )
    print("---|---|---")
    print(" "+ board[6] +" | "+ board[7] +" | "+ board[8] )

# struct_board()

def player_win(player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[1+2] == player:
            return True
        
    for i in range(3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
        
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    
    return False

# player = "X"

player = input("Choose your symbol (X or O) : ").upper()

while player not in ("X", "O"):
    print("Please enter valid input..!")
    player = input("Choose your symbol (X or O) : ").upper()
    
opponent = "X" if player == "O" else "O"


print("\n Tic Tac Teo Board Structure..! \n")
# struct_board()

while True:
    
    
    struct_board()

    move = input(f"Player {player}, Enter Your move (1-9) : ")

    try:
        move = int(move)

        if move < 1 and move > 9 or board[move-1] != " ":
            print("Plase enter valid move..!")
            # return True
            continue
        
    except ValueError:
        print("Invalid input, Please try to entered input (1-9)")

    board[move-1] = player

    if player_win(player):
        struct_board()
        print(f"The game was ended succesfully, Player {player} wins the game..!")
        break

    if " " not in board:
        struct_board()
        print("The game was drawn by effects of users..!")
        break

#     player = "0" if player == "X" else "X"
    player, opponent = opponent, player
    
    
    
    
