import json

# New book to add
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# ------------------------------
# Task 1 — Read the inventory
# ------------------------------
with open("inventory.json", "r") as file:
    inventory = json.load(file)

print("Total books in inventory:", len(inventory))


# ------------------------------
# Task 2 — Update and save
# ------------------------------
inventory.append(new_book)

with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

print("New book added successfully!")


# ------------------------------
# Task 3 — Display the inventory
# ------------------------------
with open("inventory.json", "r") as file:
    updated_inventory = json.load(file)

print("\nUpdated Inventory:\n")

for book in updated_inventory:
    print(f"Title: {book['title']} | "
          f"Author: {book['author']} | "
          f"Price: ${book['price']:.2f}")