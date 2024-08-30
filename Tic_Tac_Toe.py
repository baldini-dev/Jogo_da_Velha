import random

def displayBoard(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def enterMove(board):
    move = input("Digite o número do quadrado onde você deseja jogar (1-9): ")
    while not move.isdigit() or int(move) < 1 or int(move) > 9:
        move = input("Entrada inválida. Digite o número do quadrado onde você deseja jogar (1-9): ")
    move = int(move) - 1
    row = move // 3
    col = move % 3
    if board[row][col] == "O" or board[row][col] == "X":
        print("O quadrado escolhido já está ocupado. Tente novamente.")
        enterMove(board)
    else:
        board[row][col] = "O"
        return board

def makeListOfFreeFields(board):
    print("Vez do computador.")
    available_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "O" and board[i][j] != "X":
                available_squares.append((i, j))
    if available_squares:
        row, col = random.choice(available_squares)
        board[row][col] = "X"
    else:
        print("O jogo terminou em empate.")
        return None
    return board

def victoryFor(board, sign):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        elif board[0][i] == board[1][i] == board[2][i] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def drawMove():
    board = [[str(i + j*3 + 1) for i in range(3)] for j in range(3)]
    board[1][1] = "X"
    displayBoard(board)
    while True:
        board = enterMove(board)
        displayBoard(board)
        if victoryFor(board, "O"):
            print("Você ganhou!")
            break
        board = makeListOfFreeFields(board)
        if not board:
            break
        displayBoard(board)
        if victoryFor(board, "X"):
            print("Você perdeu.")
            break

if __name__ == "__main__":
    drawMove()