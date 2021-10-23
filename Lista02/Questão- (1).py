import math
pi = math.pi

raio = float(input('Olá Digite um valor :'))

#se raio menor que 0 e raio menor que 10000.0


def circunferencia():
    c = float(round(2 * pi * raio ,2))
    return(f'{c}')

def area():
    a = float(round(pi * raio**2 ,2))
    return(f'{a}')

print(circunferencia(),area())

