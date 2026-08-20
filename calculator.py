print("Welcome to the calculator program!")
print("*"*40)
def calc(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b==0:
            return"Division by zero is not allowed."
        else:
            return a / b
    else:
        return " Invalid operator"
try:
    a = float(input("Enter first number:\n "))
    op = input("Enter operator (+, -, *, /):\n ")
    b = float(input("Enter second number: \n"))
    result = calc(a, b, op)
    print(f"The result is: {result}")   
except ValueError:
    print("Invalid input. Please enter numeric values for the numbers.")
print("*"*40)