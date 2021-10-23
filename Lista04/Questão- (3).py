n1 = int(input("Digite um numero : "))

def teste(n: int ,count=0 )-> int:
    if n == 1:
        return count
    if n % 2 == 0:
        num = n / 2
        return teste(num, count +1)
    else:
        num = (n*3+1)/2
        return teste(num, count +1)
    
if __name__ == "__main__":    
    print (teste(n1))


 