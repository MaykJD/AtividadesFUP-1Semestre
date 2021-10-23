val_1 = int(input("Entre com um valor : "))
val_2 = int(input("Entre com outro valor : "))

def cubo (n:int):
    return n**3 

def somatoria(a:int, b:int, f:"função")->int :
    if a <= b:
        return f(a) + somatoria(a +1 , b , f)
    else:
        return 0
    

print(somatoria(val_1, val_2, cubo))