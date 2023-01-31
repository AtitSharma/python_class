class ProductPriceError(Exception):
    pass

class Product:
    def __init__(self,name,price):
        self.name=name
        self.__price=price
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,price):
        if price <=0:
            raise ProductPriceError("Cannot be zero")
        self.__price=price
      
p=Product("Tshirt",600)
try:
    p.price=-1
    print(f"The price before exception was {p.price}")
except ProductPriceError as msg:
    print(msg)
    print(f"The price After exception was {p.price}")