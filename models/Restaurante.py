from models.avaliacao import Avaliacao

class restaurante:
    restaurantes = []

    def __init__(self, name, category):
        self._name = name
        self.category = category.upper()
        self._true = False
        self._avaliacao = []
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
    
    def get_avaliacao(self, cliente, nota):
        Avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(Avaliacao)
    
    def AVG_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(Avaliacao._nota for avaliacao in self._avaliacao)
        quantidade = len(self._avaliacao)
        media = round(soma_das_notas / quantidade,1)
        return media






