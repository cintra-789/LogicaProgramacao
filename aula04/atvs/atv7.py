#7- Solicite dois números e verifique se o segundo é menor que o primeiro
num1 = input("Digite um numero: ")
num2 = input("Digite o segundo numero: ")

num1 = int(num1)
num2 = int(num2)

if num2 > num1:
    print("O segundo numero e maior que o primeiro.")
else:
    print("O segundo numero e menor que o primeiro.")