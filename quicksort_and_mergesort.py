def quicks(L = [12, 4, 5, 8, 1, 9, 3, 5]):
    if not L:
        return []
    
    less = quicks([e for e in L if e < L[0]])
    equal = [e for e in L if e == L[0]]
    greater = quicks([e for e in L if e > L[0]])

    return less + equal +  greater

print quicks()

def mergesort(L = [12, 4, 5, 8, 1, 9, 3, 5]):

    def merge(A, B):
        print A, B
        i = 0
        j = 0
        result = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                result.append(A[i])
                i+=1
            else:
                result.append(B[j])
                j+=1
        #print result
        return result + A[i:] + B[j:]
    
    #print L
    
    if len(L) <= 1:
        return L

    mid = int(len(L)/2)
    return merge(mergesort(L[:mid]), mergesort(L[mid:]))

print mergesort()
