# NAND Gate implemented as Turing Machine
def nand_gate(input_bits):
    tape = input_bits.copy()
    S0, S1, H = "S0", "S1", "H"
    head_position = 0
    current_state = S0
    
    while current_state != H:
        symbol = tape[head_position]
        if current_state == S0:
            if symbol == 0:
                tape[head_position] = 1
                head_position += 0
                current_state = H
            else:  # symbol == 1
                tape[head_position] = 1
                head_position += 1
                current_state = S1
        elif current_state == S1:
            if symbol == 0:
                tape[head_position] = 1
                head_position += 0
                current_state = H
            else:  # symbol == 1
                tape[head_position] = 0
                head_position += 0
                current_state = H
    return tape[head_position]

# NOT Gate using NAND
def not_gate(input_bit):
    return nand_gate([input_bit, input_bit])

# AND Gate using NAND
def and_gate(input_bits):
    return not_gate(nand_gate(input_bits))

# OR Gate using NAND
def or_gate(input_bits):
    return nand_gate([not_gate(input_bits[0]), not_gate(input_bits[1])])

# XOR Gate using NAND
def xor_gate(input_bits):
    temp1 = nand_gate([input_bits[0], input_bits[1]])
    temp2 = nand_gate([input_bits[0], temp1])
    temp3 = nand_gate([input_bits[1], temp1])
    return nand_gate([temp2, temp3])

# Half Adder
def half_adder(input_bits):
    sum_bit = xor_gate(input_bits)
    carry_bit = and_gate(input_bits)
    return [sum_bit, carry_bit]

# Full Adder
def full_adder(input_bits):
    half_adder1 = half_adder([input_bits[0], input_bits[1]])
    half_adder2 = half_adder([half_adder1[0], input_bits[2]])
    carry_out = or_gate([half_adder1[1], half_adder2[1]])
    sum_bit = half_adder2[0]
    return [sum_bit, carry_out]

# Testing each gate and adder
print("Testing NAND Gate")
tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
for test in tests:
    out = nand_gate(test)
    print(f"Inputs: {test}, NAND Output: {out}")

print("\nTesting NOT Gate")
for test_bit in [0, 1]:
    out = not_gate(test_bit)
    print(f"Input: {test_bit}, NOT Output: {out}")

print("\nTesting AND Gate")
for test_bits in tests:
    out = and_gate(test_bits)
    print(f"Inputs: {test_bits}, AND Output: {out}")

print("\nTesting OR Gate")
for test_bits in tests:
    out = or_gate(test_bits)
    print(f"Inputs: {test_bits}, OR Output: {out}")

print("\nTesting XOR Gate")
for test_bits in tests:
    out = xor_gate(test_bits)
    print(f"Inputs: {test_bits}, XOR Output: {out}")

print("\nTesting Half Adder")
for test_bits in tests:
    sum_bit, carry_bit = half_adder(test_bits)
    print(f"Inputs: {test_bits}, Sum: {sum_bit}, Carry: {carry_bit}")

print("\nTesting Full Adder")
extended_tests = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
for test_bits in extended_tests:
    sum_bit, carry_out = full_adder(test_bits)
    print(f"Inputs: {test_bits}, Sum: {sum_bit}, Carry Out: {carry_out}")

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

def decimal_to_binary(num):
    return bin(num)[2:].zfill(8)

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def add_interface(num1, num2):

    binary_num1 = decimal_to_binary(num1)
    binary_num2 = decimal_to_binary(num2)

    print(f"Number 1 in Decimal: {num1}, Binary: {binary_num1}")
    print(f"Number 2 in Decimal: {num2}, Binary: {binary_num2}")
    print("-------------------------------------")

    # Convert binary strings to lists of integers
    binary_num1_list = list(map(int, binary_num1))
    binary_num2_list = list(map(int, binary_num2))

    result = eight_bit_adder(binary_num1_list, binary_num2_list)
    binary_result = ''.join(map(str, result))
    decimal_result = binary_to_decimal(binary_result)

    print(f"Sum :: Decimal: {decimal_result}, Binary: {binary_result}")

def user_interface():
    try:
        num1 = int(input("Enter the first number (0-255): "))
        num2 = int(input("Enter the second number (0-255): "))
        print("-------------------------------------")

        if 0 <= num1 <= 255 and 0 <= num2 <= 255:
            add_interface(num1, num2)
        else:
            print("Error: Please enter numbers in the range 0-255.")

    except ValueError:
        print("-------------------------------------")
        print("Invalid input! Please enter a valid integer.")

def main():
    user_interface()

if __name__ == "__main__":
    main()