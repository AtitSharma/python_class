class Product:
    def __init__(self,name,price):
        self.name=name
        self.__price=price
        
    @property   
    def price(self):
        return self.__price
    
        
    @price.setter
    def price(self,price):
        if price>0:
            self.__price=price
            
            
tsirt=Product("Tsirt",500)
jacket=Product("Jacket",1000)
# print(tsirt.name)
# print(tsirt._Product__price)
print(tsirt.price)
tsirt.price=10
print(tsirt.price)