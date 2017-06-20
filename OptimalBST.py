'''
This Implementation in giving some error, code by Samarth
'''
def OBST(P):
    n = len(P)
    R = [[0 for i in range(0,n+1)] for j in range(0,n+2)]
    C = [[0 for i in range(0,n+1)] for j in range(0,n+2)]

    for i in range(1,n):

        ## Initialization
        C[i][i-1] = 0
        C[i][i] = P[i]
        R[i][i] = i
        C[n+1][n] = 0

    for d in range(1,n):
        for i in range(1,n-d+1):
            j = i + d
            minval = 9999
            kmin = -1
            
            for k in range(i,j+1):
                if (C[i][k-1] + C[k+1][j]) < minval:
                    minval = (C[i][k-1] + C[k+1][j])
                    kmin = k
            R[i][j] = kmin
            cost = P[i]
            for s in range(i+1,j):
                cost += P[s]

            ## Main part
            C[i][j] = minval + cost

##    print(C)
##    print(R)
    return C[1][n],R[1][n]



comp,root = OBST([0.1,0.2,0.4,0.3])

print(root)
print(comp)
