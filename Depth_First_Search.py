n = 6
graph = [(1,2),(1,3),(2,4),(2,5),(3,6),(5,6)]

def DFS():
    global graph
    visited = []

    root = 1
    #get first edge
    stack = []
    stack.append(root)
    visited.append(root)
    
    while stack:
        parent = stack.pop()
        children = []
        for (u,v) in graph:
            if u == parent:
                children.append(v)
            elif v == parent:
                children.append(u)

        #check then visit
        for child in children:
            if not child in visited:
                stack.append(child)
                visited.append(child)
                #print "Visited: " + str(child)

    return visited

def DFS_path(start, goal):
    global graph

    root = start
    #get first edge
    stack = [(root, [root], [root])]

    paths = []
    
    while stack:
        (parent, parent_path, visited) = stack.pop()
        children = []
        for (u,v) in graph:
            if u == parent:
                children.append(v)
            elif v == parent:
                children.append(u)

        for child in children:
            if goal == child:
                paths.append(parent_path + [child])
                continue

            if not child in visited:
                stack.append((child, parent_path + [child], visited + [child]))
                print (child, parent_path + [child], visited + [child])
            
    return paths

def BFS():
    global graph
    visited = []

    root = 1
    #get first edge
    queue = []
    queue.append(root)
    visited.append(root)
    
    while queue:
        parent = queue.pop(0)
        children = []
        for (u,v) in graph:
            if u == parent:
                children.append(v)
            elif v == parent:
                children.append(u)

        #check then visit
        for child in children:
            if not child in visited:
                queue.append(child)
                visited.append(child)
                #print "Visited: " + str(child)

    return visited

print DFS()
print DFS_path(6,2)
print BFS()
