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

def display_items():
    print("\nAvailable Items (Item : Weight, Value)")
    for i, (w, v) in items.items():
        print(f"{i}: {w}kg, Value {v}")

def calculate_totals(selected):
    total_weight = sum(items[i][0] for i in selected)
    total_value = sum(items[i][1] for i in selected)
    return total_weight, total_value

# --- Main Program ---
selected_items = []

display_items()

print("\nYou can select up to 5 items per round. Enter 'F' to finish at any time.")

while True:
    remaining_capacity = CAPACITY - sum(items[i][0] for i in selected_items)
    if remaining_capacity == 0:
        print("\n✅ Capacity reached. Cannot select more items.")
        break

    print(f"\nCurrent total weight: {sum(items[i][0] for i in selected_items)}, "
          f"total value: {sum(items[i][1] for i in selected_items)}")
    print(f"Remaining capacity: {remaining_capacity}kg")

    user_input = input("Enter up to 5 item numbers (comma-separated) or 'F' to finish: ").strip()
    
    if user_input.upper() == 'F':
        print("\n✅ Finished selection.")
        break

    try:
        choices = list(map(int, user_input.split(",")))

        if len(choices) > 5:
            print("❌ You can select a maximum of 5 items per round. Try again.")
            continue

        if any(c not in items for c in choices):
            print("❌ One or more item numbers are invalid. Try again.")
            continue

        if any(c in selected_items for c in choices):
            print("❌ One or more items already selected. Choose different items.")
            continue

        # Calculate totals for this round
        round_weight, round_value = calculate_totals(choices)
        if round_weight > remaining_capacity:
            print(f"❌ Selected items exceed remaining capacity ({remaining_capacity}kg). Try again.")
            continue

        # Add to cumulative selection
        selected_items.extend(choices)
        total_weight, total_value = calculate_totals(selected_items)
        print(f"✅ Added items {choices}. Total weight: {total_weight}, Total value: {total_value}")

    except ValueError:
        print("❌ Invalid input. Enter numbers separated by commas or 'F' to finish.")

# --- Final Totals ---
final_weight, final_value = calculate_totals(selected_items)
print("\n🎉 Final Selection Summary")
print("Items selected:", selected_items)
print("Total weight:", final_weight)
print("Total value:", final_value)
