# There are two methods to create a tuple
# 1. ()
# 2. tuple()
# Behaviour: they are immutable

sample_tuple = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s") # Tool set

sample_element = sample_tuple[0]
print(sample_element)
sample_element = sample_tuple[1]
print(sample_element) 
sample_element = sample_tuple[-1] # gives last element
print(sample_element)

# Slicing
sliced_tuple = sample_tuple[1:3] # end index is not considered/exclusive ('Terraform', 'Jenkins')
print(sliced_tuple)

tuple_len = len(sliced_tuple)
print(tuple_len)

tuple_len = len(sample_tuple)
print(tuple_len)

# immutability
#sample_tuple[1] = "Shell"
#print(sample_tuple) # it gives below error

"""
Traceback (most recent call last):
  File "C:\DevOps-Practice\repos\learn-python\03-tuples.py", line 26, in <module>
    sample_tuple[1] = "Shell"
    ~~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
"""

# Operations
res_tuple = sample_tuple + sliced_tuple
print(res_tuple)

res_tuple_1 = sliced_tuple * 2
print(res_tuple_1)

# Methods
k8s_index = res_tuple.index("K8s")
print(k8s_index)

# Tuple unpacking (imp)
ansible, terraform, jenkins, docker, k8s = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s")
print(ansible, terraform, jenkins, docker, k8s) # output is Ansible Terraform Jenkins Docker K8s --> it unpacks and assigns each value to one variable

val1, val2, val3, val4, val5 = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s")
print(ansible, terraform, jenkins, docker, k8s) # output is Ansible Terraform Jenkins Docker K8s --> it unpacks and assigns each value to one variable

ansible, *tools, orchestrator = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s", "DevOps")
print(ansible, tools, orchestrator) # output is Ansible ['Terraform', 'Jenkins', 'Docker', 'K8s'] DevOps
print(*tools)

ansible, terraform, jenkins, docker, k8s, shell = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s")
print(ansible, terraform, jenkins, docker, k8s) # output is the below error

"""
Ansible Terraform Jenkins Docker K8s
Traceback (most recent call last):
  File "C:\DevOps-Practice\repos\learn-python\03-tuples.py", line 52, in <module>
    ansible, terraform, jenkins, docker, k8s, shell = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s")
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: not enough values to unpack (expected 6, got 5)

"""


