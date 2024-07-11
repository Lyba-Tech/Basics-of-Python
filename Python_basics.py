#Lists
# 1. Create an empty list my_list
my_list = []

# 2. Append three elements to my_list using the append method
my_list.append('apple')
my_list.append('banana')
my_list.append('cherry')

# 3. Insert an element at a specific position in my_list using the insert method
my_list.insert(1, 'orange')  # Insert 'orange' at index 1

# 4. Remove an element from my_list using the remove method
my_list.remove('banana')  # Remove 'banana' from the list

# 5. Print the final state of my_list
print("Lists - Final state of my_list:", my_list)

# Q2. Tuples
# 1. Create a tuple my_tuple with at least five elements
my_tuple = (1, 2, 3, 4, 5)

# 2. Use tuple unpacking to assign values to multiple variables
a, b, c, d, e = my_tuple

# 3. Concatenate two tuples and print the result
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(" Tuples - Concatenated tuple:", concatenated_tuple)

# 4. Access and print the elements of my_tuple using both positive and negative indexing
print("Positive indexing example:", my_tuple[0])   # Access first element
print("Negative indexing example:", my_tuple[-1])  # Access last element

# 5. Perform any operation that demonstrates that tuples are immutable
try:
    my_tuple[0] = 10  # Trying to modify a tuple will raise a TypeError
except TypeError as e:
    print("Tuples - Tuples are immutable:", e)

# Q3. Input and Output
# 1. Prompt the user to enter their name using input
name = input(" Input and Output - Enter your name: ")

# 2. Print a welcome message using the entered name
print(f"Welcome, {name}!")

# 3. Ask the user to input two numbers, convert them to integers, and calculate their sum and product
num1 = int(input("Input and Output - Enter first number: "))
num2 = int(input("Input and Output - Enter second number: "))
sum_result = num1 + num2
product_result = num1 * num2

# 4. Display the results using formatted output
print(f" Input and Output - Sum: {sum_result}")
print(f" Input and Output - Product: {product_result}")

# Q4. Operators
# 1. Create a variable number and initialize it with an integer value
number = 15

# 2. Use the modulus operator to check if the number is even or odd
if number % 2 == 0:
    print(" Operators - Number is even")
else:
    print(" Operators - Number is odd")

# 3. Use a comparison operator to check if the number is greater than or equal to 10
if number >= 10:
    print(" Operators - Number is greater than or equal to 10")

# 4. Combine logical operators to create a complex condition and print the result
if number % 2 == 0 and number >= 10:
    print(" Operators - Number is even and greater than or equal to 10")



