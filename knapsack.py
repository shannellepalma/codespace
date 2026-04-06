print ("Knapsack Problem")
print ("You are Dora the Explorer trying to fill your backpack with items of varying weights and values. Your backpack has a maximum weight")
print ("capacity of 100 units. You can select exactly 5 items at a time to add to your backpack. Your goal is to maximize the total value ")
print ("of the items in your backpack without exceeding the weight limit.")

CAPACITY = 100

# 10 items (Item: (Name, Weight, Value))
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

print("Available Items (Item : Weight, Value)")
for i, (name, w, v) in items.items():
    print(f"{i}. {name}: {w}kg, Value {v}")

print("\nEnter item numbers separated by commas. Enter 'F' when you want to finish.\n")

while True:
    user_input = input("Enter item numbers or 'F' to finish: ").strip()

    if user_input.upper() == 'F':
        print("\n✅ Finished selecting items.")
        break

    try:
        choices = list(map(int, user_input.split(",")))
        
        # Check for duplicates
        if len(set(choices)) != len(choices):
            print("❌ Duplicate items are not allowed. Try again.\n")
            continue

        total_weight = 0
        total_value = 0
        invalid = False

        for c in choices:
            if c not in items:
                print(f"❌ Invalid item number: {c}. Try again.\n")
                invalid = True
                break
            name, w, v = items[c]
            total_weight += w
            total_value += v

        if invalid:
            continue

        print("\nChosen Items:", [items[c][0] for c in choices])
        print("Total Weight:", total_weight)
        print("Total Value:", total_value)

        if total_weight > CAPACITY:
            print("❌ Capacity exceeded! Try again.\n")
        elif total_weight == CAPACITY:
            print("✅ Capacity reached exactly! You can choose again or enter 'F' to finish.\n")
        else:
            print("⚠ Weight is less than 100. You can choose again or enter 'F' to finish.\n")

    except ValueError:
        print("❌ Invalid input! Enter numbers separated by commas or 'F' to finish.\n")
