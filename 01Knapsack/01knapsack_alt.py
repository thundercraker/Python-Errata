#01knapsack
# n = 5
# W = 10
# w = [2,3,5,6,1]
# v = [1,2,4,6,2]

n = int(raw_input())
W = int(raw_input())
ws = raw_input().split()
vs = raw_input().split()
w = []
v = []
for i in range(n):
    w.append(int(ws[i]))
    v.append(int(vs[i]))

def knap(k, m, S):
    global w,v
    if k < 0 or m < 0:
        if k > 0:
            return [0, S]
        return [0, S]

    com = knap(k-1,m, S)
    value = com[0]
    
    print k,m
    
    if w[k] <= m:
        ret = knap(k-1, m-w[k], S)
        value = max(value, ret[0] + v[k])
        S = [k] + ret[1]

    return [value, S]

print knap(n-1,W,list())
    
