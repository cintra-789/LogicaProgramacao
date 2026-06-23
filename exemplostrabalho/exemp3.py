
#O que são funções
def ola(nome):
    saudação = f"Olá {nome}!"
    return saudação

saudacao = ola(input("Digite o seu nome: "))
print(saudacao)

# a e b são parâmetros da função soma
def soma(a,b):
    resultado = a + b
    return resultado
#retorno e o return, retornando o resultado calculado

#Modularização
import modulo
resultado = modulo.soma(5,6)
resultado1 = modulo.multi(2,3)
print(resultado)
print(resultado1)

#Código de linha
"""
Código de bloco
tudo aqui digitado é 
ignorado pelo python
"""


