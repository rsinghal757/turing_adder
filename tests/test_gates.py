import unittest
from gates.and_gate import and_gate
from gates.nand_gate import nand_gate
from gates.not_gate import not_gate
from gates.or_gate import or_gate
from gates.xor_gate import xor_gate

class TestLogicGates(unittest.TestCase):
    def test_nand_gate(self):
        self.assertEqual(nand_gate([0, 0]), 1)
        self.assertEqual(nand_gate([0, 1]), 1)
        self.assertEqual(nand_gate([1, 0]), 1)
        self.assertEqual(nand_gate([1, 1]), 0)

    def test_not_gate(self):
        self.assertEqual(not_gate(0), 1)
        self.assertEqual(not_gate(1), 0)

    def test_and_gate(self):
        self.assertEqual(and_gate([0, 0]), 0)
        self.assertEqual(and_gate([0, 1]), 0)
        self.assertEqual(and_gate([1, 0]), 0)
        self.assertEqual(and_gate([1, 1]), 1)

    def test_or_gate(self):
        self.assertEqual(or_gate([0, 0]), 0)
        self.assertEqual(or_gate([0, 1]), 1)
        self.assertEqual(or_gate([1, 0]), 1)
        self.assertEqual(or_gate([1, 1]), 1)

    def test_xor_gate(self):
        self.assertEqual(xor_gate([0, 0]), 0)
        self.assertEqual(xor_gate([0, 1]), 1)
        self.assertEqual(xor_gate([1, 0]), 1)
        self.assertEqual(xor_gate([1, 1]), 0)

if __name__ == '__main__':
    unittest.main()