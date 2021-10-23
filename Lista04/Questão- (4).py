x = int(input("Digite o ponto x : "))
y = int(input("Digite o ponto y : "))

def quadrante(x,y) -> int:
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return None

if __name__ == "__main__":    
   print(quadrante(x,y))