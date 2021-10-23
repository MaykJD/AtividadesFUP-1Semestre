n1 = str(input("Por favor digite um texto 1:"))
n2 = str(input("Por favor digite um texto 2:"))

def subSequencia() -> bool:    
    n1_l = len(n1)
    n2_l = len(n2)
    ix1 = 0
    ix2 = 0 
    while ix1 < n1_l and ix2 < n2_l:
        if n1[ix1] in  n2[ix2]: 
            ix1 += 1
        ix2 += 1
    return ix1 == n1_l

print(f"{n1} È uma subsequencia de {n2}" if subSequencia() == True \
 else f"{n1} Não é uma subsequencia de {n2}")
