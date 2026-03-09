#Input is not valid yet
#WHILE input is not valid:
#try to convert user input into a number
#if conversion works:
#mark input as valid
#if conversion fails:
#show error message
#return the number

while True:
    def readNumber (text):
        n=0
        valid= False
        while valid == False:
            try:
                n= float(input(text))
                valid= True
            except:
                print("Invalid Entry")

        return n
    
    a= readNumber("Enter 1st no.:")
    b= readNumber("Enter 2nd no.:")

    print("1. Addition 2. Subtraction 3. Multiplication 4. Division")

    while True:
        def readChoice (text):
            c=0
            valid= False
            while valid == False:
                try:
                    c= int(input(text))
                    if c in [1, 2, 3, 4]:
                        valid= True
                    else:
                        print("Invalid choice. Please enter a number between 1 and 4.")
                except:
                    print("Invalid Entry. Please enter a number between 1 and 4.")

            return c
        c= readChoice("Enter your choice:") 

        if c == 1:
            print(a, "+", b, "=", a+b)
        elif c == 2:
            print(a, "-", b, "=", a-b)
        elif c == 3:
            print(a, "*", b, "=", a*b)
        elif c == 4:
            if b == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(a, "/", b, "=", a/b)
        else:
            print("Invalid input")