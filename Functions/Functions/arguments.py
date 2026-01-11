def my_function_with_args(username, greeting):
        print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
        #%s is a placeholder the first %s represent the first value from the right side
        print(f"Hello, {username} , From My Function!, I wish you {greeting}")
        #using F string

my_function_with_args("John Doe", "a great year!")
#John Doe is assigned to the first argument 
#a great year is assigned to the second argument
