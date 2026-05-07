"""
[] = Lista -> inteiros/textuais/logicos
{} = Dicionario
() = Tupla/const
"""
#NOTE - NOTE = comentando para o code dar certo
import os
lista = ['gomes','fulano','cicrano','beltrano','colega','arthur']

#NOTE - print(lista)

# imprimindo valor especifico da lista
print(lista[0])

# imprimindo ultimo valor da lista
print(lista[-1])

# imprimindo intervalo
print(lista[0:3])

# ordernar a lista (alfabetica)
#NOTE - lista.sort()

# adicionando na lista
lista.append('karython')

# inserindo em posição especifica
lista.insert(2, 'joao')

# inserindo varios valores
lista.extend(['ana','beatriz','davi','david','roberto'])

numeros = []

# adicionando valores de forma dinamica
for i in range(10):
    numeros.append(i * 2)
#print(numeros)


#NOTE -  for i in range(len(lista)):
#     print(f'{i+1}° nome da lista: {lista[i]}')

# removendo item da lista
print(f'Lista antes de remover {lista}')

# pop - remove pelo indice
lista.pop(0)

# removendo o ultimo indice
lista.pop()

# removendo pelo valor (remove a primeira ocorrencia)
lista.remove('cicrano')

print(f'Lista depois de remover {lista}')

# range com um numero e um 1 na frente, começa pelo indice 1 e não pelo 0
lista_numeros = [ n for n in range(1,11)]

# removendo intervalo de valores
print(f'Lista antes de remover {lista_numeros}')

del lista_numeros[2:4]

print(f'Lista depois de remover {lista_numeros}')

#alterando valore de lista
listanomes = ['gomes','fulano','cicrano','beltrano','colega','arthur']
listanomes[1] = 'lucas'

print(listanomes)

numero = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numero)):
    if numero[i] > 5:
        numero[i] = numero[i] * 2
print(numero)

# list compreheision
numero = [n * 2 if n > 20 else n for n in numero]
print(numero)
