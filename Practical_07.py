# Practical 7: Introduction to Programming


# Q1. Lists and tuples
numbers = [10, 20, 30, 40]
names = ("Asha", "Riya", "Neha")
print(numbers, type(numbers))
print(names, type(names))


# Q2. Indexing list and tuple
items = [10, 20, 30, 40, 50]
names = ("A", "B", "C", "D", "E")
print(items[0], items[-1], items[len(items)//2])
print(names[0], names[-1], names[len(names)//2])


# Q3. Slicing lists and tuples
items = [10, 20, 30, 40, 50]
values = tuple(items)
for label, sequence in (("List", items), ("Tuple", values)):
    print(label, "first 3:", sequence[:3])
    print(label, "last 2:", sequence[-2:])
    print(label, "alternate:", sequence[::2])


# Q4. List mutability vs tuple immutability
numbers = [1, 2, 3]
numbers[0] = 99
print("Modified list:", numbers)
values = (1, 2, 3)
try:
    values[0] = 99
except TypeError as error:
    print("Tuple cannot be changed directly:", error)
print("Tuples are immutable; make a new tuple if changes are needed.")


# Q5. Add elements
items = [10, 20, 30]
items.append(40)
items.insert(1, 15)
print(items)


# Q6. Remove elements and handle missing item
items = [10, 20, 30, 40]
items.remove(20)
print("After remove(20):", items)
print("pop() returned:", items.pop())
try:
    items.remove(99)
except ValueError:
    print("Cannot remove 99: it is not present in the list.")
print("Final list:", items)


# Q7. Sort and reverse list
items = [5, 2, 9, 1, 7]
ascending = sorted(items)
descending = sorted(items, reverse=True)
print("Ascending:", ascending)
print("Descending:", descending)
items.reverse()
print("Original list reversed:", items)


# Q8. Tuple count and index with missing-item handling
values = (1, 2, 3, 2, 4, 2)
print("Count of 2:", values.count(2))
print("Index of 3:", values.index(3))
try:
    print(values.index(99))
except ValueError:
    print("99 is not present in the tuple.")


# Q9. Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)
print("Row 2:", matrix[1], "Element:", matrix[2][1])


# Q10. Convert list and tuple
items = [1, 2, 3]
values = tuple(items)
print(values)
print(list(values))


# Q11. Iterate lists and tuples
items = [1, 2, 3]
values = ("red", "green", "blue")
for item in items: print(item)
for value in values: print(value)


# Q12. Shopping cart
cart = ["notebook", "pen"]
cart.append(input("Add item: "))
remove_item = input("Item to remove (or press Enter): ").strip()
if remove_item in cart: cart.remove(remove_item)
print("Cart:", cart, "Total items:", len(cart))


# Q13. 2D list basic indexing
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Element at row 2, column 3:", matrix[1][2])


# Q14. 2D list row and column access
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Second row:", matrix[1])
print("Third column:", [row[2] for row in matrix])


# Q15. Negative indexing in 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Last row:", matrix[-1])
print("Last column:", [row[-1] for row in matrix])
print("Bottom-right:", matrix[-1][-1])


# Q16. Slicing rows in 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print("First two rows:", matrix[0:2])
print("Last two rows:", matrix[-2:])


# Q17. Partial slicing and submatrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sub = [row[0:2] for row in matrix[0:2]]
print("Top-left 2x2 submatrix:", sub)
print("Lists need a loop/comprehension to slice rows and columns together.")


# Q18. NumPy basic indexing
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element at (1, 2):", arr[1, 2])
print("First row:", arr[0, :])
print("Second column:", arr[:, 1])


# Q19. NumPy row and column slicing
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("First two rows:", arr[0:2, :])
print("Last column:", arr[:, -1])


# Q20. NumPy submatrix extraction
import numpy as np
arr = np.arange(1, 17).reshape(4, 4)
print("Middle 2x2 matrix:", arr[1:3, 1:3])
print("NumPy supports direct row-and-column slicing.")


# ==================== PRACTICE QUESTIONS ====================

# Q1. Add the new book ID at the front and remove the oldest entry.
book_ids = [1045, 1098, 1120, 1087, 1155, 1178, 1201, 1199, 1180, 1166, 1134, 1102]
book_ids.insert(0, 1215)
book_ids.pop()
print(book_ids)

# Q2. Display x, y, and altitude separately from coordinate tuples.
points = [(10,20,150),(15,25,160),(20,30,170),(25,35,180),(30,40,190),(35,45,200),(40,50,210),(45,55,220),(50,60,230),(55,65,240)]
print("X:", [p[0] for p in points])
print("Y:", [p[1] for p in points])
print("Altitude:", [p[2] for p in points])

# Q3. Update the night shift on day 5.
shifts = [["Dr A","Dr B","Dr C"],["Dr D","Dr E","Dr F"],["Dr G","Dr H","Dr I"],["Dr J","Dr K","Dr L"],["Dr M","Dr N","Dr O"],["Dr P","Dr Q","Dr R"],["Dr S","Dr T","Dr U"]]
shifts[4][2] = "Dr Z"
print(shifts[4])

# Q4. Remove duplicate songs while keeping the original order.
songs = ["Shape of You","Believer","Perfect","Believer","Faded","Perfect","Senorita","Levitating","Faded","Perfect","Blinding Lights","Senorita","Peaches","Believer","Perfect"]
unique_songs = list(dict.fromkeys(songs))
print(unique_songs)

# Q5. Show why tuple items cannot be changed directly.
calibration = [(0,0),(10,5),(20,10),(30,15),(40,20)]
try:
    calibration[2] = (25,12)
except TypeError as error:
    print("Tuple cannot be changed:", error)
calibration = calibration[:2] + [(25,12)] + calibration[3:]
print(calibration)

# Q6. Split quiz scores into midterm and final scores.
scores = [78,85,91,88,76,95,89,84]
midterm, final = scores[:4], scores[4:]
print("Midterm:", midterm, "Final:", final)
print("Highest:", max(scores), "Average:", sum(scores) / len(scores))

# Q7. Add a meal and sort the menu by price.
meals = [["Veg Burger",120],["Pizza Slice",90],["Pasta Bowl",150],["Sandwich",80]]
meals.append(["Noodles",110])
meals.sort(key=lambda meal: meal[1])
print(meals)

# Q8. Slice route points and reverse the route.
route = [(18.5204,73.8567),(18.5210,73.8575),(18.5221,73.8580),(18.5232,73.8591),(18.5243,73.8602),(18.5254,73.8613),(18.5265,73.8624),(18.5276,73.8635),(18.5287,73.8646),(18.5298,73.8657)]
print("Alternate checkpoints:", route[::2])
print("First five:", route[:5])
print("Reverse route:", route[::-1])

# Q9. Find top three prices and the lowest-price slot.
prices = [210,215,208,220,225,230,218,240,235,245]
top_three = sorted(prices, reverse=True)[:3]
print("Top three prices:", top_three)
print("Positions (1-based):", [prices.index(price) + 1 for price in top_three])
print("Lowest-price slot:", prices.index(min(prices)) + 1)

# Q10. Count room ID occurrences and find an index.
rooms = ("A101","A102","A103","B201","B202","B203","C301","C302","C303","A101","B201")
print("A101 count:", rooms.count("A101"))
print("C302 index:", rooms.index("C302"))
print("Room categories:", sorted(set(room[0] for room in rooms)))
