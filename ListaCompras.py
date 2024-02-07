"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
# importando o codigo de limpeza 
import os

#variaveis 
lista = []

####


while True:
    print('\nSelecione uma das opções')
    opcao = input('[i]nserir, [l]istar ou [a]pagar: \t')

    if opcao == 'i':
        os.system('cls')  #limpa o que estiver antes (o codigo ('cls') pode mudar de acordo com seu sistema.)
        valor = input('Insira um item a lista: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input(
            'Escolha um item para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite número int.')
        except IndexError:
            print('Índice não existente na lista')
        except Exception:
            print('Erro desconhecido...')

    elif opcao == 'l':
        os.system('cls')    #limpa o que estiver antes (o codigo ('cls') pode mudar de acordo com seu sistema.)

        if len(lista) == 0:
            print('Não a itens em sua lista. ')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por Favor, escolha um das opções existentes: [i]nserir, [l]istar ou [a]pagar: ')
