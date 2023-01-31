class Student:
    college="ABC COLLEGE"
    
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
        
print(Student.college)
s=Student("Ram","983211")
print(s.__dict__)