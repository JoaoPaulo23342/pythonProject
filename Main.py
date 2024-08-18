import os
name = [{'nome': 'Praça', 'categoria': 'Self-service', 'ativo': False},
        {'nome': 'MozosPizza', 'categoria': 'pizzaria', 'ativo': True}]
def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    
    print('𝙾 𝙰𝙿𝙻𝙸𝙲𝙰𝚃𝙸𝚅𝙾 𝙵𝙾𝙸 𝙵𝙸𝙽𝙰𝙻𝙸𝚉𝙰𝙳𝙾 𝙲𝙾𝙼 𝚂𝚄𝙲𝙴𝚂𝚂𝙾')

def error():
    print("Error 404\n")
    retorna()
def retorna():
    input("Digite algo para voltar ao menu principal ")
    main()

def get_restaurante():
    os.system('cls')
    print('Listando os restaurantes\n')
    
    for names in name:
        print(f'.{names}\n')

    retorna()


def login_restaurante():
    os.system('cls')
    print('cadastro de novos restaurantes')
    name_of = input("digite o nome do restaurante:  ")
    name.append(name_of)
    print(f"O seu {name_of} foi cadastrado no sistema com sucesso")
    retorna()
    

    

def escolher_opcao():
    try: 
        option = int(input('Escolha uma opção: '))
        option = int(option)

        if option == 1: 
            login_restaurante()
        elif option == 2: 
            get_restaurante() 
        elif option == 3: 
            print('Ativar restaurante')
        elif option == 4: 
            finalizar_app()
        else: 
            error()
    except:
        error()
        

        

def main(): 
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    

if __name__ == '__main__':
    main()








