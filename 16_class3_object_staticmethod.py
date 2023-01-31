class Calculator:
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
        
    def add(self):
        return self.a+self.b
    
    def diff(self):
        return self.a-self.b
    
    def product(self):
        return self.a*self.b
    
    def division(self):
        self.a/self.b
        
    @staticmethod
    def square_root(num):
        return num**0.5
    
    
    
    
    
    
    
    
    
c=Calculator(10,20)
print(c.add())
print(c.square_root(25)) #Static Method
# print(Calculator.square_root(25))   #Static Method

