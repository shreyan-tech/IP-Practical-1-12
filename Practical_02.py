# Practical 2: Introduction to Programming


# Q1. Name and age input
name = input("Enter name: ")
age = int(input("Enter age: "))
print("Name:", name, "Age:", age)
print(f"My name is {name} and I am {age} years old.")


# Q2. Arithmetic with two numbers
a = float(input("First number: "))
b = float(input("Second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
else:
    print("Cannot divide by zero.")


# Q3. Sum, average and expression
a, b, c = map(float, input("Enter three numbers separated by spaces: ").split())
print("Sum:", a + b + c)
print("Average:", (a + b + c) / 3)
print("(a + b) * c / 2:", (a + b) * c / 2)


# Q4. Operator precedence
print(10 + 5 * 2)
print((10 + 5) * 2)
print(100 / 5 + 3 * 2)


# Q5. Salary breakdown
salary = float(input("Basic salary: "))
hra = salary * 0.20
da = salary * 0.10
net_salary = salary + hra + da
print(f"Basic: Rs.{salary:.2f}\nHRA: Rs.{hra:.2f}\nDA: Rs.{da:.2f}\nNet salary: Rs.{net_salary:.2f}")


# Q6. Area and perimeter
import math
length = float(input("Rectangle length: "))
width = float(input("Rectangle width: "))
print("Rectangle area:", length * width)
print("Rectangle perimeter:", 2 * (length + width))
radius = float(input("Circle radius: "))
print("Circle area:", math.pi * radius ** 2)
print("Circumference:", 2 * math.pi * radius)


# Q7. Unit conversion
km = float(input("Kilometres: "))
celsius = float(input("Celsius: "))
rupees = float(input("Rupees: "))
print("Metres:", km * 1000)
print("Fahrenheit:", celsius * 9 / 5 + 32)
print("Dollars at fixed rate Rs.83/$:", rupees / 83)


# Q8. Single-line inputs
a, b, c = map(float, input("Enter a, b, c separated by spaces: ").split())
print(f"Sum = {a+b+c}; Product = {a*b*c}")


# Q9. Grading system
marks = [float(input(f"Marks for subject {i+1}: ")) for i in range(3)]
total = sum(marks)
percentage = total / 3
grade = "A" if percentage >= 90 else "B" if percentage >= 75 else "C" if percentage >= 50 else "Fail"
print("Total:", total, "Percentage:", percentage, "Grade:", grade)


# Q10. Expression error handling
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: division by zero is not allowed.")
try:
    print("Age: " + 18)
except TypeError:
    print("Error: convert the number to a string before joining.")
print("Correct:", "Age: " + str(18))


# ==================== PRACTICE QUESTIONS ====================

# Q1. Calculate an electricity bill: ₹150 fixed for up to 100 units, then ₹6 per extra unit.
units = int(input("Units consumed: "))
fixed_charge = 150
variable_charge = max(0, units - 100) * 6
print("Fixed charge: ₹", fixed_charge)
print("Variable charge: ₹", variable_charge)
print("Total payable: ₹", fixed_charge + variable_charge)

# Q2. Calculate average speed.
distance = float(input("Distance in km: "))
time = float(input("Time in hours: "))
if time > 0:
    print("Average speed:", distance / time, "km/h")
else:
    print("Time must be greater than zero.")

# Q3. Apply discount first, then GST.
bill = 2500
discount = bill * 10 / 100
after_discount = bill - discount
gst = after_discount * 18 / 100
print("Discount: ₹", discount)
print("GST: ₹", gst)
print("Net bill: ₹", after_discount + gst)

# Q4. Compare arithmetic expressions.
a, b = 25, 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Integer division:", a // b)
print("Float division:", a / b)

# Q5. Estimate fuel cost for a trip.
distance = 240
mileage = 15
price_per_litre = 105
fuel_needed = distance / mileage
print("Fuel needed:", fuel_needed, "litres")
print("Fuel cost: ₹", fuel_needed * price_per_litre)

# Q6. Find the topper and their position.
marks = list(map(int, input("Enter 5 marks separated by spaces: ").split()))
topper_marks = max(marks)
print("Topper's marks:", topper_marks)
print("Student position:", marks.index(topper_marks) + 1)

# Q7. Estimate simple-interest EMI per month.
loan = 500000
months = 24
rate = 12
interest = loan * rate * (months / 12) / 100
print("Monthly payment: ₹", (loan + interest) / months)

# Q8. Verify operator precedence.
expressions = ["10 + 5 * 2", "(10 + 5) * 2", "100 / 5 + 3 * 2", "50 - 6 / 2", "8 + 2 ** 3"]
for expression in expressions:
    print(expression, "=", eval(expression))

# Q9. Calculate a bill with tip and split it between friends.
bill = 1800
tip = bill * 8 / 100
total = bill + tip
print("Tip: ₹", tip)
print("Final bill: ₹", total)
print("Each friend pays: ₹", total / 4)

# Q10. Calculate BMI and display its category.
weight = 72
height = 1.75
bmi = weight / (height ** 2)
print("BMI:", round(bmi, 2))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
