from .full_adder import full_adder

def eight_bit_adder(a, b):
    carry = 0
    result = []
    for i in range(7, -1, -1):  # Start from the least significant bit
        sum_bit, carry = full_adder([a[i], b[i], carry])
        result.insert(0, sum_bit)  # Insert sum_bit at the beginning of the result
    # Check for final carry
    if carry:
        result.insert(0, carry)  # Insert final carry at the beginning if it exists
    return result