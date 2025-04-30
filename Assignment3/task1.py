##Factorial

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = input("Enter a number to calculate its factorial: ")
result = factorial(5)
print(f"The factorial of 5 is: {result}")