# Knapsack Problem

CAPACITY = 100

# 10 items (Item: (Weight, Value))
items = {
    1: (12, 20),
    2: (18, 30),
    3: (25, 40),
    4: (30, 50),
    5: (10, 15),
    6: (15, 25),
    7: (22, 35),
    8: (28, 45),
    9: (35, 60),
    10: (20, 32)
}

print("Available Items (Item : Weight, Value)")
for i, (w, v) in items.items():
    print(f"{i}: {w}kg, Value {v}")

print("\nYou can choose 5 items each round. Enter 'F' when you want to finish.\n")

while True:
    user_input = input("Enter 5 item numbers (comma-separated) or 'F' to finish: ").strip()

    if user_input.upper() == 'F':
        print("\n✅ Finished selecting items.")
        break

    try:
        choices = list(map(int, user_input.split(",")))

        # Check if exactly 5 items were chosen
        if len(choices) != 5:
            print("❌ You must choose exactly 5 items. Try again.")
            continue

        # Check for duplicates
        if len(set(choices)) != 5:
            print("❌ Duplicate items are not allowed. Try again.")
            continue

        total_weight = 0
        total_value = 0

        for c in choices:
            if c not in items:
                print(f"❌ Invalid item number: {c}. Try again.")
                break
            w, v = items[c]
            total_weight += w
            total_value += v
        else:
            print("\nChosen Items:", choices)
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
