# Practical 5: Introduction to Programming


# Q1. break
for n in range(1, 11):
    if n == 5: break
    print(n)


# Q2. continue
for n in range(1, 11):
    if n == 5: continue
    print(n)


# Q3. Compare break and continue
print("break stops the loop:")
for n in range(1, 6):
    if n == 3: break
    print(n)
print("continue skips one iteration:")
for n in range(1, 6):
    if n == 3: continue
    print(n)


# Q4. Search in list
numbers = [12, 5, 8, 20, 7]
target = int(input("Search number: "))
for n in numbers:
    if n == target:
        print("Found"); break
else: print("Not found")


# Q5. First divisible number
for n in range(1, 101):
    if n % 7 == 0:
        print("First number divisible by 7:", n); break


# Q6. Skip negative numbers
numbers = [4, -2, 7, -1, 0, 9]
for n in numbers:
    if n < 0: continue
    print(n)


# Q7. Sum valid inputs
total = 0
for _ in range(5):
    value = input("Enter a number (or skip with blank): ").strip()
    if not value: continue
    try: total += float(value)
    except ValueError: print("Invalid input skipped")
print("Sum:", total)


# Q8. Password retry system
correct_password = "python123"
for attempt in range(3):
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted"); break
    print("Incorrect password")
else: print("Too many attempts")


# Q9. pass statement
for n in range(1, 6):
    if n == 3:
        pass  # Placeholder; no action is taken
    print(n)


# Q10. Pattern with conditional skipping
for i in range(1, 6):
    if i == 3: continue
    print("*" * i)


# ==================== PRACTICE QUESTIONS ====================

# Q1. Stop scanning when battery drops below 15%.
battery_readings = [80, 65, 42, 14, 10]
for battery in battery_readings:
    if battery < 15:
        print("Low battery detected:", battery)
        break
    print("Scanning field; battery:", battery)

# Q2. Skip duplicate RFID entries.
rfid_entries = [101, 102, 101, 103, 104, 102]
seen = set()
for card_id in rfid_entries:
    if card_id in seen:
        continue
    seen.add(card_id)
    print("Counted card:", card_id)

# Q3. Stop the queue when a critical case is found.
patients = ["routine", "routine", "critical", "routine"]
for patient in patients:
    if patient == "critical":
        print("Critical case: stop queue")
        break
    print("Processing", patient)

# Q4. Ignore damaged barcode value -1.
barcodes = [120, 135, -1, 145, 150]
for barcode in barcodes:
    if barcode == -1:
        continue
    print("Barcode:", barcode)

# Q5. Allow at most five PIN attempts.
correct_pin = "123456"
for attempt in range(5):
    pin = input("Enter 6-digit PIN: ")
    if pin == correct_pin:
        print("Access granted")
        break
    print("Incorrect PIN")
else:
    print("Too many failed attempts")

# Q6. Skip faulty negative sensor readings while calculating average.
temperatures = [22, 24, -5, 23, 25, -2]
valid = []
for temp in temperatures:
    if temp < 0:
        continue
    valid.append(temp)
print("Average temperature:", sum(valid) / len(valid) if valid else "No valid readings")

# Q7. Use pass as a placeholder for future checks.
plagiarism_check_enabled = False
if plagiarism_check_enabled:
    pass
else:
    print("Plagiarism check is not enabled yet")

# Q8. Stop inspection at the first defective product.
products = ["good", "good", "defective", "good"]
for index, product in enumerate(products, start=1):
    if product == "defective":
        print("Defective product:", index)
        break

# Q9. Skip weekend days in a 30-day analysis.
for day in range(1, 31):
    weekday = (day - 1) % 7  # 0=Monday, 5=Saturday, 6=Sunday
    if weekday >= 5:
        continue
    print("Analyze day", day)

# Q10. Stop after the same suspicious IP appears three times.
login_ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.1", "10.0.0.3"]
counts = {}
for ip in login_ips:
    counts[ip] = counts.get(ip, 0) + 1
    if counts[ip] >= 3:
        print("Intrusion alert:", ip)
        break
