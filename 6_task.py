# main=[]
# even=[]
# odd=[]
# duplicates=[]
# for i in range (15):
#     num=int(input())
#     main.append(num)
#     if num%2==0 and (num not in even):
#         even.append(num)
#     if num%2!=0 and (num not in odd):
#         odd.append(num)
#     if main.count(num)>1 :
#         duplicates.append(num)  
# print(main)
# print(even)
# print(odd)
# print(duplicates)



main=[]
even=[]
odd=[]
duplicates=[]
for i in range (15):
    num=int(input())
    if num in main:
        duplicates.append(num)
    else:
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
    main.append(num)   
print(main)
print(even)
print(odd)
print(duplicates)   

 