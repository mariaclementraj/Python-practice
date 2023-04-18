row=int(input("Enter the rows"))
for i in range(row,0,-1):
    for j in range(0,row-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        print(" * ", end=" ")
    print()
for i in range(2,row+1):
    for j in range(0,row-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        print(" * ", end=" ")
    print()

##row=int(input("Enter the rows"))
##for i in range(row,0,-1):
##    for j in range(0,row-i):
##        print(" ", end=" ")
##    for j in range(1,i+1):
##        print("*", end=" ")
##    print()
##for i in range(2,row+1):
##    for j in range(0,row-i):
##        print(" ", end=" ")
##    for j in range(1,i+1):
##        print("*", end=" ")
##    print()
