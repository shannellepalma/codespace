#The "and" and "or" boolean operators allow building complex boolean expressions, for example:
#Try to change name to Rick and see what happens 

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")