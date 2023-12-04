from .nand_gate import nand_gate

# XOR Gate using NAND
def xor_gate(input_bits):
    temp1 = nand_gate([input_bits[0], input_bits[1]])
    temp2 = nand_gate([input_bits[0], temp1])
    temp3 = nand_gate([input_bits[1], temp1])
    return nand_gate([temp2, temp3])