# This is single line comment
"""
This is multiline comment
"""

# define a variable
a = 42 # integer

#print the value that is stored inside the variable
print(a)

# Float value
b = 42.678
print(b)

# Boolean
c = True
print(c)

# Strings
d = 'This is a string'
e = "This is also a string"
f = """
This is a multi line string
"""

# Ex: Today's weather is nice
d = 'Today\'s weather is nice'
print(d)

d = "Today's weather is nice"
print(d)


# List
test_list = ["hello", "world", "python"]
print(test_list)

# Tuple
test_tuple = ("hello", "world", "python")
print(test_tuple)

# Dictionary
test_dict = {'a':1, 'b':2, 'c':3}
print(test_dict)

# Set
# prints/considers the value in an arbitrary way (not in order given)
test_set = {'a','b',"abc"}
print(test_set)

# type()
# type() function prints datatype of the variable
print(type(test_dict))
print(type(print)) # built in function or method


# ------------------------ Operations ------------------------------

# Add
a = 42
b = 42.35
c = a + b
print(c)

# Sub
d = a - b
print(d)

# Mul
e = a*b
print(e)

# Div
f = 12
g = 3
h = f / g # by default division returns floating value
print(h, type(h)) 

# Integer division
h = f // g # this gives integer value rather than floating value
print(h, type(h))

# Modulo division 
i = f % g # gives reminder of the division
print(i)

# Addition use case
a = "42"
b = "43"
print(a + " " + b) # gives 42 43 .. this is called concatenation

# Power
a = 10
print(a**2) # a square

# ------------------------------------------ Comparision Operators -----------------------------------------

a = 10
b = 20
res = a > b
res_1 = a < b
res_2 = a != b
res_3 = a == b

print(res, res_1, res_2, res_3)

# ------------------------------------------ Logical Operators -----------------------------------------------

# AND, NOT, OR
a = True
b = False

res = a and b
res_1 = a or b
res_2 = not a
res_3 = not b
print(res, res_1, res_2, res_3)