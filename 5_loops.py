# x=[1,2,3,4,5]
# # for i in range (len(x)-1):
# #     print(x[i])

# """
# Range (start,stop,step)
# Range(10)--> start->0,stop->9,stop->1
# Range(1,10)--> start->1,stop->9,stop->1
# Range(1,10,2)--> start->1,stop->9,stop->2
# #Output 1,3,5,7,9
# """
# # for i in range (1,101):
# #     print(i)
    
    
# # i=0
# # while (i<101):
# #     print(i)
# #     i+=1
# Sum=0
# for i in range (1,11):
#     Sum+=i
# print(Sum)
# print(sum(range(1,11)))
# ## Sum of even numbers
# Total2=0
# for i in range (1,21):
#     if i%2==0:
#         Total2+=i       
# print(Total2)

# Total2=0
# for i in range (0,21,2):
#     Total2+=i       
# print(Total2)

# print(sum(range(0,21,2)))

# x=[]
# for i in range(5):
#     Name=input("Enter the name : ")
#     x.append(Name.title())

# print(x)

# i=0
# while i<5:
#     print("Hello",i+1)
#     i+=1



# i=2
# Total=0
# while i<20:
#     Total+=i
#     i+=2
# print(Total)


# Sum=0
# i=1
# while i<50:
#     if i%3==0 or i%5==0:
#         # print(i)
#         Sum+=i
#     i+=1
        
# print(Sum)
# print(sum([i for i in range (1,50) if i%3==0 or i%5==0 ]))


# a="19d89d43d56"
# x=a.split("d")
# Sum=0
# for i in x:
#     Sum+=int(i)
# print(Sum)
# print(eval(a.replace("d","+")))


# x=True
# while x:
#     username=input("Enter username")
#     password=int(input("Enter password "))
#     if username=="abc@gmail.com" and password==12345:
#         print("Sucess")
#         x=False

# username=input("Enter username")
# password=input("Enter password ")
# while username!= "abc@gmail.com" or password != "12345":
#     username=input("Enter username")
#     password=input("Enter password ")
# print("Sucess")


        
# for i in range (1,10):    
#     a=int(input())   
#     if a==9:
#         break
    
for i in range (1,10):         
    if i==7:
        continue
    print(i)
    
    
while True:
    a=input("Roll the dice")
    if a==6 or a==1:
        continue
    else:
        break



        

    
