import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """
                int a[99];
                void main() {
                    int b[99];
                    b[0] = 1;
                    putInt(b[0]);
                }



"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,500))
