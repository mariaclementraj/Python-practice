class Stu():
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone
    def get(self):
        print("Student Information")
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone is {self.phone}")

obj=Stu("Clement",20,9976816914)
obj.get()


class Stu():
    def __init__(self):
        self.name=input("Enter the Name ")
        self.age=int(input("Enter the age "))        
        self.phone=int(input("Enter the phone number "))
        self.clas=int(input("Enter the Class "))
    def get(self):
        self.m1=int(input("Enter the mark1 "))
        self.m2=int(input("Enter the mark2 "))                     
        self.m3=int(input("Enter the mark3 "))
        self.m4=int(input("Enter the mark4 "))
        self.m5=int(input("Enter the mark5 "))
    def display(self):
        print("Student Information")
        print("Name is = ",self.name)
        print("Age is = ",self.age)
        print("Phone is = ",self.phone)
        print("Class is = ",self.clas)
    def average(self):
        print("Average is = ",(self.m1+self.m2+self.m2+self.m4+self.m5)/5)
        
obj=Stu()
obj.get()
obj.display()
obj.average()
