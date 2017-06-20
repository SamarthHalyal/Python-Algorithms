class Queens:
    def __init__(self,N):
        self.N = N
        ## Initializing our Board with #
        self.board = [['#' for i in range(N)] for j in range(N)]
        self.transitive = [[0 for i in range(N)] for j in range(N)]
        self.preP = -1
        self.preQ = -1
        self.solve()
    
    def setUnsafe(self,p,q):
        self.preP = p
        self.preQ = q

        pathP = [1,-1,0,0,1,-1,-1,1]
        pathQ = [0,0,1,-1,1,-1,1,-1]

        for m,n in zip(pathP,pathQ):
            i = p
            j = q
            while True:       
                try:
                    self.transitive[i][j] = 1
                except:
                    break
                i += m
                j += n
                
    def isSafe(self,p,q):
        if self.transitive[p][q] == 0:
            return True
        else:
            return False

    def unSetPrevious(self):
        p = self.preP
        q = self.preQ
        
        self.board[p][q] = '#'

        pathP = [1,-1,0,0,1,-1,-1,1]
        pathQ = [0,0,1,-1,1,-1,1,-1]

        for m,n in zip(pathP,pathQ):
            i = p
            j = q
            while True:       
                try:
                    self.transitive[i][j] = 0
                except:
                    break
                i += m
                j += n
        
        return p,q

    def solve(self):
        n = 0
        i = j = 0
        count = 0
        while True:

            if n == self.N:
                print("Solution Found")
                return            
            
            if self.isSafe(i,j):
                self.board[i][j] = 'Q'
                self.setUnsafe(i,j)
                i = (i) % self.N
                j = (j+1) % self.N
                n += 1
            else:
                i = (i+1) % self.N
                if i == self.N-1:
                    i,j = self.unSetPrevious()
                    i = (i+1) % self.N
                    j = (j) % self.N
                
                    n -= 1
            

for i in [1,4,5,6,7,8]:
    ## for i == 2,3 it goes for infinite loop showing that
    ## it is a NON-DETERMINISTIC ALGORITHM and hence belongs
    ## to NP (Non-deterministic problem) set  
    print("trying ",i," Queens")
    for i in Queens(i).board:
        ## print(''.join(i))
        pass
