def factorial(num):
    if num==1:
        return 1
    return num * factorial(num-1)
# print(factorial(5))
def Multiplication(num,x=0):
    if x==11:
        return 
    print(f"{num} x {x} = {num*x}")
    return Multiplication(num,x+1)
# Multiplication(9)
def expo(num,power):
    if power==0:
        return 1
    return num * expo(num,power-1)
print(expo(2,2))


    