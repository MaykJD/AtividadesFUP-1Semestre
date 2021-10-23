input_txt = input("Sequençia :")
#ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT

a = input_txt.count("A")
c = input_txt.count("C")
g = input_txt.count("G")
t = input_txt.count("T")

resul = ((g+c) / (a+t+g+c)) * 100

print(f"{resul:.1f}%")

