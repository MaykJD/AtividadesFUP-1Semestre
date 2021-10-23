def constroi_vocabulario(frase: str) -> None:
    d1 = {}
    for i in frase.split(' '):
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    print(f'Palavras: {d1}')
    d2 = {}
    for x in frase:
        if x not in d2:
            d2[x] = 1
        else:
            d2[x] += 1
    print(f'Letras:: {d2}')
    
if __name__ == '__main__':
   constroi_vocabulario('isso e um teste az teste isso')