# Inputs
tempo_decorrido_hora = float(input("Digite quantas horas o carro ficou : \n" )) 
tempo_decorrido_min = float(input("Digite quantas minutos o carro ficou :\n" )) 
# Tempo de permanencia
def bb(h:float, m:float):
    if h == 1 and 59 >= m >= 0:
        return 2+(2/60 * m)
    elif h == 2 and 59 >= m >= 0:
        return 2+1.5 +(1/60*m)
    else:
        return 2+1.5+(h*1+(1/60*m))
    
print(f"O valor a pagar é -> {round (bb(tempo_decorrido_hora ,tempo_decorrido_min), 2)} R$ ")   