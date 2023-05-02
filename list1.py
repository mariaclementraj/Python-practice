#Count vowels
str=input("Enter the string ")
count=0
count1=0
count2=0
count3=0
count4=0
for i in range(len(str)):
    if str[i]=="a" or str[i]=="A":
        count+=1
    elif str[i]=="e" or str[i]=="E":
        count1+=1
    elif str[i]=="i" or str[i]=="I":
        count2+=1
    elif str[i]=="o" or str[i]=="O":
        count3+=1
    elif str[i]=="u" or str[i]=="U":
        count4+=1
print("a count is = ",count)
print("e count is = ",count1)
print("i count is = ",count2)
print("o count is = ",count3)
print("u count is = ",count4)

#String reverse
str=input("Enter the string ")
x=str.split(" ")
print(x[::-1])
