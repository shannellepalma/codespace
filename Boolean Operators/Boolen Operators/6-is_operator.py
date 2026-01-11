#Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves. For example:

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

#try to replace is with = see what happens 