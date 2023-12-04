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