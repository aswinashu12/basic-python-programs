num=int(input("enter the number"))
def factorial(n):
    if n<=1:
        return n
    else:
        x=n*factorial(n-1)
    return x
print(factorial(num))