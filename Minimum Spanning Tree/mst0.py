#filename = raw_input("graph file name : ")
filename = "village.in"
#K - number of sets
K = 3
infile = open(filename, 'r')
n = int(infile.readline())
e = []
for i in range(n):
    x = infile.readline().split()
    for j in range(i):
        if int(x[j]) != -1:
            e.append((i,j,int(x[j])))
infile.close()

def getKey(x):
    return x[2]

e.sort(key=getKey)

from disjointsets import *

x = DisjointSets(len(e) + 2)

minD = -1

def mst():
    global e, K, minD, x
    A = []
    total = 0
    for i in range(len(e) - K + 1):
        #e[i] edges of the vertex e[0], e[1]...
        edges = list(e[i])
        u = edges[0]
        v = edges[1]
        d = edges[2]
        if x.findset(u) != x.findset(v):
            #A = A U (u,v)
            edge = (u, v)
            if not edge in A:
                A.append(edge)
                #total += edges[2]
            minD = d
            x.union(u, v)
    #print total
    return A

#for i in range(len(e) + 2):
#    print x.findset(i)

print mst()
print minD

