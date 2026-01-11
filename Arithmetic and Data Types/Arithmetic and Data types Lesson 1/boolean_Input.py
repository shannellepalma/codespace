# Simple program to check if a number is even or odd

# Input a number from the user
number = int(input("Enter a number: "))

# Check if the number is even
is_even = (number % 2==0)

# Use a boolean condition to print the result
if is_even:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
