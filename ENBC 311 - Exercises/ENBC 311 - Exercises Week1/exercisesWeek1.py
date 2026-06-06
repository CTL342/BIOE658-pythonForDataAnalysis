#%% Exercise 1: Perform basic arithmetic operations with two numbers
# Data: num1 = 15, num2 = 3

# Task:
# a. Add num1 and num2
# b. Subtract num2 from num1
# c. Multiply num1 by num2
# d. Divide num1 by num2

# Solution:
num1 = 15
num2 = 3
print(num1 + num2)
print(num2 - num1)
print(num1 * num2)
print(num1 / num2)
print()

#%% Exercise 2: Manipulate a list
# Data: my_list = [10, 20, 30, 40, 50]

# Task:
# a. Add a new element 60 to my_list
# b. Remove the element 20 from my_list
# c. Get the length of my_list
# d. Access the third element of my_list

# Solution:
my_list = [10, 20, 30, 40, 50]
print(my_list)
my_list.append(60)
print(my_list)
my_list.remove(20)
print(my_list)
print(len(my_list))
print()

#%% Exercise 3: Work with a tuple
# Data: my_tuple = (1, 2, 3, 4, 5)

# Task:
# a. Access the second element of my_tuple
# b. Slice my_tuple from the second to the fourth element

# Solution:
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[1])
print(my_tuple[1:4])
print()

#%% Exercise 4: String manipulation
# Data: my_string = "Hello, World!"

# Task:
# a. Convert my_string to uppercase
# b. Replace 'World' with 'Python'
# c. Find the index of the comma ','

# Solution:
my_string = "Hello, World!"
print(my_string)
print(my_string.upper())
print(my_string.index(','))

#%% Exercise 5: Work with a dictionary
# Data: my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Task:
# a. Access the value of the key 'name'
# b. Add a new key-value pair: "email": "alice@email.com"
# c. Remove the key-value pair with the key 'age'

# Solution:
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)
print(my_dict['name'])
my_dict['email'] = "alice@email.com"
print(my_dict)
my_dict.pop('age')
print(my_dict)