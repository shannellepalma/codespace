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
                    print("Invalid Entry.")
            return c
while True:
        a= readNumber("Enter 1st no.:")
        b= readNumber("Enter 2nd no.:")

        print("--------------------------")
        print("Arithmetic Operations")
        print("--------------------------")
        print("1. [A]ddition")
        print("2. [S]ubtraction" )
        print("3. [M]ultiplication")
        print("4. [D]ivision")
        print("--------------------------")
        
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