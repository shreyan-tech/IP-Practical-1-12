# Practical 11: Introduction to Programming


# Q1. Write text file
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python\nThis is file handling.\n")
print("Data written to sample.txt")


# Q2. Read entire file
with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())


# Q3. Read line by line
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())


# Q4. Use with statement
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("First line\nSecond line\n")
with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())
# with automatically closes the file.


# Q5. Append to file
with open("sample.txt", "a", encoding="utf-8") as file:
    file.write("Appended line\n")
with open("sample.txt", "r", encoding="utf-8") as file: print(file.read())


# Q6. Count lines words characters
with open("sample.txt", "r", encoding="utf-8") as file: content = file.read()
print("Lines:", len(content.splitlines()))
print("Words:", len(content.split()))
print("Characters:", len(content))


# Q7. Search word occurrences
word = input("Word to search: ")
with open("sample.txt", "r", encoding="utf-8") as file: content = file.read()
print("Occurrences:", content.lower().count(word.lower()))


# Q8. Copy file content
with open("sample.txt", "r", encoding="utf-8") as source: content = source.read()
with open("copy.txt", "w", encoding="utf-8") as target: target.write(content)
print("Copied to copy.txt")


# Q9. Filter lines by keyword
keyword = input("Keyword: ").lower()
with open("sample.txt", "r", encoding="utf-8") as source: lines = source.readlines()
matches = [line for line in lines if keyword in line.lower()]
with open("filtered.txt", "w", encoding="utf-8") as target: target.writelines(matches)
print("Matching lines written to filtered.txt")


# Q10. Student record file
with open("students.txt", "a", encoding="utf-8") as file:
    name = input("Student name: ")
    roll = input("Roll number: ")
    marks = input("Marks: ")
    file.write(f"{roll},{name},{marks}\n")
with open("students.txt", "r", encoding="utf-8") as file:
    print("Roll, Name, Marks")
    print(file.read())


# Q11. File exception handling
try:
    with open("missing_file.txt", "r", encoding="utf-8") as file: print(file.read())
except FileNotFoundError:
    print("The requested file does not exist.")


# Q12. Replace word in file
with open("sample.txt", "r", encoding="utf-8") as file: content = file.read()
old = input("Word to replace: ")
new = input("Replacement: ")
content = content.replace(old, new)
with open("sample.txt", "w", encoding="utf-8") as file: file.write(content)
print("File updated.")


# ==================== PRACTICE QUESTIONS ====================

# Q1. Append five drone logs and count entries with battery below 50.
logs = ["ALT=250,SPD=45,BAT=78", "ALT=240,SPD=42,BAT=45", "ALT=260,SPD=48,BAT=62", "ALT=230,SPD=40,BAT=30", "ALT=255,SPD=46,BAT=51"]
with open("flight_log.txt", "a", encoding="utf-8") as file:
    for log in logs:
        file.write(log + "\n")
with open("flight_log.txt", "r", encoding="utf-8") as file:
    saved_logs = file.readlines()
print("All logs:")
print("".join(saved_logs))
print("Battery below 50:", sum(int(line.split("BAT=")[1]) < 50 for line in saved_logs if "BAT=" in line))

# Q2. Save five patient notes and display lines containing critical.
notes = ["Patient stable", "Critical condition reported", "Routine check complete", "Critical care required", "Patient discharged"]
with open("patient_notes.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(notes))
with open("patient_notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "critical" in line.lower():
            print(line.strip())

# Q3. Append login attempts and copy failed attempts to a separate file.
attempts = ["user=admin,status=FAILED", "user=riya,status=SUCCESS", "user=guest,status=FAILED"]
with open("audit_log.txt", "a", encoding="utf-8") as file:
    file.write("\n".join(attempts) + "\n")
with open("audit_log.txt", "r", encoding="utf-8") as source:
    failed = [line for line in source if "FAILED" in line]
with open("threat_log.txt", "w", encoding="utf-8") as destination:
    destination.writelines(failed)
print("Failed log entries:", len(failed))

# Q4. Store prompts, remove blank lines, and find average words per prompt.
prompts = ["Explain Python loops", "Write a simple function", "", "Describe list methods", "Explain file handling", "What is a dictionary", "Show string slicing", "Explain exceptions", "Define a tuple", "What is NumPy"]
with open("prompt_bank.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(prompts))
with open("prompt_bank.txt", "r", encoding="utf-8") as file:
    cleaned = [line.strip() for line in file if line.strip()]
with open("prompt_bank.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(cleaned))
print("Average words per prompt:", sum(len(line.split()) for line in cleaned) / len(cleaned))

# Q5. Save seven weather records and find the highest temperature day.
weather = ["TEMP=32,HUM=70,WIND=15", "TEMP=34,HUM=65,WIND=12", "TEMP=30,HUM=80,WIND=10", "TEMP=36,HUM=60,WIND=18", "TEMP=31,HUM=75,WIND=14", "TEMP=35,HUM=62,WIND=16", "TEMP=29,HUM=82,WIND=9"]
with open("weather.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(weather))
with open("weather.txt", "r", encoding="utf-8") as file:
    records = [line.strip() for line in file]
hottest = max(records, key=lambda line: int(line.split(",")[0].split("=")[1]))
print("Highest temperature record:", hottest)

# Q6. Write and read a file; readline() reads only the first line.
with open("demo.txt", "w", encoding="utf-8") as file:
    file.write("Python\nAI")
with open("demo.txt", "r", encoding="utf-8") as file:
    print(file.readline().strip())
print("Done")

# Q7. Count lines in a file.
with open("demo.txt", "w", encoding="utf-8") as file:
    file.write("A\nB\nC")
with open("demo.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
print(len(lines))

# Q8. Append to a file and display the content.
with open("demo.txt", "w", encoding="utf-8") as file:
    file.write("DATA")
with open("demo.txt", "a", encoding="utf-8") as file:
    file.write("SCIENCE")
with open("demo.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Q9. Write text to a report file.
with open("report.txt", "w", encoding="utf-8") as file:
    file.write("Python Lab\n")
    file.write("Practical 11")
print("File saved")

# Q10. Read an audit log and display failed attempts only.
with open("audit_log.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "FAILED" in line:
            print(line.strip())
