# i=number of rows      j=number of columns   k= number of space
i=1
while i<=5:
    k=1
    while k<=5-i:
         print("",end=" ")
         k=k+1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
