import math

def quadratic_root(first_number: int) -> str:
    if first_number < 0:
        return "Number cannot be negative"
    return f"Result for quadratic root: {math.sqrt(first_number)}"
