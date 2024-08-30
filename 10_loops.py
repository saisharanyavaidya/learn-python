sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]

for element in sample_list:
    print(element, len(element))

# Print the element and its corredponding index
for ele in enumerate(sample_list):
    print(ele) # this gives output in tuple

for idx,ele in enumerate(sample_list):
    print(idx,ele)

# Range based for loop

sample_range = range(0, len(sample_list))
print(sample_range, type(sample_range)) # output is range(0, 5) <class 'range'>

# so to get all the elements, we have to iterate over range
for idx in range(0, len(sample_list)):
    print(idx, sample_list[idx])

# continue statement : skips the iteration if condition is satisfied 
for idx in range(0, len(sample_list)):
    if sample_list[idx] == "Docker":
        continue
    print("continue statement", idx, sample_list[idx])


# break statement : it comes out of the loop if condition is satisfied and doesnt print anything after that
for idx in range(0, len(sample_list)):
    if sample_list[idx] == "Docker":
        break
    print("break statement", idx, sample_list[idx])

# While loop
sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]

idx = 0

while idx < len(sample_list):
    print("While loop", idx, sample_list[idx])
    idx += 1

while idx < len(sample_list):
    if sample_list[idx] == "Ansible":
        break
    print("While loop break", idx, sample_list[idx])
    idx += 1


sample_dict = {1: 1, 2: 4, 3: 15}

for k, v in sample_dict.items():
    print(k, v)