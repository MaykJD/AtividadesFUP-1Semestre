x = int(input('Digite um numero natural:'))
y = int(input('Digite um numero natural:'))
z = int(input('Digite um numero natural:'))

def ordena():
    n_max = max(x, y, z)
    n_min = min(x, y, z)
    meio = x + y + z - n_max - n_min
    print(f'{n_min} {meio} {n_max}')

ordena()