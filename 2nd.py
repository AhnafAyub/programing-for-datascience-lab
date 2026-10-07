
print ("1st code")
marks = [75, 82, 60, 45, 90]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

passed = 0

for mark in marks:
    if mark >= 50:
        passed += 1

print("Total marks:", total)
print("Average mark:", average)
print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Courses passed:", passed)

print ("2nd code")
temperatures = (30, 32, 28, 31, 33, 29)

print("Temperatures:")

for temperature in temperatures:
    print(temperature)

print("Highest temperature:", max(temperatures))
print("Lowest temperature:", min(temperatures))

print (" 3rd code")

text = input("Enter a word or short sentence: ")

characters = len(text)
vowels = 0
spaces = 0

for char in text:
    if char.lower() in "aeiou":
        vowels += 1

    if char == " ":
        spaces += 1

print("Number of characters:", characters)
print("Number of vowels:", vowels)
print("Number of spaces:", spaces)


print ("4th code")
def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


marks = [85, 75, 90, 80, 70]

grade = calculate_grade(marks)

print("Grade:", grade)


print ("5th code")
cart = [
    {"name": "Laptop", "price": 80000, "quantity": 1},
    {"name": "Mouse", "price": 1500, "quantity": 2},
    {"name": "Keyboard", "price": 3000, "quantity": 1},
    {"name": "Headphones", "price": 2500, "quantity": 1}
]

total = 0

for product in cart:
    cost = product["price"] * product["quantity"]
    total += cost

print("Total cost:", total)


def apply_discount(total):
    if total >= 2000:
        return total * 0.90
    else:
        return total


final_price = apply_discount(total)

print("Final price:", final_price)

print ("6th code")
number = int(input("Enter a number: "))

while number >= 0:
    print(number)
    number -= 1

print ("7th code")
students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78}
]

for student in students:
    print("Name:", student["name"])
    print("Department:", student["department"])
    print("Marks:", student["marks"])
    print("Attendance:", student["attendance"])
    print()

products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]


for product in products:
    print("Name:", product["name"])
    print("Price:", product["price"])
    print("Quantity:", product["quantity"])
    print()



