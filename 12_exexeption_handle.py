# num1=int(input())
# num2=int(input())
# print(f"Sum is {num1+num2}")




# name=input("Enter the name")
# print(name)



# try:
#     #Block of code
# except Exception :
#     #Block of code
# except ValueError:
#     #Block of code
# except ZeroDivisionError:
#     #Block of code
# else:
#     #Block of code
# finally:
#     #Block of code
    
    
    
    
try:
    a=int(input())
    b=int(input())
    # print(f'The sum is {a+b} ')
except ValueError:
    print('Cannot convert it')
else:   
    print(f'The sum is {a+b} ')
# finally:
#     print(f'The sum is {a+b} ')