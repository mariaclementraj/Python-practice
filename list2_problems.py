#single loop
#count_evens
count=0
l=()
list1=list(l)
end=int(input("Enter the Range"))
for i in range (end):
    inputval=int(input("Enter the range value"))
    list1.append(inputval)
print(list1)
for i in range (len(list1)):
    if(list1[i]%2==0):
        count=count+1
print(count)

#big_diff
l=()
list1=list(l)
end=int(input("Enter the Range"))
for i in range (end):
    inputval=int(input("Enter the range value"))
    list1.append(inputval)
print(list1)
small=list1[0]
for i in list1:
    if i<small:
        small=i
maxi=list1[0]
for i in list1:
    if i>maxi:
        maxi=i
diff=maxi-small
print(diff)


#sum13
count=0
l=()
list1=list(l)
end=int(input("Enter the Range"))
for i in range (end):
    inputval=int(input("Enter the range value"))
    list1.append(inputval)
print(list1)
for i in range (len(list1)):
    if list1[i]==13:
        break
    count=count+list1[i]
print(count)

#has22
count=0
l=()
list1=list(l)
end=int(input("Enter the Range"))
for i in range (end):
    inputval=int(input("Enter the range value"))
    list1.append(inputval)
print(list1)
for i in range (len(list1)-1):
    if(list1[i]==2 and list1[i+1]==2):
        count=count+1
if count>0:
    print("True")
else:
    print("False")


