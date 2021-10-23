def verify_num(lista , result):
    list_map = list(map(int, lista))
    v_aux = 0
    v_aux2 = 0
    log_test = True
    for num in list_map:
        for num1 in list_map:
            if num * num1 == result and num != num1:
                v_aux = num
                v_aux2 = num1
                log_test = True
                break
            else:
                log_test = False
    if log_test:
        print(f"Resultado: {v_aux2} e {v_aux}")            
    else:
        print(f"Resultado: Não existem tais números")            
                
if __name__ == "__main__":
    lista = []
    number = 0
    n = int(input('Quantos numeros adicionar ?: '))
    for q in range(n):
        number += 1
        print(f"{number}° Numero: ")
        valor = int(input("-> "))
        lista.append(valor)
    C = int(input('Digite um numero inteiro: '))
    
    verify_num(lista,  C)