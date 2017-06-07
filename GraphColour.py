class GraphColoring:
    def __init__(self,G,m,n):
        self.G = G
        self.m = m
        self.n = n
        self.x = [0 for i in range(n)]
        for i in range(self.n):
            self.graphCol(i)
    
    def graphCol(self,k):
        for c in range(1,self.m+1):
            if(self.isSafe(k,c)):
                self.x[k] = c
                if k+1 < self.n:
                    self.graphCol(k+1)
                else:
                    print(self.x)
                    return

    def isSafe(self,k,c):
        for i in range(self.n):
            if self.G[k][i] == 1 and c == self.x[i]:
                return False
        return True

GraphColoring([[1,1,0,0,1,1,0,0,0,0],
               [1,1,1,0,0,0,1,0,0,0],
               [0,1,1,1,0,0,0,1,0,0],
               [0,0,1,1,1,0,0,0,1,0],
               [1,0,0,1,1,0,0,0,0,1],
               [1,0,0,0,0,1,0,1,1,0],
               [0,1,0,0,0,0,1,0,1,1],
               [0,0,1,0,0,1,0,1,0,1],
               [0,0,0,1,0,1,1,0,1,0],
               [0,0,0,0,1,0,1,1,0,1]],3,10)

    
    
