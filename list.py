#Sum of the Numbers
list1=[5,7,4,9,8]
sum=0
for i in list1:
    sum=sum+i
print("Sum of the Numbers is =",sum)

#Find the maximum value
list1=[88,100,1555]
length=len(list1)
big=0
big1=0
for i in range(length):
    for j in range(i,length-1):
        if(list1[j]>list1[j+1]):
            big=list1[j]
        else:
            big1=list1[j+1]
if(big<big1):
    print("The maximum value is ",big1)   
else:
    print("The maximum value is ",big)

#Find the minimum value
list1=[2,5,52,8,100,15]
length=len(list1)
big=0
big1=0
for i in range(length):
    for j in range(i,length-1):
        if(list1[j]<list1[j+1]):
            big=list1[j+1]
            print(big)
        else:
            big1=list1[j]
            print(big1)
if(big>big1):
    print("The minimum value is ",big1)   
else:
    print("The minimum value is ",big)
