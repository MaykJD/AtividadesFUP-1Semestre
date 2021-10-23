# Importar Modulo
from modulo import *

# Main Method
if __name__ == "__main__":     
    #Testes1
    print(insert([1, 2, 3], ['a', 'b', 'c'], 2))
    print(insert("123","abc",2))
    print(insert("123456","banana",2))
    print(insert([1, 2, 3, 4,5], ['a', 'b', 'c'], 2))
    #Testes1 

    #Testes2
    print (ate_o_primeiro([1, 2, 3, 4], 3))
    print (ate_o_primeiro('abcdef', 'd'))
    print (ate_o_primeiro('bananadoce', 'c'))
    #Testes2
    
    #Testes3
    print (corta_lista([0,1,2,3,4,5,6,7,8,9], 3))
    print (corta_lista([20,30,40,50,60,70,80,], 5))
    #Testes3 