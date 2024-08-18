import os


list = ['BMW', 'Tesla', 'Mercedes']


def menu():
    print('Store Car')
    print('1-Adicione o carro no carrinho')
    print('2-Carrinho de compras')
    print('3-Deletar carro do carrinho')
    print('4-Sair')


def sair():
    os.system('cls')
    print("Saindo...")
def error():
    print("ERRO 404")
    voltar()


def limpando():
    os.system('cls')


def carrinho():
    limpando()
    print('Lista dos seus produtos no carrinho de compras\n')

    for listas in list:
        print(f'Marca do carro: {listas}')
    voltar()


def voltar():
    input('digite algo para voltar ao menu principal:  ')
    main()


def car_delete():
    os.system('cls')
    remove = input(
        'digite a marca do carro que vc quer excluir do seu carrinho')
    indice_do_carro = list.index(remove)
    list.pop(indice_do_carro)
    print(f'o seu carro com marca {remove} foi excluido do carrinho')
    voltar()


def car_buy():
    os.system('cls')
    name_of = input('Digite a marca do carro que vc quer:  ')
    list.append(name_of)
    print(f"o seu carro com marca {name_of} foi adicionado ao carrinho")
    voltar()


def menu_escolher():
    opcoes = input('escolha uma das opçoes a seguir ')
    opcoes = int(opcoes)
    if (opcoes == 1):
        car_buy()
    elif (opcoes == 2):
        carrinho()
    elif (opcoes == 3):
        car_delete()
    elif (opcoes == 4):
        sair()


def main():
    os.system('cls')
    menu()
    menu_escolher()


if __name__ == '__main__':
    main()
