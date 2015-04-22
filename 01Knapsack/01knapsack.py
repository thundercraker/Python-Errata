#01 knapsack 
n = int(raw_input())
W = int(raw_input())
ws = raw_input().split()
vs = raw_input().split()
w = []
v = []
for i in range(n):
    w.append(int(ws[i]))
    v.append(int(vs[i]))

L = []

def knap(k, m, S):
    
    if k < 0 or m < 0:
        if k > 0:
            return [0, S]
        return [0, S]

    value = knap(k-1, m, S)[0]
    
    if(w[k] < m):
        ret = knap(k-1, m-w[k], S)
        cand = ret[0] + v[k]
        
        if cand > value:
            value = cand
            S = [k] + ret[1]

    return [value, S]

print knap(n-1,W,[])
