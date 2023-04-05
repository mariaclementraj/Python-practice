#Grade sum
per=int(input("Entere the percentage "))
if(per>90):
    print("You are in A grade")
elif(per>80) and (per<=90):
    print("You are in B grade")
elif(per>=60) and (per<=80):
    print("You are in C grade")
elif(per<60):
    print("You are in D grade")

#electricity bill
unit=int(input("Enter the units "))
if(unit<100):
    print("No charges")
elif(unit>100) and (unit<200):
    bill=(unit-100)*5
    print("Total bill amount",bill)
elif(unit>200):
    bill=(unit-200)*10+500
    print("Total bill amount",bill)

#Road Tax
cost=int(input("Enter the cost price of bike"))
if(cost>100000):
    tax=15*100000/100
    print("Road Tax is = ",tax)
elif(cost>50000) and (cost<=100000):
    tax=10*10000/100
    print("Road Tax is = ",tax)
elif(cost<=50000):
    tax=5*10000/100
    print("Road Tax is = ",tax)
    

#Display the name of the day
num=int(input("Enter a number from 1 to 7 "))
if(num==1):
    print("Sunday")
elif(num==2):
    print("Monday")
elif(num==3):
    print("Tuesday")
elif(num==4):
    print("Wednesday")
elif(num==5):
    print("Thursday")
elif(num==6):
    print("Friday")
elif(num==7):
    print("Saturday")

#Display the name of the month
num=int(input("Enter a number from 1 to 12 "))
if(num==1):
    print("Jan")
elif(num==2):
    print("feb")
elif(num==3):
    print("Mar")
elif(num==4):
    print("Apr")
elif(num==5):
    print("May")
elif(num==6):
    print("June")
elif(num==7):
    print("July")
elif(num==8):
    print("Aug")
elif(num==9):
    print("Sep")
elif(num==10):
    print("Oct")
elif(num==10):
    print("Nov")
elif(num==12):
    print("Dec")

#Triangle sum
s1=int(input("Enter the one side valu of triangle"))
s2=int(input("Enter the second side valu of triangle"))
s3=int(input("Enter the Third side valu of triangle"))
if(s1==s2)and (s2==s3) and (s3==s1):
    print("An equilateral triangle")
elif(s1==s2)or (s2==s3) or (s3==s1):
    print("An isosceles triangle")
else:
    print("An scalene triangle")




