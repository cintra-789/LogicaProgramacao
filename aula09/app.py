"""
Sistema de veiculos - em json
"""

import os
import time
import json

ARQUIVO = 'carro.json'

# carrega o arquivo

if os.path.exists(ARQUIVO):
    with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
        carros = json.load(arquivo)
else:
    carros = []

# Descobrir o ID
if carros:
    proximo_id = max(carro['id'] for carro in carros) + 1
else:
    proximo_id = 1

os.system("cls")

while True:
    print("===== Sistema de Carros 🚗 =====")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("3 - Atualizar carro")
    print("4 - Deletar carro")
    print("0 - Sair")

    opcao = input('Escolha a sua opção: ')
    #create
    if opcao == "1":
        modelo = input('Digite o modelo do carro: ').title()
        preco = float(input ('Digite o preço do carro: ').replace(",", "."))
        marca = input('Digite a marca do carro: ').title()

        carro = {
            'id'      : proximo_id,
            'modelo'  : modelo,
            'preco'   : preco,
            'marca'   : marca   
        }

        carros.append(carro)
        with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
            json.dump(carro, arquivo, indent=4, ensure_ascii=False)
        proximo_id += 1

        print("Carro cadastrado com sucesso! ✅")
    elif opcao == "2":
        os.system("cls")

        if not carros:
            print("Nenhum veiculo cadastrado")
        
        else:
            print("\n📑 Lista de veiculos")

            for carro in carros:
                print(
                    f'ID: {carro['id']} |'
                    f'Modelo: {carro[modelo]} |'
                    f'Preço: {carro['preco']} |'
                    f'Marca: {carro['marca']} '
                )
    elif opcao == "3":
        os.system("cls")

        if not carros:
            print("Nenhum carro encontrado")
            continue
    

        print("\n📑 Lista de veiculos")

        for carro in carros:
                print(
                    f'ID: {carro['id']} |'
                    f'Modelo: {carro[modelo]} |'
                    f'Preço: {carro['preco']} |'
                    f'Marca: {carro['marca']} '
                )
        id_busca = int(input('Digite o ID do carro para atualizar: '))

        encontrado = False

        for carro in carros:
            if carro['id'] == id_busca:
                novo_modelo = input('Digite o novo modelo: ').title()
                novo_preco = float(input('Digite o novo preço: ').replace(",","."))
                nova_marca = input('Digite o novo marca: ').title

                with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
                    json.dump(
                        carros,
                        arquivo,
                        indent=4,
                        ensure_ascii=False
                    )
                    print("Carro atualizado com sucesso!")
                    encontrado=True
                    break
            if not encontrado:
                print("Carro não encontrado!")
    elif opcao == "4":
        os.system("cls")

        if not carros:
            print("Nenhum carro encontrado")
            continue
    

        print("\n📑 Lista de veiculos")

        for carro in carros:
                print(
                    f'ID: {carro['id']} |'
                    f'Modelo: {carro[modelo]} |'
                    f'Preço: {carro['preco']} |'
                    f'Marca: {carro['marca']} '
                )
        id_busca = int(input('Digite o ID do carro para atualizar: '))

        encontrado = False

        for carro in carros:
            if carro['id'] == id_busca:
                novo_modelo = input('Digite o novo modelo: ').title()
                novo_preco = float(input('Digite o novo preço: ').replace(",","."))
                nova_marca = input('Digite o novo marca: ').title

                with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
                    json.dump(
                        carros,
                        arquivo,
                        indent=4,
                        ensure_ascii=False
                    )
                    print("Carro atualizado com sucesso!")
                    encontrado=True
                    break
            if not encontrado:
                print("Carro não encontrado!")


    

