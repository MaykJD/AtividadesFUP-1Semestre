num1 = int(input('Digite um numero natural entre 0 e 9:'))
num2 = int(input('Digite um numero natural entre 0 e 9:'))
num3 = int(input('Digite um numero natural entre 0 e 9:'))

def soma_dos_quadrados():
    n_max = max(num1,num2,num3)
    n_min = min(num1,num2,num3)
    meio = num1+num2+num3 - n_max -n_min
    resul = meio **2 + n_max **2
    print(resul)

soma_dos_quadrados()


