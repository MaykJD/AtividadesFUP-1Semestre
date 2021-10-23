#Triangulo 1 inferior esquerda OBJ1
Lx_0 = int(input('Olá Digite a cord Triangulo 1° :'))
Ly_0 = int(input('Olá Digite a cord Triangulo 1° :'))
#Triangulo 1 superior direita
Rx_1 = int(input('Olá Digite a cord Triangulo 1° :'))
Ry_1 = int(input('Olá Digite a cord Triangulo 1° :'))

#Triangulo 2 inferior esquerda OBJ2
Lx_2 = int(input('Olá Digite a cord Triangulo 2° :'))
Ly_2 = int(input('Olá Digite a cord Triangulo 2° :'))
#Triangulo 2 inferior esquerda
Rx_3 = int(input('Olá Digite a cord Triangulo 2° :'))
Ry_3 = int(input('Olá Digite a cord Triangulo 2° :'))

def cruza():
    intc_Obj1_Obj2 = Lx_0 < Lx_2 or Ly_0 > Ly_2 and Rx_1 < Rx_3 or Ry_1 > Ry_3
    print(intc_Obj1_Obj2)
cruza()

#[0,0,2,2],[1,1,3,3]          (l1.y <= r2.y    or    l2.y <= r1.y):
#(R1[0]>=R2[2]) or (R1[2]<=R2[0]) #or (R1[3]<=R2[1]) or(R1[1]>=R2[3]):
#Algoritmo AABB para detecção de colisões
