# Practical 8: Introduction to Programming


# Q1. Create dictionary
student = {"name": "Asha", "age": 18, "marks": 85}
print(student, type(student))


# Q2. Access values
student = {"name": "Asha", "age": 18, "marks": 85}
print(student["name"], student["marks"])


# Q3. get method
student = {"name": "Asha", "marks": 85}
print(student.get("name"))
print(student.get("age", "Not available"))


# Q4. Add and update
student = {"name": "Asha", "marks": 80}
student["age"] = 18
student["marks"] = 90
print(student)


# Q5. Remove elements
student = {"name": "Asha", "age": 18, "marks": 85}
student.pop("age")
print(student)


# Q6. Iterate dictionary
student = {"name": "Asha", "age": 18, "marks": 85}
for key, value in student.items(): print(key, ":", value)


# Q7. keys values items
data = {"a": 1, "b": 2, "c": 3}
print(data.keys())
print(data.values())
print(data.items())


# Q8. Frequency counter
text = input("Enter a word or sentence: ").lower().split()
frequency = {}
for word in text: frequency[word] = frequency.get(word, 0) + 1
print(frequency)


# Q9. Nested dictionary
students = {"S1": {"name": "Asha", "marks": 85}, "S2": {"name": "Riya", "marks": 91}}
for roll, details in students.items(): print(roll, details["name"], details["marks"])


# Q10. Merge dictionaries
a = {"x": 1, "y": 2}
b = {"y": 9, "z": 3}
a.update(b)
print(a)


# Q11. Sort dictionary
marks = {"Riya": 88, "Asha": 95, "Neha": 79}
print(dict(sorted(marks.items())))
print(dict(sorted(marks.items(), key=lambda item: item[1], reverse=True)))


# Q12. Inventory system
inventory = {"pen": 10, "book": 5}
action = input("Choose add/update/remove: ").strip().lower()
product = input("Product name: ").strip().lower()
if action == "add": inventory[product] = int(input("Initial stock: "))
elif action == "update" and product in inventory: inventory[product] = int(input("New stock: "))
elif action == "remove": inventory.pop(product, None)
else: print("Unknown action or product not found")
print("Inventory:", inventory)


# ==================== PRACTICE QUESTIONS ====================

# Q1. Update classroom attendance and count present students.
attendance = {"S101":"Present", "S102":"Absent", "S103":"Present", "S104":"Late"}
attendance["S104"] = "Present"
attendance["S105"] = "Present"
print("Present students:", sum(status == "Present" for status in attendance.values()))

# Q2. Find the patient with the highest temperature and update P003.
patients = {"P001":{"name":"Asha","temp":98.6}, "P002":{"name":"Ravi","temp":101.2}, "P003":{"name":"Neha","temp":99.1}}
hottest = max(patients, key=lambda patient: patients[patient]["temp"])
print("Highest temperature:", patients[hottest]["name"], patients[hottest]["temp"])
patients["P003"]["temp"] = 100.4
print(patients["P003"])

# Q3. Update drone sensor details.
sensor = {"altitude":250,"speed":45,"battery":78,"gps":"ACTIVE"}
sensor["wind_speed"] = 12
sensor.pop("gps")
for key, value in sensor.items():
    print(key, value)

# Q4. Update inventory and remove out-of-stock products.
inventory = {"Laptop":12,"Mouse":40,"Keyboard":25,"Monitor":10}
inventory["Laptop"] -= 2
inventory["Printer"] = 5
inventory = {item: quantity for item, quantity in inventory.items() if quantity > 0}
print(inventory)

# Q5. Count each word in the chatbot text.
from collections import Counter
text = "python makes coding easy and python makes debugging easier"
word_count = Counter(text.split())
print(dict(word_count))

# Q6. Display a value from a dictionary.
student = {"name":"Asha","marks":92}
print(student["name"])

# Q7. Add a key and display dictionary length.
d = {"a":1,"b":2}
d["c"] = 3
print(len(d))

# Q8. Use get() to return a default for a missing key.
data = {"x":10,"y":20}
print(data.get("z", 0))

# Q9. Use quotes when accessing a string key.
student = {"name":"Ravi","marks":85}
print(student["name"])

# Q10. Add an item to a dictionary using a key assignment.
d = {"a":1,"b":2}
d["c"] = 3
print(d)
