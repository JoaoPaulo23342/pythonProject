from models.Main import restaurante

restaurante_rua = restaurante('rua', 'Gourmet')
restaurante_mexicano = restaurante('mexican Food', 'Nachos')
restaurante_mexicano.switch_state()
restaurante_rua.switch_state()

def main():
        restaurante.listar_restaurantes


if __name__ == '__main__':
          main()