# def Calculator():
#     def addition(num1,num2):
#         print(num1+num2)
#     return addition
# add=Calculator()
# # add(9,0)
def Calculator(operator):
    def addition(a,b):
        return a+b
    def difference(a,b):
        return a-b
    def product(a,b):
        return a*b
    if operator=="+":
        return addition
    elif operator=="-":
        return difference
    elif operator=="*":
        return product

a=Calculator("+")
# print(a(20,10))



# Closure
def increment(num):
    def factor(val):
        return num+val
    return factor
i=increment(20)
# print(i(40))
# print(i(10))


def welcome(name):
    print(f"Welcome {name}")


def bye_bye(name):
    print(f"Bye Bye {name}")
    
def greet(funct):
    funct("Ram")

greet(bye_bye)
# bye_bye("Ram")







        
    

