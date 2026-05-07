"""
    Manipulação de arquivos: percorrer os meus diretorios, encontrar o arquivo
    passar o comando de abertura de arquivo, passar comando de ação.

    arquivo = open("arquivo.txt","modo")

    modos de ação:
        - "r" : leitura do arquivo
        - "w" : escrita(sobrescreve o conteúdo do antigo)
        - "a" : append/adiciona conteúdo (r,w,a," Os mais usados")
        - "x" : criar um arquivo
        - "b" : arquivos binários
        - "t" : texto
"""
# Criando e escrevendo arquivo
arquivo = open('primeiro_arquivo.txt',"w")
arquivo.write('Ola mundo! meu primeiro arquivo')
arquivo.close()

# lendo arquivo
arquivo = open('primeiro_arquivo.txt','r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# aplicando boa pratica
with open("primeiro_arquivo.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# arquivo com multiplas escritas
with open('alunos.txt',"a") as arquivo:
    arquivo.write('Ana\n')
    arquivo.write('Bruna\n')
    arquivo.write('Joao\n')
    arquivo.write('Lucas\n')
    arquivo.write('Arthur\n')
    arquivo.write('Cintra\n')

# lendo linha a linha
with open('alunos.txt','r') as arquivo:
    for linha in arquivo:
        print(linha)

# usando lista para escrever no arquivo
frutas = ['melancia','pinha','manga','mexirica','morango']

with open('frutas.txt','w') as arquivo:
    for f in frutas:
        arquivo.write(f + '\n')

# converter o arquivo em uma lista
with open('frutas.txt','r') as arquivo:
    linhas = arquivo.readlines()

print(type(linhas))
print(linhas)

# SAIDA : ['melancia\n', 'pinha\n', 'manga\n', 'mexirica\n', 'morango\n']

# limpar a quebra de linha

with open('frutas.txt','r') as arquivo:
    for linha in arquivo:
        print(linha.strip())


# exemplo para cadastro

while True:
    nome = input("Digite o seu nome: ").title()

    with open("cadastro.txt",'a') as arquivo:
        arquivo.write(nome + "\n")
    
    sair = input('Deseja sair do sistema? s/n').lower()

    if sair == 's':
        break