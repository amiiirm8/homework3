#The apply_discount function is designed to apply a discount to a given price and calculate
#the final price after the discount has been applied. The function takes two arguments:
#price, which is the original price of the item, and discount, which is the percentage
#discount to apply (defaulting to 0 if not provided). The function returns the final
#price of the item after applying the discount.
#In the function body, the price and discount arguments are used to calculate the final
#price by multiplying the price by 1 minus the discount percentage and then converting 
#the result to an integer using the int() function. The resulting final price is then
# compared against the original price using an assert statement.
#The assert statement checks that the final price is greater than 0 and less than or
#equal to the original price. If the assertion fails (i.e., if the final price is 
#outside this range).
#While assert statements can be useful for checking assumptions during development and
#testing, they should not be relied upon as the primary means of data validation.
#In production environments, it's important to use more robust validation techniques 
#such as input validation functions or data sanitization libraries to ensure that 
#the data is safe and valid
#Now Why Doesn't work this Assert statements: Because 
#There could be a few reasons why the assert statement in the apply_discount function 
#may not be working as expected.
#One possibility is that the final price calculated by the function is always within 
#the expected range for the input arguments, so the assert statement is never triggered. 
#In this case, the assert statement would not raise an AssertionError because the condition
#it's checking is always true.
#The assert statement in the apply_discount function is designed to raise an AssertionError 
#if the final price calculated after applying the discount is not within a valid range. 
#Specifically, the assert statement checks that the final price is greater than 0 and 
#less than or equal to the original price.
#If you're not seeing an AssertionError being raised when you call the apply_discount function,
#it's possible that the final price is always within the valid range for the arguments 
#passed to the function. In other words, the assertion condition is always true, so 
#the assert statement never raises an AssertionError

# def apply_discount(price: int, discount: float = 0.0) -> int:
#     """
#     Apply Discount Percent and Calculate Final Price
#     """
#     final_price = int(price * (1 - discount))
#     if not (0 < final_price <= price):
#         raise ValueError("Invalid discount or price")
#     return final_price

def apply_discount(price: int, discount: float = 0.0) -> int:
    """
    Apply Discount Percent and Calculate Final Price
    """
    try:
        final_price = int(price * (1 - discount))
    except (TypeError, ValueError):
        raise ValueError("Invalid price or discount value")
    
    if final_price <= 0:
        raise ValueError("Discount is too high")
    return final_price

# Example usage with invalid input
original_price = "50"
discount_pct = 0.8
try:
    final_price = apply_discount(original_price, discount_pct)
    print(f"The final price is ${final_price:.2f}")
except ValueError as e:
    print(f"Error: {e}")

# Example usage with valid input
original_price = 100
discount_pct = 0.2
try:
    final_price = apply_discount(original_price, discount_pct)
    print(f"The final price is ${final_price:.2f}")
except ValueError as e:
    print(f"Error: {e}")