def addition(a,b):
    return a + b

def substraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b == 0:
        raise ValueError("Division by ZERO is not allowed")
    return a / b