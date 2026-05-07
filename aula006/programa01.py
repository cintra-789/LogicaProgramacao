"""
1. Crie um programa que o usuario possa digitar quantos numeros quiser e ao terminar imprima a lista em ordem crescente
2. Crie um programa que o usuario possa digitar a quantidade desejada de notar de um determinado aluno (nota minima 0 e maxima 10) e o programa calcula a media desse aluno,
 e ao final imprima se o aluno esta (aprovado => 7, reprovado, recuperação >=5)
"""

lista_num = []
while True:
    num = float(input('Digite um numero: '))
    lista_num.append(num)
    print(lista_num)
    cont = input("Deseja digitar mais um número? (Enter para continuar / n - Não)\n").lower()

    if cont == "n":
        break

lista_num.sort()
print(f"A lista em ordem crescente é: {lista_num}")
