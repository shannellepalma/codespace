print ("Shannelle P. Palma, BSCpE 1-1")
print ("-------------------------------")
print ("0/1 Knapsack Problem (Dynamic Programming)")
print ("-------------------------------")
print ("You are Dora the Explorer trying to fill your backpack with items of varying weights and values. Your backpack has a maximum weight")
print ("capacity of 100 units. You can select exactly 5 items at a time to add to your backpack. Your goal is to maximize the total value ")
print ("of the items in your backpack without exceeding the weight limit.")
print ("-----------------------------------------------------------------------------------------------------------------------")

CAPACITY = 100

# Items: (Name, Weight, Value)
items = {
    1: ("Robux gift card", 12, 20),
    2: ("Iphone 17", 18, 30),
    3: ("Tissue", 5, 40),
    4: ("Digicam", 30, 50),
    5: ("Mcdo", 10, 15),
    6: ("5 Dollars", 15, 25),
    7: ("Pancit Canton", 22, 35),
    8: ("Hollowblocks", 28, 45),
    9: ("Hanger", 35, 60),
    10: ("Mystery Box", 20, 32)
}

# Extract weights and values for DP
weights = [0] + [items[i][1] for i in range(1, 11)]  # 1-indexed
values = [0] + [items[i][2] for i in range(1, 11)]   # 1-indexed
n = len(items)

# Initialize DP table
dp = [[0 for w in range(CAPACITY + 1)] for i in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for w in range(CAPACITY + 1):
        if weights[i] <= w:
            dp[i][w] = max(dp[i-1][w], values[i] + dp[i-1][w - weights[i]])
        else:
            dp[i][w] = dp[i-1][w]

# Function to trace back which items were chosen
def find_items(dp, weights, n, W):
    w = W
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen.append(i)
            w -= weights[i]
    return chosen[::-1]  # Reverse to get original order

# Interactive part
print("Available Items (Item : Weight, Value)")
for i, (name, w, v) in items.items():
    print(f"{i}. {name}: {w}kg, Value {v}")

while True:
    print("\nOptions:")
    print("1 - Enter 5 items")
    print("2 - Show optimal selection")
    print("F - Finish program")
    
    user_input = input("Choose an option: ").strip().upper()
    
    if user_input == 'F':
        print("\n✅ Program finished.")
        break
    elif user_input == '1':
        try:
            selection = input("Enter exactly 5 item numbers (1-10) separated by commas: ").strip()
            
            # Check for invalid commas or spaces (like "1 2 3 4 5" or "1,,2,3,4,5")
            if " " in selection or ",," in selection:
                raise ValueError("❌ Invalid input! Make sure numbers are separated by a single comma with no spaces.")

            choices = list(map(int, selection.split(",")))

            # Check if exactly 5 items were chosen
            if len(choices) != 5:
                print("❌ You must enter exactly 5 items.\n")
                continue
            
            # Check if all numbers are 1-10
            if not all(1 <= c <= 10 for c in choices):
                print("❌ Invalid input! Only numbers 1-10 are allowed.\n")
                continue
            
            # Check for duplicates
            if len(set(choices)) != 5:
                print("❌ Duplicate items are not allowed.\n")
                continue

            total_weight = sum(items[c][1] for c in choices)
            total_value = sum(items[c][2] for c in choices)

            print("\nYour chosen items:", [items[c][0] for c in choices])
            print("Total Weight:", total_weight)
            print("Total Value:", total_value)

            if total_weight > CAPACITY:
                print("❌ Capacity exceeded! Try again.\n")
            elif total_weight == CAPACITY:
                print("✅ Capacity reached exactly! You can continue or choose another 5 items.\n")
            else:
                print("⚠ Weight is less than 100. You can continue or choose another 5 items.\n")

        except ValueError as e:
            # Catch both conversion errors and invalid format
            print(f"{e}\n❌ Invalid input! Enter exactly 5 numbers 1-10 separated by single commas, no spaces.\n")

    elif user_input == '2':
        optimal_items = find_items(dp, weights, n, CAPACITY)
        total_weight = sum(items[i][1] for i in optimal_items)
        total_value = sum(items[i][2] for i in optimal_items)

        print("\n✅ Optimal selection (2):")
        for i in optimal_items:
            print(f"- {items[i][0]} ({items[i][1]}kg, Value {items[i][2]})")
        print("Total Weight:", total_weight)
        print("Total Value:", total_value)
    else:
        print("❌ Invalid option! Choose 1, 2, or F.\n")
