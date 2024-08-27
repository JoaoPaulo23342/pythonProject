from modelos.restaurante import Restaurante
from menu.beverage import Beverage
from menu.plate import Plate

beverage = Beverage("suco melancia", 30.32, "700ml")

plate = Plate("Camarão", 100.21, "Camarões")


def main():
    print(plate)

if __name__ == '__main__':
    main()