# Number Statistics
# Task 5 - Level 1 - Day 5

# Store numerical data in a list
numbers = [
    12, 7, 25, 4, 18,
    31, 9, 42, 16, 5,
    28, 11, 36, 3, 20
]

# Create separate lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Process each number
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Find largest and smallest numbers
largest_number = max(numbers)
smallest_number = min(numbers)

# Display results
print("===== NUMBER STATISTICS =====")

print("Numbers:", numbers)

print("\nEven Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

print("\nLargest Number:", largest_number)
print("Smallest Number:", smallest_number)