from models.avaliacao import Avaliacao

class restaurante:
    restaurantes = []

    def __init__(self, name, category):
        self._name = name
        self.category = category.upper()
        self._true = False
        self.avaliacao = []
        restaurante.restaurantes.append(self)

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_category(self):
        return self.category

    def set_category(self, value):
        self.category = value

    def get_true(self):
        return self.true
    
    

    def set_true(self, value):
        self.true = value

    def __str__(self):
        return f'{self._name} | {self._category}'

    @classmethod
    def listar_restaurantes(cls):
        print(f"{( 'Nome do restaurante'.ljust(25) )} | {( 'categoria'.ljust(25) )} | {'Status'}")
        for restaurantex in cls.restaurantes:
            print(f'{restaurantex._name.ljust(25)} | {restaurantex.category.ljust(25)} | {restaurantex.true}')

    @property
    def true(self):
        return 'true✅' if self._true else 'false❌'
    
    def switch_state(self):
        self._true = not self._true
    
    

restaurante_praca = restaurante('Praca', 'Gourmet')
restaurante_pizza = restaurante('pizza', 'italiana')
restaurante_praca.switch_state()
restaurante_praca.category = 'Gourmet'
restaurante.set_category = 'gourmet'
restaurante_pizza.switch_state()

restaurante.listar_restaurantes()


