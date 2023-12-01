import re

# Function to find the first and last number in a string
def find_first_and_last_number(s):
    # Find all numbers in the string
    numbers = re.findall(r'\d', s)
    if len(numbers) >= 1:
        return int(str(numbers[0] + numbers[-1]))
    else:
        return 0  # No numbers found

# Open the file and read the lines
with open("input1.txt", "r") as file:
    rows = file.readlines()

total_sum = 0

# Iterate over each row to find the numbers and calculate the sum
for row in rows:
    combined_number = find_first_and_last_number(row.strip())
    total_sum += combined_number
    print(f"Row: {row.strip()}, Combined number: {combined_number}")

print("\nTotal sum:", total_sum)