def Welcome():
    print("Welcome everyone")
    



def welcome1(name,address):#parameter
    print("Welcome ",name)
    print("Your Address :",address)


# name=input('Enter Your Name  ')
# address=input('Enter Your address  ')
# welcome1(name,address)#arguments


# a=10
# b=20
# print("The sum of {0} and {1} is {2}".format(a,b,a+b))
# print(f"The sum of {a} and {b} is {a+b}")



def Profile(name,address,contact,weight=70):
    print(f"The name is : {name}")
    print(f"The address is : {address}")
    print(f"The contact is : {contact}")
    print(f"The weight is : {weight}")

# Profile("Ram","Ktm",123)


# Profile(name="Ram",contact=123,address="Ktm")



# def Add(num1,num2=1):
#     return num1+num2
    
# print(Add(10,20))
# print(Add(10))


def Sub(num1,num2):
    return num1-num2
    
def Product(num1,num2):
    print(num1*num2)

# print(Product(2,7))
# print(Sub(5,2))
    
    
    
def Multiple_ard(*a):
    return a
print(Multiple_ard(1,2,3,4,5,6,7,"Python",9))





  