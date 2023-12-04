from .nand_gate import nand_gate
from .not_gate import not_gate

# AND Gate using NAND
def and_gate(input_bits):
    return not_gate(nand_gate(input_bits))