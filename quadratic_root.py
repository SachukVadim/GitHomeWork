import math

def quadratic_root(first_number:int) -> float:
    if first_number < 0:
        return "Number cannot be zero"
    return f"Result for quadratic root {math.sqrt(first_number)}"