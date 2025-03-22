
def primzahlen_sieb(schranke):
    alle_zahlen = [x for x in range(2,schranke+1)]
    nicht_primzahlen = []
    
    
    for i in alle_zahlen:
        j= i 
        while j <= schranke+1:
            j+=i
            if j <= schranke+1:
                nicht_primzahlen.append(j)
        
    primzahlen = [x for x in alle_zahlen if x not in nicht_primzahlen]
    return primzahlen



liste = primzahlen_sieb(10000)
for i in liste:
    print(i)
    

    
    