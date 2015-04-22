class DisjointSetNaive:

    def __init__(self, sets):
        self.N = [i for i in range(sets + 1)]

    def findSet(self, X):
        if self.N[X] == X:
            return X
        else:
            return self.findSet(self.N[X])

    def union(self, X, Y):
        xr = self.findSet(X)
        yr = self.findSet(Y)
        if not xr == yr:
            if(xr > yr):
                self.N[xr] = yr
            else:
                self.N[yr] = xr

DS = DisjointSetNaive(10)
DS.union(4,7)
DS.union(1,7)
print DS.findSet(7)
