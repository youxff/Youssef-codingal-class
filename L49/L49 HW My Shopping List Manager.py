# --- FILE HANDLING - My Shopping List -----------------------------------------
# Topics: open() | file modes r/w/a | read() | readlines() | write() | close()

# --- PART 1: Write your shopping list to a file -------------------------------
file = open("L49/shopping-list.txt", "w")
file.write("1. Milk\n")
file.write("2. Bread\n")
file.write("3. Eggs\n")
file.close()
print("Shopping list saved to shopping-list.txt!")

# --- PART 2: Read the full file -----------------------------------------------
file = open("L49/shopping-list.txt", "r")
content = file.read()
print("\n=== My Shopping List ===")
print(content)
file.close()

# --- PART 3: Count the items --------------------------------------------------
file = open("L49/shopping-list.txt", "r")
lines = file.readlines()
print(f"You have {len(lines)} items on your shopping list.")
file.close()

# --- PART 4: Add more items - append mode -------------------------------------
file = open("L49/shopping-list.txt", "a")
file.write("4. Apples\n")
file.write("5. Rice\n")
file.close()
print("\n2 more items added!")

# --- PART 5: Read the updated file --------------------------------------------
file = open("L49/shopping-list.txt", "r")
print("\n=== Updated Shopping List ===")
print(file.read())
file.close()

# --- PART 6: Search for an item -----------------------------------------------
file = open("L49/shopping-list.txt", "r")
content = file.read()
file.close()

item = input("\nEnter an item to search for: ")

if item in content:
    print(f"{item} is on your shopping list.")
else:
    print(f"{item} is not on your shopping list.")

# --- PART 7: Display items with numbers ---------------------------------------
file = open("L49/shopping-list.txt", "r")
lines = file.readlines()
file.close()

print("\n=== Numbered Shopping List ===")

for number, item in enumerate(lines, start=1):
    print(f"Item {number}: {item.strip()}")

# --- PART 8: Add a new item chosen by the user --------------------------------
new_item = input("\nEnter a new item to add: ")

file = open("L49/shopping-list.txt", "a")
file.write(f"{new_item}\n")
file.close()

print(f"{new_item} has been added to your shopping list.")

# --- PART 9: Show the final shopping list -------------------------------------
file = open("L49/shopping-list.txt", "r")

print("\n=== Final Shopping List ===")
for line in file:
    print(line.strip())

file.close()

print("\nThank you for using the Shopping List Manager!")
