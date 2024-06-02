def sum(a,b):
    return a + b

def multiple(a,b):
    return a * b

def remainder(a,b):
    return a % b

try:
    from calculator import remainder as re
except ImportError:
    print("Custom 'calculator' module not found . Using built-in function.")
    def re(a,b):
        return a % b

a = int(input("Enter a:"))
b = int(input("Enter b:"))

print("Result = ",re(a,b))