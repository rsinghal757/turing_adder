from .half_adder import half_adder
from gates.or_gate import or_gate

# Full Adder
def full_adder(input_bits):
    half_adder1 = half_adder([input_bits[0], input_bits[1]])
    half_adder2 = half_adder([half_adder1[0], input_bits[2]])
    carry_out = or_gate([half_adder1[1], half_adder2[1]])
    sum_bit = half_adder2[0]
    return [sum_bit, carry_out]