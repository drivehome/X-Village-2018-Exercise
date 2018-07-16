class map:

    def set_map(self,n):
        self.x=[]
        for j in range(0,n):
            y=["*"]*n
            self.x.append(y)
        return self.x    

    def set_pattern(self,n,p):
        if p == 1:
            self.x[(n-1)//2-1][(n-1)//2-1]=0
            self.x[(n-1)//2-1][(n-1)//2]=0
            self.x[(n-1)//2-1][(n-1)//2+1]=0
            self.x[(n-1)//2][(n-1)//2-1]=0
            self.x[(n-1)//2+1][(n-1)//2]=0

    def display(self):
        for row in self.x:
            for col in row:
                print(col, end=" ")
            print("")
        
c=map()
c.set_map(7)
c.set_pattern(7,1)
c.display()