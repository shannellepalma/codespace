print("WELCOME TO NEWTON'S LAW CALCULATOR")
print("--------------------------------------------------------")

def value(text):
        l= 0
        valid= False
        while valid == False:
            try:
                l= float(input(text))
                valid = True
            except ValueError:
                print("Invalid Entry")
        return l
    
def choice(text):
            c= 0
            valid= False
            while valid == False:
                try:
                    c= int(input(text))
                    if c in [1, 2, 3, 4]:
                        valid= True
                    else:
                        print("Invalid choice. Please enter a number between 1 and 4.")
                except ValueError:
                    print("Invalid Entry")
            return c

def division (text):
    d= 0
    valid= False
    while valid == False:
        try:
            d= float(input(text))
            if d != 0:
                valid = True
            else:
                print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Invalid Entry")
    return d

def mass (text):
    m= 0
    valid= False
    while valid == False:
        try:
            m= float(input(text))
            if m != 0 and m > 0:
                valid = True
            else:
                print("Error: Mass must be a positive value.")
        except ValueError:
            print("Invalid Entry")
    return m

while True:
    print("1. Force ")
    print("2. Mass")
    print("3. Acceleration")
    print("4. Exit")
    print("--------------------------------------------------------")
    n = choice("ENTER YOUR CHOICE (1-4):")

    if n == 1:
        m = mass("Enter the mass in kg:")
        a = value("Enter the acceleration in m/s^2:")
        print("--------------------------------------------------------")
        print("Formula:")
        print("F = m * a")
        print("--------------------------------------------------------")
        print("Solution:")
        print(f"N = {m} * {a}")
        print(f"Force = {m*a} N")
        print("--------------------------------------------------------")

    elif n == 2:
        f = value("Enter the force in N:")
        a = division("Enter the acceleration in m/s^2:")
        print("--------------------------------------------------------")
        print("Formula:")
        print("m = F / a")
        print("--------------------------------------------------------")
        print("Solution:")
        print(f"m = {f} / {a}")
        print(f"Mass = {f/a} kg")
        print("--------------------------------------------------------")

    elif n == 3:
        f = value("Enter the force in N:")
        m = mass("Enter the mass in kg:")
        print("--------------------------------------------------------")
        print("Formula:")
        print("a = F / m")
        print("--------------------------------------------------------")
        print("Solution:")
        print(f"a = {f} / {m}")
        print(f"Acceleration = {f/m} m/s^2")
        print("--------------------------------------------------------")

    elif n == 4:
        print("Thank you for using the Newton's Law Calculator!")
        print("--------------------------------------------------------")
        break

    else:
        print("Invalid input")


    
