# =========================
# Lab 03 – Python Collections Practice
# =========================

print("QUESTION 1 – Student Grades\n")

grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()

print("Sorted grades:", grades)
print("Highest grade:", grades[-1])
print("Lowest grade:", grades[0])
print("Total number of grades:", len(grades))

print("\n-----------------------------\n")

# =========================
# Question 2 – Shopping Cart
# =========================

print("QUESTION 2 – Shopping Cart\n")

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

print("Number of apples:", cart.count("apple"))
print("Position of milk:", cart.index("milk"))

cart.remove("apple")
removed = cart.pop()

print("Removed item using pop:", removed)
print("Is banana in cart?", "banana" in cart)
print("Final cart:", cart)

print("\n-----------------------------\n")

# =========================
# Question 3 – Tuples
# =========================

print("QUESTION 3 – Coordinate System\n")

point1 = (3, 5)
point2 = (7, 2)

x1, y1 = point1
x2, y2 = point2

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("Point 1:", point1)
print("Point 2:", point2)
print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")
print("Distance between points:", distance)

chars = tuple("PYTHON")
print("Characters tuple:", chars)

for c in chars:
    print(c)

print("\n-----------------------------\n")

# =========================
# Question 4 – Sets
# =========================

print("QUESTION 4 – Class Attendance\n")

monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

both = monday_class & wednesday_class
either = monday_class | wednesday_class
only_monday = monday_class - wednesday_class
only_one = monday_class ^ wednesday_class

print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)
print("Attended both classes:", both)
print("Attended either class:", either)
print("Only Monday:", only_monday)
print("Only one class (not both):", only_one)
print("Is Monday subset of all students?", monday_class <= either)

print("\n-----------------------------\n")

# =========================
# Question 5 – Dictionary
# =========================

print("QUESTION 5 – Contact Book\n")

contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print("Alice's number:", contacts["Alice"])

contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Total contacts:", len(contacts))

print("\n-----------------------------\n")

# =========================
# Question 6 – Inventory System
# =========================

print("QUESTION 6 – Inventory Management\n")

inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

print("=== Current Inventory ===")
for item, (price, qty) in inventory.items():
    print(f"{item} - Price: ${price}, Quantity: {qty}")

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

all_products = electronics | accessories
print("\nAll product categories:", all_products)

prices = [value[0] for value in inventory.values()]
print("\nPrice list:", prices)

prices.sort()
print("Sorted prices:", prices)
print("Lowest price: $", prices[0])
print("Highest price: $", prices[-1])

inventory["Headphones"] = (49.99, 20)

mouse_price = inventory["Mouse"][0]
inventory["Mouse"] = (mouse_price, 12)

del inventory["Monitor"]

print("\n=== Final Inventory ===")
for item, (price, qty) in inventory.items():
    print(f"{item} - Price: ${price}, Quantity: {qty}")
