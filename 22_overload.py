class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    def __str__(self):
        return self.name
    
    def __eq__(self, obj):
        return self.price==obj.price
    
    def __add__(self,obj):
        return self.price+obj.price
    
    def __mul__(self,obj):
        if isinstance(obj,Product):
            return self.price * obj.price
        elif isinstance(obj,int):
            return self.price * obj
        
    
tshirt=Product("Tshirt",100)
pant=Product("Pant",200)
        
print(tshirt+pant)
print(tshirt*pant)