"""
calculator.py
A modular calculator program demonstrating functions, parameters,
return values, default arguments, and error handling.
"""

def add(a, b=0):
    """
    Returns the sum of two numbers.
    Default value of b is 0.
    """
    return a + b


def subtract(a, b=0):
    """
    Returns the difference between two numbers.
    Default value of b is 0.
    """
    return a - b


def multiply(a, b=1):
    """
    Returns the product of two numbers.
    Default value of b is 1.
    """
    return a * b


def divide(a, b):
    """
    Returns the division result of two numbers.
    Handles division by zero.
    """
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


def get_numbers():
    """
    Takes two numbers from the user and returns them.
    """
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


def calculator_menu():
    """
    Displays calculator menu options.
    """
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def main():
    """
    Main function to run the calculator.
    """
    while True:
        calculator_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            a, b = get_numbers()

            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            elif choice == "4":
                result = divide(a, b)

            print("Result:", result)
        else:
            print("Invalid choice! Please select a valid option.")


# Program execution starts here
if __name__ == "__main__":
    main()
