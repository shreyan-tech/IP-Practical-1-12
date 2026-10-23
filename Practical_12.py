# Practical 12: Introduction to Programming


# Q1. Basic try except division
try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Q2. Handle different errors
try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Sum:", a+b, "Division:", a/b)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Second number cannot be zero.")


# Q3. try except else
try:
    a = float(input("Numerator: "))
    b = float(input("Denominator: "))
    result = a / b
except (ValueError, ZeroDivisionError) as error:
    print("Operation failed:", error)
else:
    print("Division successful:", result)


# Q4. finally cleanup
try:
    file = open("sample.txt", "r", encoding="utf-8")
    print(file.readline())
except FileNotFoundError:
    print("File not found.")
finally:
    try: file.close(); print("File closed.")
    except NameError: print("No file was opened.")


# Q5. Capture exception details
try:
    number = int(input("Enter an integer: "))
    print(10 / number)
except Exception as error:
    print("Error occurred:", error)


# Q6. Repeat until valid integer
while True:
    try:
        number = int(input("Enter an integer: "))
        print("Valid number:", number)
        break
    except ValueError:
        print("Invalid input. Try again.")


# Q7. Friendly invalid operation messages
try:
    a = float(input("First number: "))
    op = input("Operator (+, -, *, /): ")
    b = float(input("Second number: "))
    if op == "+": print(a+b)
    elif op == "-": print(a-b)
    elif op == "*": print(a*b)
    elif op == "/":
        if b == 0: print("Cannot divide by zero.")
        else: print(a/b)
    else: print("Please choose a valid operator.")
except ValueError:
    print("Please enter numbers only.")


# Q8. Raise exception for age
try:
    age = int(input("Enter age: "))
    if age < 18: raise ValueError("Age must be at least 18.")
    print("Age requirement satisfied.")
except ValueError as error:
    print("Invalid age:", error)


# Q9. Custom exception for marks
class InvalidMarksError(Exception):
    pass
try:
    marks = float(input("Enter marks from 0 to 100: "))
    if not 0 <= marks <= 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    print("Marks accepted:", marks)
except (ValueError, InvalidMarksError) as error:
    print("Invalid marks:", error)


# Q10. Bank withdrawal
balance = 5000
try:
    amount = float(input("Withdrawal amount: "))
    if amount <= 0: raise ValueError("Amount must be positive.")
    if amount > balance: raise ValueError("Insufficient balance.")
    balance -= amount
    print("Withdrawal successful. Remaining balance:", balance)
except ValueError as error:
    print("Transaction failed:", error)


# Q11. Compare exception handling
# Without handling, invalid input may stop the program.
# With try-except, the program displays a friendly message.
try:
    number = int(input("Enter an integer: "))
    print("Number:", number)
except ValueError:
    print("Handled: please enter a whole number.")


# Q12. Nested exception handling
try:
    numbers = [10, 20, 30]
    index = int(input("List index (0 to 2): "))
    try:
        divisor = float(input("Divisor: "))
        print("Value:", numbers[index] / divisor)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except IndexError:
        print("Index is outside the list.")
except ValueError:
    print("Please enter numeric input.")


# ==================== PRACTICE QUESTIONS ====================

# Q1. Raise a custom exception when battery is below 15%.
class LowBatteryError(Exception):
    pass

battery = 12
try:
    if battery < 15:
        raise LowBatteryError("Battery is too low for flight")
    print("Continue flight calculations safely")
except LowBatteryError as error:
    print(error)

# Q2. Validate patient age and dosage, and always run cleanup.
class InvalidDosageError(Exception):
    pass

try:
    age = 25
    dosage = 1200
    if age < 1 or dosage <= 0 or dosage > 1000:
        raise InvalidDosageError("Invalid age or dosage")
    print("Dosage accepted")
except InvalidDosageError as error:
    print(error)
finally:
    print("Validation completed")

# Q3. Raise an exception after three failed login attempts.
class SuspiciousLoginError(Exception):
    pass

try:
    failed_attempts = 3
    if failed_attempts >= 3:
        raise SuspiciousLoginError("Too many failed attempts")
except SuspiciousLoginError as error:
    print(error)
finally:
    print("Login check finished")

# Q4. Handle missing file, invalid data, division by zero, and faulty readings.
try:
    with open("temperatures.txt", "r", encoding="utf-8") as file:
        values = [float(line.strip()) for line in file if line.strip()]
    values = [value for value in values if value >= -100]
    if not values:
        raise ZeroDivisionError("No valid sensor readings")
    print("Average temperature:", sum(values) / len(values))
except FileNotFoundError:
    print("Temperature file was not found")
except ValueError:
    print("File contains an invalid temperature")
except ZeroDivisionError as error:
    print(error)

# Q5. Validate labels and reject blanks, digits, and too many duplicates.
class InvalidLabelError(Exception):
    pass

labels = ["cat", "dog", "cat", "bird", "cat", ""]
try:
    if any(not label.strip() for label in labels):
        raise InvalidLabelError("Label cannot be blank")
    if any(any(ch.isdigit() for ch in label) for label in labels):
        raise InvalidLabelError("Labels cannot contain digits")
    duplicates = len(labels) - len(set(labels))
    if duplicates > 1:
        raise InvalidLabelError("Duplicate labels exceed the allowed limit")
except InvalidLabelError as error:
    print(error)
except Exception as error:
    print("Unexpected error:", error)

# Q6. Handle division by zero and run finally.
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Math Error")
finally:
    print("Done")

# Q7. Show the ValueError, else, and finally flow.
try:
    num = int("25A")
except ValueError:
    print("Invalid")
else:
    print("Valid")
finally:
    print("Closed")

# Q8. Handle an invalid list index.
try:
    data = [1, 2, 3]
    print(data[5])
except IndexError:
    print("Out of Range")
finally:
    print("Execution Complete")

# Q9. Fill the blanks: divide by zero and catch ZeroDivisionError.
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Division error")
finally:
    print("Completed")

# Q10. Define and raise a user-defined exception.
class LowMarksError(Exception):
    pass

marks = 25
try:
    if marks < 35:
        raise LowMarksError("Fail")
except LowMarksError as error:
    print(error)
