#Hello_Name
name=input("Enter the Name ")
print("Hello "+name+"!")

#make_abba
name=input("Enter the Name1 ")
name1=input("Enter the Name2 ")
print(name+name1+name1+name)

#make_tags
tag=input("Enter the tag ")
name=input("Enter the Name ")
print("<"+tag+">"+name+"</"+tag+">")

#make_out_word
tag=input("Enter the string length 4")
name=input("Enter the Name ")
print(tag[0:2]+name+tag[-1]+tag[-2])

#extra_end
name=input("Enter the Name ")
print((name[-2]+name[-1])*3)

#first_two
name=input("Enter the Name ")
print(name[0:2])

#first_half
length=0
name=input("Enter the Name in even length")
length=len(name)
i=length/2
print(name[0:int(i)])

#without_end
name=input("Enter the Name")
print(name[1:-1])

#combo_string
length=0
length1=0
name=input("Enter the Name 1 ")
name1=input("Enter the Name 2 ")
length=len(name)
length1=len(name1)
if(length>length1):
    print(name1+name+name1)
else:
    print(name+name1+name)

#non_start
name=input("Enter the Name 1 ")
name1=input("Enter the Name 2 ")
print(name[1:]+name1[1:])

#left2
name=input("Enter the Name ")
print(name[2:]+name[:2])



