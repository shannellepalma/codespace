def readNumber(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def readPositive(text):
    while True:
        value = readNumber(text)
        if value <= 0:
            print("Invalid input. Value must be greater than zero.")
        else:
            return value

while True:
    print("====================")
    print("Thermodynamics Calculator")
    print("====================")
    print("1. First Law of Thermodynamics")
    print("2. Heat Capacity")
    print("3. Specific Heat Capacity")
    print("4. Molar Heat Capacity")
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
        U = readNumber("Enter change in internal energy (ΔU): ")
        W = readNumber("Enter work done (ΔW): ")

        print("\nFormula: ΔQ = ΔU + ΔW")
        print(f"Solution: ΔQ = {U} + {W}")
        print(f"Heat Transfer = {U + W}\n")


    elif n == 2:
        Q = readNumber("Enter heat change (ΔQ): ")
        dT = readNumber("Enter temperature change (ΔT): ")

        if dT == 0:
            print("Temperature change cannot be zero.\n")
        else:
            print("\nFormula: C = ΔQ / ΔT")
            print(f"Solution: C = {Q} / {dT}")
            print(f"Heat Capacity = {Q/dT}\n")


    elif n == 3:
        Q = readNumber("Enter heat change (ΔQ): ")
        m = readPositive("Enter mass (kg): ")
        dT = readNumber("Enter temperature change (ΔT): ")

        if dT == 0:
            print("Temperature change cannot be zero.\n")
        else:
            print("\nFormula: c = ΔQ / (mΔT)")
            print(f"Solution: c = {Q} / ({m} * {dT})")
            print(f"Specific Heat Capacity = {Q/(m*dT)}\n")


    elif n == 4:
        Q = readNumber("Enter heat change (ΔQ): ")
        n_moles = readPositive("Enter number of moles (n): ")
        dT = readNumber("Enter temperature change (ΔT): ")

        if dT == 0:
            print("Temperature change cannot be zero.\n")
        else:
            print("\nFormula: C = ΔQ / (nΔT)")
            print(f"Solution: C = {Q} / ({n_moles} * {dT})")
            print(f"Molar Heat Capacity = {Q/(n_moles*dT)}\n")


    elif n == 5:
        print("Exiting program...")
        break