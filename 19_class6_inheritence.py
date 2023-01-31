class Person:
    def __init__(self,name,address):
        self.name=name
        self.address=address       
        
    def walk(self):
        print(f"{self.name} is walking")
        
        
class Teacher(Person):
    def __init__(self,name,address,degignation):
        super().__init__(name,address)
        self.degignation=degignation
        
    def teach(self):
        print(f"{self.name} is teaching")
        
        
class Student(Person):
    def __init__(self,name,address,roll_num):
        super().__init__(name,address)
        self.roll_num=roll_num
        
    def intro(self):
        super().walk()
        print(f"{self.name} is student")
        
# t=Teacher("Shyam","ktm","good")
# # t.teach()
# # t.walk()
# s=Student("Std1","Bkt",123)
# s.intro()
# s.walk()


class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
                
    def login(self):
        print(f"{self.name} has loged in with {self.password}")
    
class Person(User):
    def __init__(self,username,password,name,address):
        super().__init__(username,password)
        self.name=name
        self.address=address
        
    def profile(self):
        print(f"Name: {self.name}")
        print(f"Username: {self.username}")
        print(f"Address: {self.address}")
        
class Student(Person):
    def __init__(self,username,password,name,address,rollnum):
        super().__init__(username,password,name,address)
        self.rollnum=rollnum
    
    def profile(self):
        super().profile()
        print(f"Roll: {self.rollnum}")
        
class Teacher(Person):
    def __init__(self,username,password,name,address,degignation):
        super().__init__(username,password,name,address)
        self.degignation=degignation
        
    def profile(self):
        super().profile()
        print(f"Degignation: {self.degignation}")
        
        
t=Teacher("teacher1",123,'Teacher_name ',"kTM","GOOD")  
t.profile()
print("*****")
s=Student("Student",1234,"student_name","Bkt",123)
s.profile()
# t.login()