import os
os.system("cls")
num1 = float(input("Me diga um número para a comparação: "))
num2 = float(input("Me diga um novo número para prosseguir com a comparação: "))
resul = "num1 é maior" if num1 > num2 else "num1 e menor"
print(resul)