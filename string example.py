#count_hi
name=input("Enter the string ")
print(name.count("hi"))

#cat_dog
name=input("Enter the string ")
value=name.count("cat")
value1=name.count("dog")
if value==value1:
    print("True")
else:
    print("False")

#xyz_there
name=input("Enter the string ")
value=name.count("xyz")
value1=name.count(".xyz")
if value1>0:
    print("False")
elif value>0:
    print("True")
else:
    print("False")

#count_code
name=input("Enter the string ")
print(name.count("code"))

#end_other
name=input("Enter the string name 1")
name1=input("Enter the string name 2")
print(name[-3:-1]==name1[-3:-1])

