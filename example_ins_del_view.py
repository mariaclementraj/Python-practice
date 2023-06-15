print("1. Add employee name")
print("2. View employee name")
print("3. Delete employee name")
print("4. Exit")
name=[]
while (1!=0):
    user=int(input("Enter the choice "))
    def add():
        n=int(input("Enter how many employee do you want to add "))
        for i in range(n):
            inpu=input("Enter the name ")
            name.append(inpu)
    def view():
        print(name)
        
    def delete():
        delname=input("Enter the delete employee name ")
        if name==[]:
            print("There is nothing to delete")
        elif delname not in name:
           print("This employee is not present to delete")
        else:
            name.remove(delname)
    def exit():
        print("Thank u")
        
    if user==1:
        add()
    if user==2:
        view()
    if user==3:
        delete()
    if user==4:
        exit()
        break


