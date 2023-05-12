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
    if list1[i] in list1:
        count1=list1.count((list1[i]))
    d[key]=count1
print(d)

#sort a dictionary
d={}
length=int(input("Enter the length of the dictionary "))
for i in range (length):
    key=input("Enter the key value in name")
    d[key]=int(input("Enter the value in age"))
print(d)
sort={}
sort=sorted(d.keys())
print(sort)
sort=sorted(d.values())
print(sort)

#Reverse the sorted Order
sort=sorted(d.keys(), reverse=True)
print(sort)
sort=sorted(d.values(), reverse=True)
print(sort)

#Count vowels
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
count10=0
str1=input("Enter the string ")
d={}
for i in range(len(str1)):
    key="a"
    if str1[i]=="a":
        count1+=1
    d[key]=count1
    key="A"
    if str1[i]=="A":
        count2+=1
    d[key]=count2
    key="e"
    if str1[i]=="e":
        count3+=1
    d[key]=count3
    key="E"
    if str1[i]=="E":
        count4+=1
    d[key]=count4
    key="i"
    if str1[i]=="i":
       count5+=1
    d[key]=count5
    key="I"
    if str1[i]=="I":
        count6+=1
    d[key]=count6
    key="o"
    if str1[i]=="o":
       count7+=1
    d[key]=count7
    key="O"
    if str1[i]=="O":
        count8+=1
    d[key]=count8
    key="u"
    if str1[i]=="u":
       count9+=1
    d[key]=count9
    key="U"
    if str1[i]=="U":
        count10+=1
    d[key]=count10
print(d)


