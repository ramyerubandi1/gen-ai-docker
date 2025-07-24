def add(x, y):
    return x 

def subtract(x,
    return x - y

def multiply(x, y):jnvkjsnvsvbk
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    print("=== Simple Calculator ====")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid inpssut")
        return

    ops = {'1': add, '2': subtract, '3': multiply

