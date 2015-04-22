
class Priority_Queue:
    def __init__(self, CompareFunc):
        self.Comp = CompareFunc
        self.a = []
        
    def empty(self):
        if self.a == []:
            return True
        else:
            return False

    def heapify(self, i):
        l = i*2+1
        r = (i+1)*2
        if l < len(self.a) and self.Comp(self.a[i], self.a[l]) == False:
            largest = l
        else:
            largest = i
        if r < len(self.a) and self.Comp(self.a[largest], self.a[r]) == False:
            largest = r
        if largest != i:
            self.a[i],self.a[largest] = self.a[largest],self.a[i]
            self.heapify(largest)
        
    def enqueue(self, x):
        self.a.append(x)
        i = len(self.a)-1
        j = (i-1)/2
        while i > 0 and self.Comp(self.a[i], self.a[j]) == True:
            self.a[i],self.a[j] = self.a[j],self.a[i]
            i = j
            j = (i-1)/2

    def dequeue(self):
        x = self.a[0]
        i = len(self.a)-1
        self.a[0],self.a[i] = self.a[i],self.a[0]
        del self.a[i]
        self.heapify(0)
        return x


