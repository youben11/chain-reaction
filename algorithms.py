def newBoard(n, p):
    board = [[(0, 0) for column in range(p)] for row in range(n)]
    return board

def possible(gameBoard, n, m, i, j, player):
    if i not in range(n) or j not in range(m):
        return False
    cell = gameBoard[i][j]
    if cell[0] == 0 or cell[0] == player:
        return True
    else:
        return False

def put(gameBoard, n, m, i, j, player):
    #The "if win" after each recursive put()
    #is used to avoid the infinite recursion
    cell_cap = 4
    if i == 0 or i == n-1:
        #cell in top or bottom side
        cell_cap -= 1
    if j == 0 or j == m-1:
        #cell in left or right side
        cell_cap -= 1
    #cell_cap == 2 if a corner
    cell = gameBoard[i][j]
    pawns = cell[1] + 1
    if pawns == cell_cap:
        gameBoard[i][j] = (0, 0)
        if cell_cap == 4:
            put(gameBoard, n, m, i-1, j, player)
            if win(gameBoard, n, m, player):
                return
            put(gameBoard, n, m, i+1, j, player)
            if win(gameBoard, n, m, player):
                return
            put(gameBoard, n, m, i, j-1, player)
            if win(gameBoard, n, m, player):
                return
            put(gameBoard, n, m, i, j+1, player)
        else:
            if i < n-1:
                #add on the bottom side
                put(gameBoard, n, m, i+1, j, player)
                if win(gameBoard, n, m, player):
                    return
            if i > 0:
                #add on the top side
                put(gameBoard, n, m, i-1, j, player)
                if win(gameBoard, n, m, player):
                    return
            if j < m-1:
                #add on the right side
                put(gameBoard, n, m, i, j+1, player)
                if win(gameBoard, n, m, player):
                    return
            if j > 0:
                #add on the left side
                put(gameBoard, n, m, i, j-1, player)
                if win(gameBoard, n, m, player):
                    return
    else:
        gameBoard[i][j] = (player, pawns)

def loose(gameBoard, n, m, player):
    for row in range(n):
        for column in range(m):
            cell = gameBoard[row][column]
            if cell[0] == player:
                return False
    return True

def win(gameBoard, n, m, player):
    for row in range(n):
        for column in range(m):
            cell = gameBoard[row][column]
            if cell[0] == 0:
                #no player control the cells
                continue
            if cell[0] != player:
                return False
    return True

def print_board(board):
    r = len(board)
    c = len(board[0])

    for row in board:
        for col in row:
            print "(%d,%d)" % col,
        print ""
