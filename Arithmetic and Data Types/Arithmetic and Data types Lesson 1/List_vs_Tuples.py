# # Lists (mutable)
# my_list = [1, 2, 3]
# my_list.append(4)
# my_list[0] = 10
# print(my_list)  # Output: [0, 2, 3, 4]

# # Tuples (immutable)
# my_tuple = (1, 2, 3)
# # Attempting to modify a tuple will raise an error:
# # my_tuple[0] = 0  # This will result in a TypeError
# new_tuple = (0, 2, 3)
# print(new_tuple)  # Output: (0, 2, 3)

# my_list_1 = [1, 2, 3, 4]
# del my_list_1[2]
# print(my_list_1)  # Output: [1, 2, 4]

# # Deleting the entire list
# del my_list_1[2:]
# # Now my_list is not defined anymore and no longer exists

my_list2 = [1, 2, 3, 4]
my_list2 = my_list2[1:] 
print(my_list2)  # Output: [1, 2, 4] (removing the element at index 2)
