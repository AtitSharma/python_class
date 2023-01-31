#lambda

a=lambda x,y : x*y
# print(a(10,20))


#map

a=[1,2,3,4,5,6,7]
def increment_by_one(n):
    return n+1
val=list(map(increment_by_one,a))
# print(val)


output=list(map(lambda n: n+1,a))
# print(output)

# def find_even(n):
#     if n%2==0:
#         return n
    

# even=list(map(find_even,a))
# print(even)


def Capital_firts(n):
    return n.capitalize()
name_list=["ram",'shyam','hari',"sita","mira"]
st=list(map(Capital_firts,name_list))
# print(st)

sta=list(map(str.capitalize,name_list))
# print(sta)


# mn=list(map(int,input().split()))
# print(mn)


# sta=list(map(lambda n: n.capitalize(),name_list))
# print(sta)


# Filter (function,iterable_obj)


num=[1,2,3,4,5,6,7,8,9,10]
x=list(filter(lambda n : n%2==0,num))
# print(x)
 
a="2,4,6,d,8,9,e,4"
print(sum(map(int,filter(lambda n : n.isdigit(),a.split(",")))))
# print(sum(map(int,filter(str.isdigit,a.split(",")))))

marks_of_students=[{"name":"Ram"
                    ,"Marks":{"maths":80,"science":85,"computer":90}
                    },
                   {"name":"Sita"
                    ,"Marks":{"maths":87,"science":79,"computer":85}},
                   {"name":"Hari"
                    ,"Marks":{"maths":90,"science":75,"computer":88}}]
name=[]
marks=[]
for i in marks_of_students:
    name.append(i["name"])
    marks.append(sum(i.get("Marks").values()))
    
new_list=list(zip(name,marks))
max=new_list[0][1]
min=new_list[0][1]
for i,j in new_list:
    if j>max:
        max=j
    if j<min:
        min=j
# print(max)
# print(new_list)
for i,j in  new_list:
    if j ==max:
        print(f"First is {i}")
    elif j==min:
        print(f"Third is {i}")
    else:
        print(f"Second is {i}")
        
    

z=[1,2,2,3,4,2,2,3,4,2,0,0]
x=list(filter(lambda n : z.count(n)<2,z ))
print(x)


    






