# Practical 10: Introduction to Programming


# Q1. String indexing
text = input("Enter a string: ")
print("First:", text[0] if text else "")
print("Last:", text[-1] if text else "")
print("Middle:", text[len(text)//2] if text else "")


# Q2. String slicing
text = input("Enter a string: ")
print("First five:", text[:5])
print("From index 2:", text[2:])
print("Every second character:", text[::2])


# Q3. Step slicing and reverse
text = input("Enter a string: ")
print("Alternate characters:", text[::2])
print("Reverse:", text[::-1])


# Q4. String immutability
text = "Python"
try:
    text[0] = "J"
except TypeError:
    print("Strings are immutable.")
text = "J" + text[1:]
print(text)


# Q5. in and not in
text = input("Enter text: ")
word = input("Word to search: ")
print(word in text)
print(word not in text)


# Q6. find and index
text = input("Enter text: ")
word = input("Word to find: ")
print("find:", text.find(word))
try: print("index:", text.index(word))
except ValueError: print("Word not found; index() raises ValueError.")


# Q7. Count occurrences
text = input("Enter text: ")
char = input("Character/substring to count: ")
print("Occurrences:", text.count(char))


# Q8. Case conversion
text = input("Enter text: ")
print(text.upper())
print(text.lower())
print(text.title())


# Q9. Remove spaces and format
text = input("Enter text: ")
print("Trimmed:", text.strip())
print("No spaces:", text.replace(" ", ""))
print("Formatted:", " ".join(text.split()))


# Q10. Split and join
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Words:", words)
print("Joined with hyphens:", "-".join(words))


# Q11. Palindrome checker
text = input("Enter text: ").lower().replace(" ", "")
print("Palindrome" if text == text[::-1] else "Not palindrome")


# Q12. Text analyzer
from collections import Counter
words = input("Enter a sentence: ").lower().split()
print("Word count:", len(words))
print("Character count (including spaces):", len(" ".join(words)))
print("Most frequent word:", Counter(words).most_common(1)[0][0] if words else "No words")


# ==================== PRACTICE QUESTIONS ====================

# Q1. Clean chatbot text and join words with underscores.
text = " Python makes NLP powerful "
clean_text = " ".join(text.split()).lower()
print("_".join(clean_text.split()))

# Q2. Mask the middle of a student ID.
student_id = "STU2026CS1098"
print(student_id[:4] + "****" + student_id[-4:])

# Q3. Extract values from a drone log.
log = "ALT:250|SPD:45|BAT:78"
for item in log.split("|"):
    key, value = item.split(":")
    print(key, value)

# Q4. Check password character types and minimum length.
password = "PySecure2026!"
print("Uppercase:", any(ch.isupper() for ch in password))
print("Lowercase:", any(ch.islower() for ch in password))
print("Digit:", any(ch.isdigit() for ch in password))
print("Special character:", any(not ch.isalnum() for ch in password))
print("Minimum length:", len(password) >= 8)

# Q5. Count symptoms and find the most repeated one.
from collections import Counter
symptoms = "fever cough fever fatigue fever cold".split()
counts = Counter(symptoms)
print("Fever count:", counts["fever"])
print("Unique symptoms:", set(symptoms))
print("Most repeated:", counts.most_common(1)[0][0])

# Q6. Display the output of string slicing.
text = "PythonProgramming"
print(text[2:10:2])

# Q7. Strip, uppercase, and replace spaces.
s = " Data Science "
print(s.strip().upper().replace(" ", "_"))

# Q8. Reverse split parts and join with hyphens.
msg = "AI|ML|DL|NLP"
parts = msg.split("|")
print("-".join(parts[::-1]))

# Q9. Extract the word Programming.
text = "PythonProgramming"
print(text[6:])

# Q10. Replace spaces with hyphens.
sentence = "Python makes coding easy"
print(sentence.replace(" ", "-"))
