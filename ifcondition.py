#Even number or Odd number
num=int(input("Enter the value "))
if(num%2==0):
    print("Enter the value is Even number")
else:
    print("Enter the value is Odd number")

#Positive or negative
num=int(input("Enter the value "))
if(num<0):
    print("Enter the value is Negative number")
else:
    print("Enter the value is Positive number")

#Greatest number
a=int(input("Enter the a value "))
b=int(input("Enter the b value "))
if(a>b):
    print("a value is greater than b ")
else:
    print("b value is greater than a ")
    
#Calculate the percentage of class attended
total=int(input("Enter the Toal Working days "))
wdays=int(input("Enter the Working days "))
per=total/wdays*100
if(per<75):
    print("You are not allow to sit in the exam ")
else:
    print("You are allow to sit in the exam ")

