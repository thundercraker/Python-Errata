maze = [[0,0,0,0,0],
        [0,1,0,1,0],
        [0,0,0,0,0],
        [1,0,1,0,1],
        [0,0,0,0,0]]

for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze[row][col] == 1:
            maze[row][col] = "W"
            

import copy
from priorityqueue import *

card = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def mapucs(maze, start, goal):
    global card
    class Node:
        def __init__(self, xy, maze, cost):
            self.maze = copy.deepcopy(maze)
            self.xy = xy
            self.cost = cost

        def printN(self):
            self.printMaze()
            print self.cost
            print self.xy

        def printMaze(self):
            for r in range(len(self.maze)):
                row = ""
                for c in range(len(self.maze[0])):
                    row += str(self.maze[r][c]) + " "
                print row

    def comp(n1,n2):
        if n1.cost < n2.cost:
            return -1
        elif n2.cost > n1.cost:
            return 1
        else:
            return 0

    def legal(maze,xy,move):
        x = xy[0]
        y = xy[1]
        if x >= 0 and x < len(maze):
            if y >= 0 and y < len(maze[0]):
                if maze[x][y] != "W":
                    return True
        return False;

    def move(xy, move):
        return (xy[0] + move[0], xy[1] + move[1])

    root = Node(start, maze, 0)
    frontier = Priority_Queue(comp)
    explored = set()
    frontier.enqueue(root)

    while not frontier.empty():
        parent = frontier.dequeue()

        parent.maze[parent.xy[0]][parent.xy[1]] = 'X'
        explored.add(parent.xy)
        
        if parent.xy == goal:
            return parent

        for d in card:
            newxy = move(parent.xy,d)
            #check legality
            if not newxy in explored:                
                if legal(parent.maze, newxy, d) == True:
                    child = Node(newxy, parent.maze, parent.cost + 1)
                    frontier.enqueue(child)

n = mapucs(maze, (0,0), (4,0))
n. printN()               
            
        
    


        
