# Practical 4: Introduction to Programming


# Q1. For loop and range
for i in range(1, 11): print(i)
print("Even numbers:")
for i in range(2, 11, 2): print(i)


# Q2. While loop
n = 1
while n <= 10:
    print(n)
    n += 1


# Q3. Sum and average
n = int(input("How many numbers? "))
total = 0
for i in range(n):
    total += float(input(f"Number {i+1}: "))
print("Sum:", total, "Average:", total / n if n > 0 else 0)


# Q4. Factorial
n = int(input("Enter a non-negative integer: "))
if n < 0: print("Factorial is not defined for negative numbers")
else:
    fact = 1
    for i in range(1, n + 1): fact *= i
    print("Factorial:", fact)


# Q5. Multiplication table
n = int(input("Enter number: "))
for i in range(1, 11): print(f"{n} x {i} = {n*i}")


# Q6. Reverse and palindrome
n = input("Enter an integer: ")
rev = n[::-1]
print("Reverse:", rev)
print("Palindrome" if n == rev else "Not palindrome")


# Q7. Count digits, even and odd
n = input("Enter a positive integer: ")
digits = [int(ch) for ch in n if ch.isdigit()]
print("Digits:", len(digits))
print("Even digits:", sum(d % 2 == 0 for d in digits))
print("Odd digits:", sum(d % 2 != 0 for d in digits))


# Q8. Prime checker
n = int(input("Enter integer: "))
is_prime = n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
print("Prime" if is_prime else "Not prime")


# Q9. Fibonacci series
n = int(input("How many terms? "))
a, b = 0, 1
for _ in range(max(0, n)):
    print(a, end=" ")
    a, b = b, a + b
print()


# Q10. Nested loop pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# ==================== PRACTICE QUESTIONS ====================

# Q1. Print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

# Q2. Predict the output of the loop.
for i in range(1, 6):
    print(i)

# Q3. Print a 3 by 3 star pattern.
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# Q4. Generate the first five Fibonacci numbers.
a, b = 0, 1
for i in range(5):
    print(a, end=" ")
    a, b = b, a + b
print()

# Q5. Increment the counter so the while loop ends.
num = 1
while num <= 5:
    print(num)
    num += 1

# Q6. Print the first five multiples of 2.
i = 1
while i <= 5:
    print(i * 2)
    i += 1

# Q7. Calculate factorial of 4.
fact = 1
for i in range(1, 5):
    fact *= i
print(fact)

# Q8. Correct factorial logic by starting from 1.
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

# Q9. Display the first five Fibonacci numbers.
a, b = 0, 1
for i in range(5):
    print(a, end=" ")
    a, b = b, a + b
print()

# Q10. Print a growing triangle of stars.
for i in range(3):
    for j in range(i + 1):
        print("*", end="")
    print()
