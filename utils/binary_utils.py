def decimal_to_binary(num):
    return bin(num)[2:].zfill(8)

def binary_to_decimal(binary_str):
    return int(binary_str, 2)