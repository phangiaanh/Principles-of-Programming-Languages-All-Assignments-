import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """
                int i;
                void main(){
                    for(i = 0; i < 10; i = i + 1) a[i] = "a";
                    for(i = 0; i < 10; i = i + 1) b[i] = "b";

                    {
                        //string b[10];
                        for(i = 0; i < 10; i = i + 1) b[i] = "c";
                    }

                    
                    for(i = 0; i < 10; i = i + 1) putStringLn(a[i]);
                    for(i = 0; i < 10; i = i + 1) putString(b[i]);
                }
                string a[10], b[10];
                """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,500))
