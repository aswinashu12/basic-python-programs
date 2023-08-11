def my_function(n):
    return lambda a: a * n
my_val=my_function(2)
print(my_val(3))
