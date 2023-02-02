from abc import ABC,abstractmethod
# print(dir(ABC))
class Shape(ABC):  
    @abstractmethod
    def area(self):
        pass
    
class Rectange(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    
class Square(Shape):
    def __init__(self,l):
        self.l=l
        
    def Area(self):
        return self.l*self.l
    
    def area(self):
        pass 
r=Rectange(1,2)
print(r.area())
s=Square(5)
print(s.Area())

        
    
    