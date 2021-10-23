def imprime_matriz():
    for i in range(len(v)):
        linha = []
        for j in range(len(v)):
            coprimos = test_coprimos(v[i], v[j])
            if coprimos:
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
    
    for i in range(len(v)):
        l3.append([i])  
    print("{}".format(l3))
    
    for i in range(len(matriz)):
        print(f"v{[i]}", end='  ')            
        for j in range(len(matriz[i])): 
            print('{:>2} '.format(matriz[i][j]) , end=' ')  
        print()  
            
def test_coprimos(x: int, y: int):
    coprimos = True
    minimo = min(x,y)
    for i in range(minimo,1,-2):
        if x % i == 0 and y % i == 0:
            coprimos = False
            break
    return coprimos    


if __name__ == "__main__":
    v = []
    l3 = []
    matriz = []   
    # Pegando Values

    n = int(input('Adicionar quantos numeros? '))
    number = 0
    for q in range(n):
        number += 1
        print(f"{number}° Numero: ")
        valor = int(input(':-> '))
        v.append(valor)    

    print(imprime_matriz())                           