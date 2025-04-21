import logging

logging.basicConfig(filename="error.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def divide(a, b):
    if b == 0:
        logging.error("Division by zero error")
        raise ValueError("Cannot divide by zero")
    return a / b

def square_root(x):
    if x < 0:
        logging.error("Square root of negative number error")
        raise ValueError("Cannot calculate square root of a negative number")
    return x ** 0.5
