from gates.and_gate import and_gate
from gates.xor_gate import xor_gate

# Half Adder
def half_adder(input_bits):
    sum_bit = xor_gate(input_bits)
    carry_bit = and_gate(input_bits)
    return [sum_bit, carry_bit]