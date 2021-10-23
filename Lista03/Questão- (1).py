n1 = str(input("Por favor digite um texto 1:"))
n2 = str(input("Por favor digite um texto 2:"))

print("Anagramas !" if sorted(n1) == sorted(n2) else "Não são anagramas!")
