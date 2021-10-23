def converte_vetor(vetor: list) -> dict:
    d1 = {}
    for i in range (len(vetor)):
        if vetor[i] != 0:
            d1[i] = vetor[i]
    return d1    
    
if __name__ == '__main__':
    print(converte_vetor([1, 0, 0,0, 0, 0, 3, 0, 0, 0]))
