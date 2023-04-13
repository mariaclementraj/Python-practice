rows=int(input("Enter the number of rows"))
column=int(input("Enter the number of column"))
for i in range(1,rows+1):
    for j in range(1,column+1):
        print(i,end=" ")
    print("")

    
rows=int(input("Enter the number of rows"))
column=int(input("Enter the number of column"))
for i in range(1,rows+1):
    for j in range(1,column+1):
        print(j,end=" ")
        j+=1
    print("")

total=1
rows=int(input("Enter the number of rows"))
column=int(input("Enter the number of column"))
for i in range(1,rows+1):
    for j in range(1,column+1):
        j=total
        print(j,end=" ")
        j+=1
        total=j
    print("")
total=0
rows=int(input("Enter the number of rows"))
column=int(input("Enter the number of column"))
for i in range(1,rows+1):
    total=i
    for j in range(1,column+1):
        j=total
        print(j,end=" ")
        j+=3
        total=j
    print("")
     
rows=int(input("Enter the number of rows"))
column=int(input("Enter the number of column"))
for i in range(1,rows+1):
    for j in range(1,column+1):
        print(chr(64+i),end=" ")
    print("")

total=1
rows=int(input("Enter the number of rows"))
column=int(input("Enter the number of column"))
for i in range(1,rows+1):
    for j in range(1,column+1):
        j=total
        print(chr(64+j),end=" ")
        j+=1
        total=j
    print("")

total=0
rows=int(input("Enter the number of rows"))
column=int(input("Enter the number of column"))
for i in range(1,rows+1):
    total=i
    for j in range(1,column+1):
        j=total
        print(chr(64+j),end=" ")
        j+=3
        total=j
    print("")

