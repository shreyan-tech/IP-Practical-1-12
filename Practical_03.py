# Practical 3: Introduction to Programming


# Q1. Basic if
n = float(input("Enter a number: "))
if n > 0:
    print("Positive number")


# Q2. Even or odd
n = int(input("Enter an integer: "))
print("Even" if n % 2 == 0 else "Odd")


# Q3. Grade using elif
marks = float(input("Enter marks: "))
if marks >= 90: grade = "A"
elif marks >= 75: grade = "B"
elif marks >= 50: grade = "C"
else: grade = "Fail"
print("Grade:", grade)


# Q4. Voting eligibility
age = int(input("Enter age: "))
nationality = input("Enter nationality: ").strip().lower()
if age >= 18:
    if nationality == "indian": print("Eligible to vote, subject to voter registration.")
    else: print("Nationality requirement not met.")
else: print("Not eligible by age.")


# Q5. Largest of three
a, b, c = map(float, input("Enter three numbers: ").split())
if a >= b and a >= c: largest = a
elif b >= a and b >= c: largest = b
else: largest = c
print("Largest:", largest)


# Q6. Leap year
year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0): print("Leap year")
else: print("Not a leap year")


# Q7. Simple calculator
a = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Second number: "))
if op == "+": print(a + b)
elif op == "-": print(a - b)
elif op == "*": print(a * b)
elif op == "/":
    print(a / b if b != 0 else "Cannot divide by zero")
else: print("Invalid operator")


# Q8. Discount system
amount = float(input("Purchase amount: "))
discount = 0.20 if amount >= 2000 else 0.10 if amount >= 1000 else 0
print("Discount:", amount * discount)
print("Final amount:", amount * (1 - discount))


# Q9. Triangle type
a, b, c = map(float, input("Enter three side lengths: ").split())
if min(a, b, c) <= 0 or a+b <= c or a+c <= b or b+c <= a:
    print("Invalid triangle")
elif a == b == c: print("Equilateral")
elif a == b or b == c or a == c: print("Isosceles")
else: print("Scalene")


# Q10. Menu-driven program
print("1. Even/odd  2. Largest of three  3. Grade")
choice = input("Choose 1, 2 or 3: ")
if choice == "1":
    n = int(input("Number: ")); print("Even" if n % 2 == 0 else "Odd")
elif choice == "2":
    nums = list(map(float, input("Three numbers: ").split())); print("Largest:", max(nums))
elif choice == "3":
    m = float(input("Marks: "))
    print("A" if m >= 90 else "B" if m >= 75 else "C" if m >= 50 else "Fail")
else: print("Invalid choice")


# ==================== PRACTICE QUESTIONS ====================

# Q1. Check placement eligibility.
cgpa = float(input("CGPA: "))
attendance = float(input("Attendance percentage: "))
print("Eligible" if cgpa >= 7 and attendance >= 75 else "Not eligible")

# Q2. Check loan approval.
salary = float(input("Monthly salary: ₹"))
credit_score = int(input("Credit score: "))
print("Loan approved" if salary >= 30000 and credit_score > 700 else "Loan not approved")

# Q3. Calculate discount on a purchase.
amount = float(input("Purchase amount: ₹"))
if amount > 5000:
    discount_rate = 15
elif amount > 2000:
    discount_rate = 10
else:
    discount_rate = 0
print("Discount: ₹", amount * discount_rate / 100)
print("Final amount: ₹", amount * (1 - discount_rate / 100))

# Q4. Check voting eligibility with nested if.
age = int(input("Age: "))
nationality = input("Nationality: ").strip().lower()
if age >= 18:
    if nationality == "indian":
        print("Eligible to vote")
    else:
        print("Must be an Indian citizen")
else:
    print("Too young to vote")

# Q5. Calculate parking charges, capped at ₹100 per day.
hours = int(input("Hours parked: "))
charge = 0 if hours <= 0 else 20 + max(0, hours - 1) * 10
print("Parking charge: ₹", min(charge, 100))

# Q6. Classify age group.
age = int(input("Age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# Q7. Check scholarship eligibility.
marks = float(input("Marks: "))
income = float(input("Family income: ₹"))
print("Scholarship eligible" if marks > 85 and income < 300000 else "Not eligible")

# Q8. Display recharge benefits.
amount = float(input("Recharge amount: ₹"))
if amount >= 299:
    print("2 GB/day")
elif amount >= 199:
    print("1 GB/day")
else:
    print("Talktime benefits")

# Q9. Classify systolic blood pressure.
bp = int(input("Systolic blood pressure: "))
if bp < 120:
    print("Normal")
elif bp < 130:
    print("Elevated")
elif bp < 140:
    print("High Stage 1")
else:
    print("High Stage 2")

# Q10. Calculate employee bonus from years of service.
years = int(input("Years of service: "))
salary = float(input("Annual salary: ₹"))
rate = 20 if years >= 10 else 10 if years >= 5 else 0
print("Bonus: ₹", salary * rate / 100)
