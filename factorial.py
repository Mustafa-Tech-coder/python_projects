def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print("!"*30)
n= int(input("Enter a number: \n"))
print(f"The factorial of {n} is {factorial(n)}.")
print("enter a valid non-negative integer.")
print("!"*30)
print(factorial(n))
