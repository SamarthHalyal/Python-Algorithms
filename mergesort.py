import math
def mergesort(b,c,a):
    if len(a) > 1:
        #partition first-half
        for i in range(0,int(math.floor(len(a)/2))):
            b.append(a[i])
        #partition second-half
        for j in range(int(math.floor(len(a)/2)),len(a)):
            c.append(a[j])
        #print b and c
        print("SUB ARRAYS,",b,c)
        #recursive mergesort first-half
        mergesort([],[],b)
        #recursive mergesort second-half
        mergesort([],[],c)
        merge(b,c,a)
        print("FULL ARRAY,",a)

def merge(b,c,a):
    i = 0
    j = 0
    k = 0
    while i < len(b) and j < len(c):
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1

    if i < len(b):
        for l in  range(i,len(b)):
            a[k] = b[l]
            k += 1
    if j < len(c):        
        for l in  range(j,len(b)):
            a[k] = b[l]
            k += 1

array = [10,9,8,7,6,5,4,3,2,1]
mergesort([],[],array)
print(array)    
