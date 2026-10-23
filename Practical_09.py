# Practical 9: Introduction to Programming


# Q1. Define and call function
def greet():
    print("Hello! Welcome to Python.")
greet()
greet()


# Q2. Function with parameters
def greet(name):
    print("Hello", name)
greet(input("Enter name: "))


# Q3. Return value
def add(a, b):
    return a + b
print("Sum:", add(10, 20))


# Q4. Default and keyword arguments
def student(name, course="BSc CS AI & ML"):
    print(name, course)
student("Asha")
student(course="BSc CS AI & ML", name="Riya")


# Q5. Built-in functions
numbers = [12, 5, 20, 8]
print(len(numbers), sum(numbers), max(numbers), min(numbers))


# Q6. List processing function
def process(numbers):
    return sum(numbers), max(numbers), min(numbers)
nums = list(map(float, input("Enter numbers separated by spaces: ").split()))
print("Sum, max, min:", process(nums))


# Q7. Recursive factorial
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)
n = int(input("Non-negative integer: "))
print(factorial(n) if n >= 0 else "Invalid input")


# Q8. Recursive Fibonacci
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)
count = int(input("Number of terms (up to 20): "))
print([fibonacci(i) for i in range(max(0, min(count, 20)))])


# Q9. Function calling function
def square(n): return n*n
def sum_of_squares(a, b): return square(a) + square(b)
print(sum_of_squares(3, 4))


# Q10. Local and global scope
message = "global"
def show():
    message = "local"
    print("Inside function:", message)
show()
print("Outside function:", message)


# Q11. Menu-driven functions
def even_odd(n): return "Even" if n % 2 == 0 else "Odd"
def square(n): return n*n
choice = input("1 Even/Odd, 2 Square: ")
n = int(input("Number: "))
if choice == "1": print(even_odd(n))
elif choice == "2": print(square(n))
else: print("Invalid choice")


# Q12. Student result function
def result(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return total, percentage, ("Pass" if all(m >= 35 for m in marks) else "Fail")
marks = [float(input(f"Subject {i+1} marks: ")) for i in range(3)]
print("Total, percentage, result:", result(marks))


# ==================== PRACTICE QUESTIONS ====================

# Q1. Calculate average battery drop per hour and warn if it exceeds 5%.
def average_drop(values):
    drop = (values[0] - values[-1]) / (len(values) - 1)
    if drop > 5:
        print("Warning: average drop is above 5% per hour")
    return drop
print("Average drop:", average_drop([92, 88, 84, 79, 73, 68]))

# Q2. Calculate BMI and return its category.
def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 2), category
print(calculate_bmi(72, 1.75))

# Q3. Recursively find the sum of digits in a PIN.
def digit_sum(pin):
    if pin == 0:
        return 0
    return pin % 10 + digit_sum(pin // 10)
print(digit_sum(482931))

# Q4. Calculate final bill after discount and GST.
def bill_amount(price, discount, gst):
    discounted_price = price - price * discount / 100
    return discounted_price + discounted_price * gst / 100
print("Final bill: ₹", bill_amount(2500, 10, 18))

# Q5. Clean text, convert it to lowercase, and count words.
def sanitize_text(text):
    cleaned = " ".join(text.split()).lower()
    return cleaned, len(cleaned.split())
print(sanitize_text("Python Makes AI Easy"))

# Q6. Add two numbers using a function.
def add(a, b):
    return a + b
print(add(5, 3))

# Q7. Call a function with its default argument.
def greet(name="Student"):
    print("Hello", name)
greet()

# Q8. Calculate factorial recursively.
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)
print(fact(4))

# Q9. Correct the missing colon in the function definition.
def add(a, b):
    return a + b
print(add(2, 3))

# Q10. Correct the indentation inside the function.
def square(x):
    print(x * x)
square(5)
