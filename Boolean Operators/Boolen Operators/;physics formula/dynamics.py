def readNumber(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Invalid Entry. Please enter a valid number.")

def readPositive(text):
    while True:
        value = readNumber(text)
        if value <= 0:
            print("Invalid input: value must be greater than zero.")
        else:
            return value


while True:
    print("====================")
    print("Dynamics Calculator")
    print("====================")
    print("1. Newton's Second Law of Motion")
    print("2. Weight")
    print("3. Frictional Force")
    print("4. Gravitational Force")
    print("5. Exit")
    print("====================")

    try:
        n = int(input("ENTER YOUR CHOICE (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")
        continue

    if n < 1 or n > 5:
        print("Invalid choice. Please select 1-5.")
        continue


    if n == 1:
        m = readPositive("Enter mass (kg): ")
        a = readNumber("Enter acceleration (m/s^2): ")

        print("\nFormula: F = m * a")
        print(f"Solution: F = {m} * {a}")
        print(f"Force = {m*a} N\n")


    elif n == 2:
        m = readPositive("Enter mass (kg): ")
        g = 9.8

        print("\nFormula: W = m * g")
        print(f"Solution: W = {m} * {g}")
        print(f"Weight = {m*g} N\n")


    elif n == 3:
        mu = readPositive("Enter coefficient of friction: ")
        N = readPositive("Enter normal force (N): ")

        print("\nFormula: F_friction = μ * N")
        print(f"Solution: F_friction = {mu} * {N}")
        print(f"Frictional Force = {mu*N} N\n")


    elif n == 4:
        m1 = readPositive("Enter mass 1 (kg): ")
        m2 = readPositive("Enter mass 2 (kg): ")
        r = readPositive("Enter distance between masses (m): ")

        G = 6.674e-11
        F = G * (m1 * m2) / (r ** 2)

        print("\nFormula: F_gravity = G * (m1 * m2) / r^2")
        print(f"Solution: F_gravity = {G} * ({m1} * {m2}) / {r}^2")
        print(f"Gravitational Force = {F} N\n")


    elif n == 5:
        print("Exiting program...")
        break