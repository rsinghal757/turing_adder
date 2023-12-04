from .nand_gate import nand_gate
from .not_gate import not_gate

# OR Gate using NAND
def or_gate(input_bits):
    return nand_gate([not_gate(input_bits[0]), not_gate(input_bits[1])])