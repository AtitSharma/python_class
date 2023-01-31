# colors=["yellow","red","orange","blue","violent","red","white"]
# colors_to_remove=["red","violent"]
# for i in colors:
#     if i in colors_to_remove:
#         colors.remove(i)
# print(colors)


# fruits=["apple","guava","grapes","banana","orange","mango"]
# for i in range (len(fruits)):
#     if fruits[i]=="guava" or fruits[i]=="orange":
#         fruits[i]="watermelon"
# print(fruits)
# print(len(fruits))
# print(fruits[5])
students = {
    "count": 2,
    "data": [
        {
            "name": "Ram",
            "address": "Tinknune",
            "course": "Python Django",
            "attendance": [
                {
                    "month": "January",
                    "total_working_days": 25,
                    "present": 24,
                    "absent": 1,
                    "leave": 0,
                },
                {
                    "month": "February",
                    "total_working_days": 28,
                    "present": 20,
                    "absent": 2,
                    "leave": 6,
                }
            ]
        },
        {
            "name": "Hari",
            "address": "Tinknune",
            "course": "Python Django",
            "attendance": [
                {
                    "month": "January",
                    "total_working_days": 25,
                    "present": 23,
                    "absent": 1,
                    "leave": 1,
                },
                {
                    "month": "February",
                    "total_working_days": 28,
                    "present": 27,
                    "absent": 0,
                    "leave": 1,
                }
            ]
        }
    ]
}



m=students.get("data")
for i in m:
    x=list(i.values())
    y=list(i.keys())
    mm=list(zip(y,x))
    for i,j in mm:
        if i=="attendance":
            for z in j:
                datas=z.items()
                for k,l in datas:
                    print(f"{k} : {l}")
        else:           
            print(f"{i} : {j}")
    print("*************")
    
        
        
