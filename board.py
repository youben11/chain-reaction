class Board():
    def __init__(self, n, p):
        self.board = [[(0, 0) for column in range(p)] for row in range(n)]
        self.n = n
        self.m = p

    def possible(self, i, j, player):
        if i not in range(self.n) or j not in range(self.m):
            return False
        cell = self.board[i][j]
        if cell[0] == 0 or cell[0] == player:
            return True
        else:
            return False

    def loose(self, player):
        for row in range(self.n):
            for column in range(self.m):
                cell = self.board[row][column]
                if cell[0] == player:
                    return False
        return True

    def win(self, player):
        for row in range(self.n):
            for column in range(self.m):
                cell = self.board[row][column]
                if cell[0] == 0:
                    #no player control the cells
                    continue
                if cell[0] != player:
                    return False
        return True

    def put(self, i, j, player):
        #The "if win" after each recursive put()
        #is used to avoid the infinite recursion
        gameBoard = self.board
        n = self.n
        m = self.m
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
                self.put(i-1, j, player)
                if self.win(player):
                    return
                self.put(i+1, j, player)
                if self.win(player):
                    return
                self.put(i, j-1, player)
                if self.win(player):
                    return
                self.put(i, j+1, player)
            else:
                if i < n-1:
                    #add on the bottom side
                    self.put(i+1, j, player)
                    if self.win(player):
                        return
                if i > 0:
                    #add on the top side
                    self.put(i-1, j, player)
                    if self.win(player):
                        return
                if j < m-1:
                    #add on the right side
                    self.put(i, j+1, player)
                    if self.win(player):
                        return
                if j > 0:
                    #add on the left side
                    self.put(i, j-1, player)
                    if self.win(player):
                        return
        else:
            gameBoard[i][j] = (player, pawns)
