def multiply(num1, num2):
    """Takes two positive integers as parameters and returns the product of those two numbers
    (the result from multiplying them together)."""
    if num2 == 1:
        return num1
    return num1 + multiply(num1, num2 - 1)
