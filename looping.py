#calculate sum of all numbers
num=int(input("Enter the number"))
total=0
for i in range(1,num+1):
    total=total+i
print("Sum of number is ",total)
    
    
#calculate sum of all Odd numbers
num=int(input("Enter the number"))
total=0
for i in range(1,num):
    if(i%2!=0):
        total=total+i
print("Sum of Odd number is ",total)
    
#Multiplication table
ans=0
ran=int(input("Enter the range"))
mul=int(input("Enter the multiplication number"))
for i in range(1,ran+1):
    ans=i*mul
    print(i," x ",mul, " = ",ans)
