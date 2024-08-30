# Check whether the given number is greater than 10 or not

user_input = int(input("Enter a number : "))
#user_input = int(user_input)

# if user_input > 10:
#     print("User input value is greater than 10")
# else:
#     print("User input value is less than or equal to 10")

# Check whether the given number is greater than 10 or less than 10 or equal to 10 or something else
# Method 1 : Nested if-else
if user_input == 10:
    print("Right on Target")
else:
    if user_input > 10:
        print("User input value is greater than 10")
    else: 
        if user_input < 10:
            print("User input value is less than 10")

# Method 2
if user_input == 10:
    print("Right on Target")
elif user_input > 10:
    print("User input value is greater than 10")
else: 
    print("User input value is less than 10")

# Exception Handling : try - except
try: 
    user_input = int(input("Enter a number : "))
    if user_input == 10:
        print("Right on Target")
    elif user_input > 10:
        print("User input value is greater than 10")
    else: 
        print("User input value is less than 10")
except ValueError:
    print("Please enter a number")