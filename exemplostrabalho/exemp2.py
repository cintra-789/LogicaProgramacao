#Entrada de dados
nome = input('Digite o seu nome: ')
idade = input("Digite a idade que fez ou irá fazer em 2026: ")

#Processamento de dados
idade_num = int(idade)
data_nascimento = 2026 - idade_num

#Saída de dados
print(f"Olá {nome}! Você nasceu no ano de {data_nascimento}.")

