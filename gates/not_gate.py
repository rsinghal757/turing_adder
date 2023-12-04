from .nand_gate import nand_gate

# NOT Gate using NAND
def not_gate(input_bit):
    return nand_gate([input_bit, input_bit])