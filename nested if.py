#Mathematical operators
num1=int(input("Enter the a value "))
num2=int(input("Enter the b value "))
oper=input("Which operation do you want to do = ")
if "+"==oper:
    num3=num1+num2
    print("Your addition value is = ",num3)
elif "-"==oper:
    num3=num1-num2
    print("Your addition value is = ",num3)
elif "*"==oper:
    num3=num1*num2
    print("Your addition value is = ",num3)
elif "/"==oper:
    num3=num1/num2
    print("Your addition value is = ",num3)
elif "%"==oper:
    num3=num1%num2
    print("Your addition value is = ",num3)
elif "//"==oper:
    num3=num1//num2
    print("Your addition value is = ",num3)
elif "**"==oper:
    num3=num1**num2
    print("Your addition value is = ",num3)
else:
    print("Please perform arithmetic operation only")

#Chocolate program
types="Milk White Dark Cadbury DairyMilk"
cho=input("Enter the Chocolate name")
if cho in types:
    if(cho=="Milk"):
        how=int(input("Enter how much chocolate do yuo want "))
        bill=how*10
        print("Total bill is = ", bill)
    elif(cho=="White"):
        how=int(input("Enter how much chocolate do yuo want "))
        bill=how*10
        print("Total bill is = ", bill)
    elif(cho=="Dark"):
        how=int(input("Enter how much chocolate do yuo want "))
        bill=how*10
        print("Total bill is = ", bill)
    elif(cho=="Cadbury"):
        how=int(input("Enter how much chocolate do yuo want "))
        bill=how*10
        print("Total bill is = ", bill)
    elif(cho=="DairyMilk"):
        how=int(input("Enter how much chocolate do yuo want "))
        bill=how*10
        print("Total bill is = ", bill)
else:
    print("This choclate not available now please visit later")

#Leap Year
year=int(input("Enter the year"))
if (year>3):
    if(year%4==0 and year%100!=0):
        print("This year is a leap year")
    else:
        print("This year is not a leap year")
else:
    print("Enter the Correct year")

         
