# Practical 1: Introduction to Programming


# Q1. Variable creation and naming
name = "Shreya"
age = 18
marks = 85.5
city = "Mumbai"
print(name, age, marks, city)
# Variable names cannot start with digits, contain hyphens, or use keywords.


# Q2. Dynamic typing
value = 10
print(value, type(value))
value = "Hello"
print(value, type(value))
value = 3.14
print(value, type(value))


# Q3. Constants by convention
PI = 3.14159
GRAVITY = 9.8
MAX_USERS = 100
print(PI, GRAVITY, MAX_USERS)
# Uppercase names indicate constants by convention; Python does not enforce them.


# Q4. Data type identification
integer_value = int(input("Enter an integer: "))
float_value = float(input("Enter a decimal number: "))
string_value = input("Enter text: ")
boolean_value = input("Enter True or False: ").strip().lower() == "true"
for value in (integer_value, float_value, string_value, boolean_value):
    print(value, type(value))


# Q5. Type conversion
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
print("Age next year:", age + 1)
print("Marks after adding 5:", marks + 5)


# Q6. Implicit vs explicit conversion
a = 5
b = 2.5
print("int + float =", a + b)  # Python converts the int to float
try:
    print(5 + "2")
except TypeError as error:
    print("int + string causes TypeError:", error)
print("Fixed using explicit casting:", 5 + int("2"))


# Q7. Memory behavior and id
a = 100
b = a
print("IDs:", id(a), id(b))
b = 200
print("a =", a, "b =", b)


# Q8. Swap using two methods
a = input("Enter a: ")
b = input("Enter b: ")
# Method 1: third variable
x, y = a, b
temp = x
x = y
y = temp
print("Using third variable:", x, y)
# Method 2: tuple unpacking
x, y = a, b
x, y = y, x
print("Using tuple unpacking:", x, y)


# Q9. Data type based calculator
a = input("Enter first value: ")
b = input("Enter second value: ")
try:
    x, y = float(a), float(b)
    print("Both inputs are numeric; sum =", x + y)
except ValueError:
    if a.strip() and b.strip():
        print("At least one input is text; concatenation =", a + b)
    else:
        print("Invalid empty input.")


# Q10. Boolean logic
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
adult = age >= 18
passed = marks >= 50
print("Adult:", adult, "Passed:", passed)
if adult and passed:
    print("Both conditions are true.")


# Q11. Temperature converter
celsius = float(input("Temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius:.1f} C = {fahrenheit:.1f} F")


# ==================== PRACTICE QUESTIONS ====================

# Q1. Correct the invalid variable name.
name = "Python"
print(name)

# Q2. Convert age to an integer before adding 5.
age = "18"
print(int(age) + 5)

# Q3. Fix the undefined variable.
marks = 95
total_marks = marks
print(total_marks)

# Q4. Use Python's Boolean value correctly.
is_pass = True
print(is_pass)

# Q5. Convert a decimal string to float.
num = float("12.5")
print(num)

# Q6. Find the type after reassignment.
x = 10
x = "Python"
print(type(x))

# Q7. Convert the string to an integer before addition.
a = "20"
b = 5
print(int(a) + b)

# Q8. Predict the result of swapping two values.
a = 10
b = 20
a, b = b, a
print(a, b)

# Q9. Check whether age is greater than 18.
age = 19
print(age > 18)

# Q10. Convert Celsius to Fahrenheit.
c = 37
f = (c * 9 / 5) + 32
print(f)
