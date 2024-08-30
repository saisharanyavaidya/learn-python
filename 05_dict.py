sample_dict = {1: 1, 2: 4, 3: 9} # dict()
# keys in dictionary should be of immutable datatype
print(sample_dict[3])

sample_dict = {1: 1, 2: 4, 3: 15}
print(sample_dict[3])

sample_dict = {(1, 2, 3, 4): 1, 2: 4, 3: 15} # we can define like this as tuple is also immutable
print(sample_dict[(1, 2, 3, 4)])

sample_dict = {"1, 2, 3, 4": 1, 2: 4, 3: 15} # we can define like this as string is also immutable
print(sample_dict["1, 2, 3, 4"])

#sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 15} # this gives below error as list is immutable 
#print(sample_dict[[1, 2, 3, 4]])

"""
Traceback (most recent call last):
  File "C:\DevOps-Practice\repos\learn-python\05-dict.py", line 9, in <module>
    sample_dict = {[1, 2, 3, 4]: 1, 2: 4, 3: 15} # this gives error as list is immutable
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
"""

dict_keys = sample_dict.keys()
dict_values = sample_dict.values()
dict_items = sample_dict.items()

print(dict_keys, dict_values, dict_items)

# What happens if you access a key that is not present inside a dictionary
sample_dict = {"1": 1, 2: 4, 3: 15}
#print(sample_dict[1]) # this gives below error as key 1 is not available
"""
Traceback (most recent call last):
  File "C:\DevOps-Practice\repos\learn-python\05-dict.py", line 33, in <module>
    print(sample_dict[1]) # this gives error as key 1 is not available
          ~~~~~~~~~~~^^^
KeyError: 1
"""
print(sample_dict.get(1)) # this doesnt give any error but returns None object

# Adding an item.. we can add item as dict is mutable datatype, only keys are immutable
sample_dict = {1: 1, 2: 4, 3: 15}
sample_dict[4] = 16
print(sample_dict)
