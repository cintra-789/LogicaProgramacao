#Olá {nome do fulano}, seja bem vindo!
""" Descobri que você tem {peso do fulano}
Seu peso é: {peso do fulano}
Sua altura é: {altura do fulano}
 Seu IMC é: {IMC do fulano}"""
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / altura * altura
print("Olá ",nome," seja bem vindo!\n","Descobri que você tem ",idade,"\n","Seu peso é: ",peso,"\n","Sua altura é:",altura,"\n","Seu IMC é: ",imc)
