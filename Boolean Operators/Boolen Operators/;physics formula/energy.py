def readNumber(text):
    while True:
        try:
            value = float(input(text))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def readPositive(text):
    while True:
        value = readNumber(text)
        if value <= 0:
            print("Invalid input: Value must be greater than zero.")
        else:
            return value

half = 0.5
while True:
    print("====================")
    print("Energy Calculator")
    print("====================")
    print("1. Work")
    print("2. Kinetic Energy")
    print("3. Gravitational Potential Energy")
    print("4. Elastic Potential Energy")
    print("5. Exit")
    print("====================")

    try:
        choice = int(input("ENTER YOUR CHOICE (1-5): "))
        if choice < 1 or choice > 5:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    if choice == 1:
        F = readPositive("Enter Force (N): ")
        d = readNumber("Enter Distance (m): ")
        print(f"\nFormula: W = F * d")
        print(f"Solution: W = {F} * {d}")
        print(f"Work = {F*d} J\n")

    elif choice == 2:
        m = readPositive("Enter mass (kg): ")
        v = readNumber("Enter velocity (m/s): ")
        print(f"\nFormula: KE = 0.5 * m * v^2")
        print(f"Solution: KE = 0.5 * {m} * {v**2}")
        print(f"Kinetic Energy = {half*m*v**2} J\n")

    elif choice == 3:
        m = readPositive("Enter mass (kg): ")
        g = 9.81
        h = readNumber("Enter height (m): ")
        print(f"\nFormula: PE = m * g * h")
        print(f"Solution: PE = {m} * {g} * {h}")
        print(f"Gravitational Potential Energy = {m*g*h} J\n")

    elif choice == 4:
        k = readPositive("Enter spring constant (N/m): ")
        x = readNumber("Enter extension (m): ")
        print(f"\nFormula: U = 0.5 * k * x^2")
        print(f"Solution: U = 0.5 * {k} * {x**2}")
        print(f"Elastic Potential Energy = {half*k*x**2} J\n")

    elif choice == 5:
        print("\nExiting program...")
        print("Thank you for using Energy Calculator!")
        break