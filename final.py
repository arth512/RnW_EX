print("Welcome to Inventory List Analyzer!\n")

items = []
categories = set()

while True:
    name = input("Enter item name: ").strip().lower()
    category = input("Enter category: ").strip().lower()

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative! Try again.")
                continue
            break
        except ValueError:
            print("Invalid quantity! Please enter a number.")

    items.append((name, category, quantity))
    categories.add(category)

    choice = input("\nDo you want to add more items? (y/n): ").lower()
    print()
    if choice != 'y':
        break

print("=========== INVENTORY SUMMARY ===========\n")

total_items = len(items)
print(f"Total Different Items: {total_items}")
print(f"Explanation: You entered {total_items} different items: " +
      ", ".join(i[0].capitalize() for i in items) + ".\n")

total_quantity = sum(i[2] for i in items)
print(f"Total Quantity in Stock: {total_quantity}")
print("Explanation: Sum of all quantities: " +
      " + ".join(str(i[2]) for i in items) +
      f" = {total_quantity}\n")

average_quantity = total_quantity / total_items
print(f"Average Quantity per Item: {average_quantity:.2f}")
print(f"Explanation: Average = {total_quantity} total / {total_items} items\n")

most_stocked = max(items, key=lambda x: x[2])
least_stocked = min(items, key=lambda x: x[2])

print(f"Most Stocked Item: {most_stocked[0].capitalize()} ({most_stocked[2]} units)")
print("Explanation: Has the highest quantity among all items.\n")

print(f"Least Stocked Item: {least_stocked[0].capitalize()} ({least_stocked[2]} units)")
print("Explanation: Has the lowest quantity.\n")

print("----------------------------------------\n")

print(f"Unique Categories in Inventory: {categories}")
print("Explanation: Categories are taken from user input and converted to lowercase.")
print("No duplicates are shown here.\n")

print("----------------------------------------")
print("Items Sorted by Quantity (High to Low):\n")

sorted_items = sorted(items, key=lambda x: x[2], reverse=True)
for idx, item in enumerate(sorted_items, start=1):
    print(f"{idx}. {item[0].capitalize()} - {item[2]} units")

print("\nExplanation: Sorted using quantity field (highest to lowest).\n")

print("----------------------------------------")
print("Categories in Alphabetical Order:\n")

sorted_categories = sorted(categories)
for idx, cat in enumerate(sorted_categories, start=1):
    print(f"{idx}. {cat}")

print("\nExplanation: Unique categories sorted alphabetically for display.")
print("\n=========== END OF REPORT ===========")
