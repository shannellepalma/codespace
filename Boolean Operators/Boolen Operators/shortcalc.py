while True:
    a = float(input("Enter 1st no.: "))
    b = float(input("Enter 2nd no.: "))

    print("1.Addition 2.Subtraction 3.Multiplication 4.Division")
    c = int(input("Choice: "))

    ops = {
        1: ("+", a + b),
        2: ("-", a - b),
        3: ("*", a * b),
        4: ("/", "Error" if b == 0 else a / b)
    }

    if c in ops:
        print(a, ops[c][0], b, "=", ops[c][1])
    else:
        print("Invalid input")