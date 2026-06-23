'''
    Sistema de veículos - em json
'''

import os
import time
import json

ARQUIVO = 'carros.json'

#carrega o arquivo

if os.path.exists(ARQUIVO):
    with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
        carros = json.load(arquivo)
else:
    carros = []

    #descobrir o ID
if carros:
    proximo_id = max(carro['id'] for carro in carros) +1
else:
    proximo_id = 1

os.system('cls')

while True:
    print("\n----------------- Sistema de carros 🚗 -----------------")
    print('1. cadastrar carros')
    print('2. listar carros')
    print('3. Atualizar carros')
    print('4. deletar carros')
    print('0. sair')

    opcao = input("Escolha uma opção: ")
     #criar
    if opcao == '1':
        modelo = input("Digite o modelo do carro: ").title()
        preco = float(input('Digite o preço do carro: '))
        marca = input("Digite a marca: ").title()

        carro = {
            "id": proximo_id,
            "modelo": modelo,
            "preço": preco,
            "marca": marca
        }

        carros.append(carro)

        with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
            json.dump(carros, arquivo, indent=4, ensure_ascii=False)

        proximo_id +=1

        print('Dados cadastrados com sucesso! ✅')

    elif opcao == '2':
        os.system ('cls')

        if not carros: 
            print('Nenhum carro cadastrado!❌')

        else: 
            print('\n 📋Lista de carros')

            for carro in carros: 
                print(
                    f'ID: {carro['id']} |'
                    f'Modelo: {carro['modelo']} |'
                    f'Preço: {carro['preço']} |'
                    f'Marca: {carro['marca']} |'
                )

    elif opcao == '3':
        os.system('cls')

        if not carros:
            print('Nenhum carro cadastrado!❌')
            continue
        print('\n 📋Lista de carros')
        for carro in carros:
            print(
                    f'ID: {carro['id']} |'
                    f'Modelo: {carro['modelo']} |'
                    f'Preço: {carro['preço']} |'
                    f'Marca: {carro['marca']} |'
                )
        id_busca = int(input('Digite o ID do carro para atalizar: '))

        encontrado = False
        for carro in carros:
            if carro['id'] == id_busca:
                novo_modelo = input("Digite o novo modelo: ").title()
                novo_preco = float(input("Digite o novo preço: ").replace(',', '.'))
                novo_marca = input("Digite a nova marca: ").title()

                with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
                    json.dump(
                        carros,
                        arquivo, 
                        indent=4, 
                        ensure_ascii=False
                        )
                    print('Carro atualizado com sucesso!✅')
                    encontrado = True
                    break

            if not encontrado: 
                print('Carro não encontrado❌')

    elif opcao == '4':
        os.system('cls')

        if not carros:
            print('Nenhum carro cadastrado!❌')
            continue
        print('\n 📋Lista de carros')
        for carro in carros:
            print(
                    f'ID: {carro['id']} |'
                    f'Modelo: {carro['modelo']} |'
                    f'Preço: {carro['preço']} |'
                    f'Marca: {carro['marca']} |'
                )
        id_busca = int(input('Digite o ID do carro para deletar: '))

        encontrado = False
        for carro in carros:
            if carro['id'] == id_busca:
                carros.remove(carro)

                with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
                    json.dump(
                        carros,
                        arquivo, 
                        indent=4, 
                        ensure_ascii=False
                        )
                    print('Carro deletado com sucesso!✅')
                    encontrado = True
                    break

            if not encontrado: 
                print('Carro não encontrado❌')        

    #Sair
    elif opcao == '0':
        total = 10
        barra = ""
        print('Saindo do sistema...')
        for i in range(total + 1):
            barra += "🟩"
            porcentagem = int((i / total *100)) 
            vazio = "-" * (total-1)
            print(f'\r[{barra}] {porcentagem}%', end='')
        time.sleep(0.3)
        break
    else: 
        print('❌Opção inválida.')    