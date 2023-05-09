import math

def safe_divide(a: float, b: float) -> float:
    """
    Safely divides two numbers and handles potential errors.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        Optional[float]: The result of the division, or None if an error occurs.

    Raises:
        ZeroDivisionError: If b is zero.
        TypeError: If a or b is not a number.
        OverflowError: If the division result is infinite (e.g., if a is not finite or b is zero).
        Exception: If any other exception occurs.
    """
    try:
        result = a / b
        if math.isinf(result):
            raise OverflowError("Result is infinite")
    except ZeroDivisionError:
        print("Error: division by zero")
        return None
    except TypeError:
        print("Error: invalid operand type")
        return None
    except OverflowError as e:
        print("Error:", e)
        return None
    except Exception as e:
        print("Error:", e)
        return None
    else:
        return result
    

# Example usage of safe_divide function
numerator = 10
denominator = 2
result = safe_divide(numerator, denominator)
if result is not None:
    print(f"{numerator} divided by {denominator} is {result}")