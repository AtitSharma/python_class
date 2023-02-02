# print(all([True,True,False]))
# print(any([True,True,False]))

a=[]
def append_item(items,a=[]):
    a.append(items)
    return a


b=append_item(20)
print(b)
c=append_item(10)
print(c)
