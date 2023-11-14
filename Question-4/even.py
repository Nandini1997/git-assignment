def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
input_number = int(input("Enter a number: "))
result = check_even_odd(input_number)
print(f"The entered number is {result}.")