"""
1. Crie um programa que o usuario possa digitar quantos numeros quiser e ao terminar imprima a lista em ordem crescente
2. Crie um programa que o usuario possa digitar a quantidade desejada de notar de um determinado aluno (nota minima 0 e maxima 10) e o programa calcula a media desse aluno,
 e ao final imprima se o aluno esta (aprovado => 7, reprovado, recuperação >=5)
"""

print('Programa de boletim escolar')
notas = []
while True:
    nota = float(input("Digite a nota do aluno: "))
    if nota > 10:
        print("Nota inválida")
        break
    else:
        notas.append(nota)
    print(notas)
    cont = input("Deseja digitar uma nota? (Enter para continuar / n - Não)\n").lower()

    if cont == 'n':
        break

med = sum(notas) / len(notas)

if nota > 10:
        print("Impossivel calcular a media")
else: 
    print(f"A media do aluno é: {med:.1f}")
    if med >= 7:
            print("O aluno está aprovado!")
    elif med >= 5:
         print("O aluno está de recupeção!")
    else:
            print("O aluno está reprovado!")
            