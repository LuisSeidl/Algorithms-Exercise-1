import random
import timeit

class Matrix():
    
    def __init__(self,m,n):
        self.zeilen = m
        self.spalten = n
        self.values = [[0]*self.spalten for _ in range(0,self.zeilen)]
        
        
    def __str__(self):
        return "\n".join([" ".join(map(str, self.zeilen)) for self.zeilen in self.values])
    
    
    def RandomFill(self,min=0,max=100):
        for z in range(0,self.zeilen):
            for s in range(0,self.spalten):
                self.values[z][s] = random.randint(min,max)
                
                
    def Input(self):
        for z in range(0,self.zeilen):
            for s in range(0,self.spalten):
                print("Value at: [" + str(z) + "][" + str(s) + "] :")
                self.values[z][s] = input()
    
    
    
    def Add(self, other):
        if not isinstance(other,Matrix) or self.spalten != other.spalten or self.zeilen != other.zeilen:
            print("Matrizes don't have the same Dimensions")
            return 0
        
        result = Matrix(self.zeilen,self.spalten)
        counter = 0
        start = timeit.default_timer()
        
        for z in range(0,self.zeilen):
            for s in range(0,self.spalten):
                counter += 1
                result.values[z][s] = self.values[z][s] + other.values[z][s]
        
        stop = timeit.default_timer()
        time = int((stop-start)*1000)
        
        print("Addition of " + str(self.zeilen) + "x" + str(self.spalten) + " Matrices took " + str(counter) + " operations and " + str(time) + "ms" + "(="+ str(time/1000)+")s")
        return result
        
        
    def Mult(self, other):    
        if not isinstance(other,Matrix) or self.spalten != other.zeilen:
            print("Matrizes not Suitable for Multiplikation")
            return 0
        
        counter = 0
        start = timeit.default_timer()
        
        result = Matrix(self.zeilen,self.spalten)
        for z in range(0,self.zeilen):
            for s in range(0,self.spalten):
                counter +=1
                result.values[z][s] = sum(self.values[z][k] * other.values[k][s] for k in range(self.spalten))
                
                
        stop = timeit.default_timer()
        time = (stop-start)*1000
        
        print("Multiplikation of " + str(other.zeilen) + "x" + str(self.spalten) + " Matrices took " + str(counter) + " operations and " + str(time) + "ms" + "(="+ str(round(time/1000,2))+")s")
        return result
    
    
    
quadrat_size = 26000
matrix = Matrix(quadrat_size,quadrat_size)

M = Matrix(quadrat_size,quadrat_size)

C = matrix.Add(M)

# Multiplikation 1 min: 880
# Multiplikation 2 min: 1100
# Multiplikation 5 min: 1450
# Multiplikation 10 min: 1800

# Addition 1 min: 23670
# Addition 2 min: 34000
# Addition 5 min: 50775
# Addition 10 min: 70520