import itertools

#Iterativer Euklidischer Algorithmus
def ggT_iterativ(a,b):
    
    while True:
        if b == 0:
            return a

        r = a%b
        a = b
        b = r

        
#Rekursiver Euklidischer Algorithmus
def ggT_rekursiv(a,b):
    if b == 0:
        return a
    else:
        return ggT_rekursiv(b, a%b)
    
    
# Der Iterative Algorithmus ist besser, da rekursion ineffizienter als ein while-loop ist   
    
    
# kgV algorithmus, a*b/ggT(a,b)
def kgV(a,b):
    return int(a*b/(ggT_iterativ(a,b)))    



a_values = list()
b_values = list()

for i in range(30,41):
    a_values.append(i)
    b_values.append(i)
    
    
all_combinations = itertools.product(a_values,b_values)

for tup in all_combinations:
    print("Zahlen: "+ str(tup) +" | kgV: " + str(kgV(tup[0],tup[1])) + ", ggT: " + str(ggT_iterativ(tup[0],tup[1])) + ", Produkt: " +  str(tup[0]*tup[1]))
    
    
# Wirklich auffallen tut nichts, ausser dass umso höher der kgV, umso kleiner der ggT (was klar ist)