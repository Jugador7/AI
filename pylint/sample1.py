"""
This module provides a simple addition function.
"""

def add(number1, number2):
    """
    Add two numbers and return the result.

    Parameters:
    number1 (int or float): The first number to add.
    number2 (int or float): The second number to add.

    Returns:
    int or float: The sum of the two numbers.
    """
    return number1 + number2

NUM_1 = 4
NUM_2 = 5
TOTAL = add(NUM_1, NUM_2)

print(f"The sum of {NUM_1} and {NUM_2} is {TOTAL}")
