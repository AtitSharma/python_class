def decorate_func(func):
    def wrapper(n):
        print("Hello guyz")
        func(n)
        print("Bye Bye Everyone")
    return wrapper
@decorate_func
def welcome(n):
    print("Welcome everone")

@decorate_func
def push(n):
    print("Push", n)
# w=decorate_func(welcome)
# w()
welcome(1)
# push(1)






