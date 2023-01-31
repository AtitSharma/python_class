def smart_division(func):
    def wrapper(a,b):
        if b==0:
            return "Cant divide by zero"
        else:
            return func(a,b)
    return wrapper
        
        
@smart_division     
def division(a,b):
    return a/b
import time
# print(division(10,20))
# print(division(10,0))
def  Execution(fn):
    def wrapper(*x,**y):
        start=time.time()
        fn(*x,**y)
        print(time.time()-start)
    return wrapper

@Execution      
def Example(*n):
    print("Hello")
    
@Execution 
def Example2(*n):
    print(f"{n} times")

@Execution 
def Example3(x,y):
    print(x+y)
    
    
Example()
print("**")
Example2(10)
print("**")
Example3(y=10,x=20) 
    
    
