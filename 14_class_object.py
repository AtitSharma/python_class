# class Projector:
#     def __init__(self,color,year,model):
#         self.color=color
#         self.year=year
#         self.model=model
        
#     def visualize(self):
#         print(f"Visualizing {self.model}")
        
#     def lightning(self):
#         print(f"Lightning {self.color}")
    
#     def Description(self):
#         print(f"{self.color} {self.year} {self.model}")
#         print("***")     
          
#     def __str__(self):
#         return self.color
    
    
#     def __repr__(self):
#         return self.model
    
        
# p1=Projector("Pink",2020,"Nec")
# p2=Projector("White",2019,"Acer")
# # p1.Description()
# # p1.lightning()
# print(p1)
# print(p1.__dict__)
# print(p1.__sizeof__())
# p2.Description()
# p1.visualize()
# p2.Description()
# projectors=[]
# for _ in range (2):
#     color=input("Color :")
#     model=input("Model :")
#     year=input("Year :")
#     p=Projector(color,year,model)
#     projectors.append(p)
    
# print(projectors)

  
class Student:
    def __init__(self,id,name,contact,address):
        self.id=id
        self.name=name
        self.contact=contact
        self.address=address
        self.total_attendance=0
        
    def update_attendance(self):
        self.total_attendance+=1
        
   
    def view_attendance(self):
        return self.total_attendance 
    
s=Student(123,"Atit","78121","KTM")
s.update_attendance() 
print(Student.view_attendance(s)) #Instance Method

s2=Student(123,"Ram","09801371","BKT")
s2.update_attendance()
print(s2.view_attendance())



