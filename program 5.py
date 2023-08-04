#largest among 3 numbers
x=int(input("enter the 1st number  "))
y=int(input("enter the 2nd number  "))
z=int(input("enter the 3rd number  "))
if x>y and x>z:
  print("x is largest")
elif y>x and y>z:
  print("y is largest")
else:
  print("z is largest")