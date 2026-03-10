def readAny (text):
    a=0
    valid= False
    while valid == False:
        try:
            a= float(input(text))
            valid= True
        except ValueError:
            print("Invalid Entry. Please enter a valid number.")
    return a

def readMass(text):
    m= 0
    valid= False
    while valid == False:
        try:
            m= float(input(text))
            if m != 0 and m > 0:
                valid = True
            else:
                print("Invalid Input: Mass must be a positive value.")
        except ValueError:
            print("Invalid Entry. Please enter a valid number.")
    return m
    
def readChoice(min_choice, max_choice, text):
    while True:
        try:
            c = int(input(text))
            if c < min_choice or c > max_choice:
                print(f"Invalid choice. Enter a number between {min_choice} and {max_choice}.")
            else:
                return c
        except ValueError:
            print("Invalid Entry. Please enter a whole number.")

while True:
        print("====================")
        print("Dynamics Calculator")
        print("====================")
        print("1. Newton's Second Law of Motion")
        print("2. Weight" )
        print("3. Frictional Force")
        print("4. Gravity Force")
        print("5. Exit")
        print("====================")
        
        n= readChoice(1, 5,"ENTER YOUR CHOICE (1-5):")
        if n == 1:
            m = readMass("Enter mass (kg): ")
            a = readAny("Enter acceleration (m/s^2): ")
            print("Formula:\n F = m * a")
            print(f"Solution: \n N = {m} * {a}")
            print(f"Force = {m*a} N")
        elif n == 2:
            m = readMass("Enter mass (kg): ")
            g = 9.8
            print("Formula:\n W = m * g")
            print(f"Solution:\n W = {m} * {g}")
            print(f"Weight = {m*g} N")

        elif n == 3:
            while True:
                mu = readAny("Enter coefficient of friction: ")
                if mu < 0:
                    print("Invalid Input: Coefficient of friction cannot be negative. Try again.")
                else:
                    N = readAny("Enter normal force (N): ")
                    print("Formula:\n F_friction = μ * N")
                    print(f"Solution:\n F_friction = {mu} * {N}")
                    print(f"Frictional Force = {mu*N} N")
                    break
        elif n == 4:
            m1 = readMass("Enter mass 1 (kg): ")
            m2 = readMass("Enter mass 2 (kg): ")
            r = readMass("Enter distance between masses (m): ")
            G = 6.674e-11
            F = G * (m1*m2) / (r**2)
            print("Formula:\n F_gravity = G * (m1 * m2) / r^2")
            print(f"Solution:\n F_gravity = {G} * ({m1} * {m2}) / {r}^2")
            print(f"Gravitational Force = {F} N\n")
        elif n == 5:
            print("Exiting program...")
            break
        