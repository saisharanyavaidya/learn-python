sample_set = {1, 2, 5, 2, 4, 3} # set can also be written as set()
print(sample_set) # output will be {1, 2, 3, 4, 5}..
#A Set returns unique elements that is stored inside a variable
# Sets do not consider the order of insertion
# Sets don't support indexing

# Add elements to a set
sample_set.add(6)
print(sample_set)

# we also have methods like intersection(), union()

# Sets don't support indexing
print(sample_set[2]) # this gives below error

"""
Traceback (most recent call last):
  File "C:\DevOps-Practice\repos\learn-python\06_sets.py", line 14, in <module>
    print(sample_set[2]) # this gives below error
          ~~~~~~~~~~^^^
TypeError: 'set' object is not subscriptable
"""
