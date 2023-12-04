An 8-bit adder implemented using logic gates, each of which is in turn implemented as a Turing machine.

## Features

- **NAND Gate**: Implemented as a Turing Machine that takes bits as the tape's starting position to compute the output bit. See `gates/nand_gate.py` for the implementation.
- **Logic Gates**: Constructs AND, OR, XOR, and NOT gates using the NAND gate implementation.
- **Adders**: Performs 1-bit and 8-bit additions using these gates.

This project is a light-hearted exploration into the world of computation and digital logic.

## Prerequisites

- Python 3.x

## Installation

To install the Turing Adder, clone the repository and navigate to the project directory:

```sh
git clone https://github.com/yourusername/turing_adder.git
cd turing_adder
```

## Usage

To run the program from the command line:

```sh
python main.py
```

This will initiate an interactive prompt where you can input two 8-bit binary numbers and see the result of their addition.

For integration into Python scripts:

```python
from turing_adder.gates import and_gate

# Example usage of an AND gate
result = and_gate([1, 0])
print(result)  # Output: 0
```

## Running Tests

Ensure the correctness of the gates and adders by running the tests:

```sh
python -m unittest discover -s tests
```

This will run all the tests in the `tests` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.