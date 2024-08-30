sample_str = "This is a sample string"
print(sample_str)

# How to access individual characters from a string
print(sample_str[8])

# Slicing
sub_str = sample_str[2 : 7]
print(sub_str)

# -ve indexing
print(sample_str[-1]) # last character
sub_str_neg_index = sample_str[-7 : -2]
print(sub_str_neg_index)

sub_str = sample_str[:]
print(sub_str)

sub_str = sample_str[1:]
print(sub_str)

sub_str = sample_str[:5]
print(sub_str)

sub_str = sample_str[::2]
print(sub_str) # prints characters at 0,2,,4,6,8..

# Reverse a string
sub_str = sample_str[::-1]
print(sub_str) # reverses a string (imp)

# length of a string
len_str = len(sample_str)
print("Length of the string:", len_str)

# Method
sample_str = "hello"
print(sample_str.capitalize()) # capitalizes first character and prints Hello

# split(), join(), format(), count(), strip(), lstrip(), rstrip()
sample_str = "This is a sample string"
str_split = sample_str.split() # by default it splits on whitespaces if any seperator is not specified.. output will be a list
print(str_split, type(str_split))

join_split_Str = " ".join(str_split)
print(join_split_Str, type(join_split_Str))

join_split_Str = "-".join(str_split)
print(join_split_Str, type(join_split_Str))

count_a = sample_str.count('a')
print(count_a)

sample_str = "     devops is a good career choice    "
strip_str = sample_str.strip() # removes leading and trailing spaces.. lstrip() removes leading spaces, rstrip() removes trailing spaces
print(strip_str)

# Strings are immutable means once they are assigned, they cannot be altered
sample_Str = "This is a sample string"
sample_Str[-1] = 'G'
print(sample_Str) # this gives below error

"""
Traceback (most recent call last):
  File "C:\DevOps-Practice\repos\learn-python\02_strings.py", line 59, in <module>
    sample_Str[-1] = 'G'
    ~~~~~~~~~~^^^^
TypeError: 'str' object does not support item assignment

"""