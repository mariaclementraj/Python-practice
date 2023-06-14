class Stu():
    def __init__(self):
        self.name=input("Enter the Name ")
        self.age=int(input("Enter the age "))
        self.m3=int(input("Enter the mark3 "))
        self.m4=int(input("Enter the mark4 "))  
     
class Stu1(Stu):
    def __init__(self):
        self.m1=int(input("Enter the mark1 "))
        self.m2=int(input("Enter the mark2 ")) 
        super().__init__()    
    def display(self):
        print("Student Information")
        print("Name is = ",self.name)
        print("Age is = ",self.age)
        print("Mark1 = ",self.m1)
        print("Mark2 = ",self.m2)
        print("Mark3 = ",self.m3)
        print("Mark4 = ",self.m4)
    def average(self):
        print("Average is = ",(self.m1+self.m2+self.m3+self.m4)/4)
        
obj=Stu1()
obj.display()
obj.average()

class Stu():
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Stu1(Stu):
    def __init__(self,name,age,m3,m4):
        super().__init__(name,age)
        self.m3=m3
        self.m4=m4
      
class Stu2(Stu1):
    def __init__(self,name,age,m1,m2,m3,m4):
        super().__init__(name,age,m3,m4)
        self.m1=m1
        self.m2=m2 
    def display(self):
        print("Student Information")
        print("Name is = ",self.name)
        print("Age is = ",self.age)
        print("Mark1 = ",self.m1)
        print("Mark2 = ",self.m2)
        print("Mark3 = ",self.m3)
        print("Mark4 = ",self.m4)
    def average(self):
        print("Average is = ",(self.m1+self.m2+self.m3+self.m4)/4)
        
obj=Stu2("clement",29,55,55,55,55)
obj.display()
obj.average()
