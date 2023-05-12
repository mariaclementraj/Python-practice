#student passed detail
stu={}
length=int(input("Enter the length of the student information"))
for i in range (length):
    key=input("Enter the student name")
    value=int(input("Enter the mark"))
    if (value>=35):
        stu[key]=value
print(stu)

#Convert two list into dictionary
d={}
l1=["name", "age", "no"]
l2=["clama", "20", "1234"]
for i in range(len(l1)):
    key=l1[i]
    d[key]=l2[i]
print(d)
    
#Count key and value
count1=0
d={}
list1=[1,1,2,5,1,2,6]
for i in range(len(list1)):
    key=list1[i]
    if list1[i]in list1:
        count1=list1.count((list1[i]))
    d[key]=count1
print(d)

Count vowels
count1=0
str1=input("Enter the string")
d={}
for i in range(len(str1)):
    key="a"
    if "a" in str1:
        count1=str1.count("a")
    d[key]=count1
    key="A"
    if "A" in str1:
        count1=str1.count("A")
    d[key]=count1
    key="e"
    if "e" in str1:
        count1=str1.count("e")
    d[key]=count1
    key="E"
    if "E" in str1:
        count1=str1.count("E")
    d[key]=count1
    key="i"
    if "i" in str1:
        count1=str1.count("i")
    d[key]=count1
    key="I"
    if "I" in str1:
        count1=str1.count("I")
    d[key]=count1
    key="o"
    if "o" in str1:
        count1=str1.count("o")
    d[key]=count1
    key="O"
    if "O" in str1:
        count1=str1.count("O")
    d[key]=count1
    key="u"
    if "u" in str1:
        count1=str1.count("u")
    d[key]=count1
    key="U"
    if "U" in str1:
        count1=str1.count("U")
    d[key]=count1

print(d)

