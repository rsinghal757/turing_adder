import unittest
from adders.eight_bit_adder import eight_bit_adder
from adders.full_adder import full_adder
from adders.half_adder import half_adder
from utils.binary_utils import decimal_to_binary

class TestAdders(unittest.TestCase):

    def test_half_adder(self):
        self.assertEqual(half_adder([0, 0]), [0, 0])
        self.assertEqual(half_adder([0, 1]), [1, 0])
        self.assertEqual(half_adder([1, 0]), [1, 0])
        self.assertEqual(half_adder([1, 1]), [0, 1])

    def test_full_adder(self):
        # Testing with carry-in as 0
        self.assertEqual(full_adder([0, 0, 0]), [0, 0])
        self.assertEqual(full_adder([0, 1, 0]), [1, 0])
        self.assertEqual(full_adder([1, 0, 0]), [1, 0])
        self.assertEqual(full_adder([1, 1, 0]), [0, 1])

        # Testing with carry-in as 1
        self.assertEqual(full_adder([0, 0, 1]), [1, 0])
        self.assertEqual(full_adder([0, 1, 1]), [0, 1])
        self.assertEqual(full_adder([1, 0, 1]), [0, 1])
        self.assertEqual(full_adder([1, 1, 1]), [1, 1])

    def test_eight_bit_adder(self):
        # Test cases for 8-bit adder
        test_cases = [
            (0, 0, "00000000"),
            (154, 20, "10101110"),
            (127, 5, "10000100"),
            (255, 255, "111111110"),  # Note the 9-bit result due to overflow
        ]

        for num1, num2, expected in test_cases:
            binary_num1 = list(map(int, decimal_to_binary(num1)))
            binary_num2 = list(map(int, decimal_to_binary(num2)))
            result = eight_bit_adder(binary_num1, binary_num2)
            binary_result = ''.join(map(str, result))
            self.assertEqual(binary_result, expected)

if __name__ == '__main__':
    unittest.main()
