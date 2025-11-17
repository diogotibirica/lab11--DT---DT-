# https://github.com/diogotibirica/lab11--DT---DT-.git
# Partner 1: Diogo Tibirica
# Partner 2: Diogo Tibirica
import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be greater than 0 and not 1")
    if b <= 0:
        raise ValueError("Logarithm argument must be greater than 0")
    return math.log(b, a)

def exp(a, b):
    return a ** b