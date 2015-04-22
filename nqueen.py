import copy, sys

solution = []
board = []
finish = False
solc = 0

def nqueen(N):
    global board
    board = [[0 for i in range(N)] for i in range(N)]

    def is_safe(row, col):
        global board
        queens = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    queens.append([i, j])
        #print queens
        for queen in queens:
            qr, qc = queen
            if qr == row or qc == col:
                return False
            if (qr + qc) == (row + col) or (qc - qr) == (col - row):
                return False
        return True

    def place(row, col):
        global solution, board, finish, solc
        #print 'Call', row, col
        
        sol = False
        
        if finish:
            return solution

        if row == len(board):
            #finished here
            solc += 1
            #print 'Solution', solc
            #print board
            solution.append(copy.deepcopy(board))
            return solution
        
        while col < len(board):
            if is_safe(row, col):
                #print 'Put queen at', row, col
                #put a queen here
                board[row][col] = 1
                place(row+1,0)
                if row+1==len(board):
                    sol = True
            else:
                col += 1

        #print 'Backtrack no col safe for row', row
        #nothing, backtrack
        if row == 0:
            print 'Finish'
            finish = True
            return solution

        for c in range(len(board)):
            if board[row-1][c] == 1:
                #remove queen, but first clear the top row
                if sol:
                    board[row] = [0 for i in range(len(board))]
                board[row-1][c] = 0
                #print 'removed queen at ', row - 1, c
                #now go back and try one col right
                place(row-1,c+1)

    place(0,0)

sys.setrecursionlimit(10000)
try:                    
    nqueen(8)
except Exception as e:
    print e
    
print len(solution)
print solution[len(solution) - 1]
