sample_str = "This is a sample string"
sample_str_list = list(sample_str)
print(sample_str_list)

sample_str_tuple = tuple(sample_str)
print(sample_str_tuple)

# Accept input from user
user_input = input("Enter a number: ")
print(user_input, type(user_input)) # the type will be string output :  <class 'str'>

add_10 = int(user_input) + 10 # since user input will be string datatype, we need to explicitly convert it to int
print(add_10)

split_input = "10 100 200 500 700".split(" ")
print(split_input)


