def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
input_numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
result = calculate_sum(input_numbers)
print(f"The sum of the entered numbers is: {result}")
