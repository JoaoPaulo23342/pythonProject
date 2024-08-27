from menu.Item_menu import ItemMenu

class Beverage(ItemMenu):
          def __init__(self,name,price,size):
                  super.__init__(name,price)
                  self.size = size