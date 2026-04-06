#ATM Machine
print("Welcome to the ATM Machine")
user = int(input("Enter your ATM number  to check if it is valid"))
valid_users = [1234, 5678, 91011, 12131]
if user in valid_users:
    print("Valid USer")
    print("Select your choice")
    print("1. Withdraw")                                
    print("2. Deposit")
    print("3. Check Balance")

    choice = int(input("Enter your choice 1/2/3: "))
    balance = 1000

    if choice == 1:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Please collect your cash. Your new balance is {balance}")
        else:
            print("Insufficient balance")           
    elif choice == 2:

        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print(f"Amount deposited successfully. Your new balance is {balance}")

    elif choice == 3:
        print(f"Your current balance is {balance}")



                        




                        