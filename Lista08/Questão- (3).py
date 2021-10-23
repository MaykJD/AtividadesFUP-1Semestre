def adiciona_vetores(vetor1: dict, vetor2: dict) -> dict:
    v1 = {}
    for x in vetor1:
        for y in vetor2:
            if x == y:
                soma = vetor1[x] + vetor2[y]
                if x not in v1:
                    v1.setdefault(x,soma)
                else:
                    v1[x] = soma
            else:
                if x not in v1:
                    v1.setdefault(x,vetor1[x])
                elif y not in v1:
                    v1.setdefault(y,vetor2[y])
                    
    v2_final = {}
    for key in sorted(v1.keys()):
        v2_final.setdefault(key,v1[key])          
    return v2_final      

if __name__ == '__main__':
    print(adiciona_vetores({0: 1,6: 3}, {0: 2, 6: 4}))
    print(adiciona_vetores({0: 1,6: 3}, {3: 2, 8: 4}))