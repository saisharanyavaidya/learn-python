def sample_func():
    print("This is a sample function")

# Call the function
sample_func()

def add(num1, num2):
    sum = num1 + num2
    return sum

res = add(1, 2)
print(res)

res = add(num2=3, num1=4)
print(res)

help(add)

def add(num1, num2, num3 = 10):
    sum = num1 + num2 + num3
    return sum

res = add(1, 2)
print(res)

# One user enters 10 numbers and another user enters 100 numbers. Define your function to handle this situation
# A: Variable length arguments

def add_args(num1, num2, *args):
    res = num1 + num2 + sum(args)
    return res

res = add_args(1, 2, 3, 4, 5, 10)
print(res)

res = add_args(1, 2, 3, 4)
print(res)

# Key word arguments

def add_args(*args, **kwargs):
    print(args, kwargs)

res = add_args(1, 2, 3, 4, num1=5, num2=10)
print(res)

res = add_args(1, 2, 3, 4)
print(res)

# map
# filter

# Lambda : inline function
add_numbers = lambda num1, num2 : num1 + num2
res = add_numbers(1, 2)
print(res)

