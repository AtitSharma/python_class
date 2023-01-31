class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password    
        
    @classmethod
    def create_user_with_random_paswword(cls,username):
        return cls(username,"Default_password")
    
 
u=User("atit@gmail.com",1123)
print(u.__dict__)
u2=User.create_user_with_random_paswword("hari@gmailcom")
print(u2.__dict__)
