# Create a list

sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"] # it can also be written as list()

# Indexing, Slicing
sample_element = sample_list[0]
print(sample_element)
sample_element = sample_list[1]
print(sample_element)
#sample_element = sample_list[5] # gives below error
#print(sample_element)

"""
Traceback (most recent call last):
  File "C:\DevOps-Practice\repos\learn-python\04_list.py", line 10, in <module>
    sample_element = sample_list[5]
                     ~~~~~~~~~~~^^^
IndexError: list index out of range
"""
sample_element = sample_list[len(sample_list) - 1]
print(sample_element)

# Slicing
sliced_list = sample_list[1:3] # end index is not considered/exclusive ('Terraform', 'Jenkins')
print(sliced_list)

list_len = len(sliced_list)
print(list_len)

list_len = len(sample_list)
print(list_len)

# List is a mutable datatype means once defined, it can be altered
sample_list[1] = "Shell"
print(sample_list)

# append an element to end of the list
sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]
sample_list.append("Shell") # it is affecting the original list by performing an operation, hence it is called as inplace operation
print(sample_list)

# append list to list
sample_list.append(sample_list) # here whole list will be added as a single element in the main list
print(sample_list) 
print(len(sample_list))

# extend
sample_list = [1, 2, 'sample', True] # we can store heterogeneous datatypes in a List or tuple
sample_list.extend(sample_list)
print(len(sample_list), sample_list)

# membership operator : in, not in
is_element = 2 in sample_list # checks if element 2 is there in sample_list
print(is_element)
