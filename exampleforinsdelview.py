print("1. Add employee name")
print("2. View employee name")
print("3. Delete employee name")
print("4. Exit")
user=int(input("Enter the choice "))
class Emp():
    def __init__(self):
       self.name=[]
    def add(self):
        if user==1:
            n=int(input("Enter the how many employee do you want to add "))
            for i in range(n):
                inpu=input("Enter the name ")
                self.name.append(inpu)
    def view(self):
        user=int(input("Enter the choice "))
        if user==2:
            print(self.name)
               
    def del1(self):
        user=int(input("Enter the choice "))
        if user==3:
            delname=input("Enter the delete name")
            self.name.remove(delname)
    def exit(self):
        user=int(input("Enter the choice "))
        if user==4:
            print("Thank u")                         
obj=Emp()
obj.add()
obj.view()
obj.del1()
obj.exit()


