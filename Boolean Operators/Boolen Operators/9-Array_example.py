#assume that you have 4 task to do in school

School_task=["review","homework","activity","reporting"]

#Prints how many task you have left
print("Remaining Task: " + str(len(School_task)))

#select the first task
print("First task is: "  + str(School_task[0]))

#Check remaining task if still 4
if len(School_task)==4:
    print("You have not finished a single task")

#print all task
print("your task is: " + str(School_task))