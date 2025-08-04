#Simple Calculator Functions
# Requirements:
# Create these functions:
    # add(a, b) - returns the sum of two numbers
    # subtract(a, b) - returns the difference of two numbers
    # multiply(a, b) - returns the product of two numbers
    # divide(a, b) - returns the quotient, handles division by zero
# Create a main function that:
    # Gets two numbers from the user
    # Asks which operation to perform
    # Calls the appropriate function
    # Displays the result
def addition(a, b):
    result = (a + b)
    print(f"{a} + {b} = {result}")
    return result

def subtraction(a, b):
    result = (a - b)
    print(f"{a} - {b} = {result}")
    return result

def multiplication(a, b):
    result = (a * b)
    print(f"{a} x {b} = {result}")
    return result

def division(a, b):
    try:
        result = (a / b)
        print(f"{a} ÷ {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Choose operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1-4): "))
print("\n")

if choice == 1:
    addition(num1, num2)
elif choice == 2:
    subtraction(num1, num2)
elif choice == 3:
    multiplication(num1,num2)
elif choice == 4:
    division(num1, num2)