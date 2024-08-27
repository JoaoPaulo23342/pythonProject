from menu.Item_menu import ItemMenu

class Plate(ItemMenu):
          def __init__(self, name, price, description):
                  super().__init__(name,price)
                  self.description = description