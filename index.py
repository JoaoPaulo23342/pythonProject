from models.Restaurante import restaurante
import os
restaurante_rua = restaurante('rua', 'Gourmet')
restaurante_rua.get_avaliacao('gui', 10)
restaurante.get_avaliacao("joao", 4)


def main():
        os.system('cls')
        restaurante.listar_restaurantes()
        
        
        


if __name__ == '__main__':
          main()