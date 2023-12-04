# Turing Adder

An 8-bit adder implemented using logic gates, which are then implemented as a Turing machine.

- NAND Gate is implemented as a Turing Machine which takes the bits as the starting position of the tape, and computes the output bit. See gates/nand_gate.py for the implementation.
- All other gates are built using this NAND gate implementation.
- Adders use these gates to do 1-bit additions, and 8-bit additions subsequently.

Nothing serious - just a fun little project.