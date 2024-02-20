

def multiply(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Invalid arguments. Both arguments must be numbers.")
    return x * y
