import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
	def test_CallExpr_1(self):
		input = """
				boolean compare(float a, int b)
				{
					if(a > b) return true;
					else return false;
				}

				void main()
				{
					if (compare(5.2, 3)) putInt(2);
					else putFloat(3);
				}
				"""
		expect = "2"
		self.assertTrue(TestCodeGen.test(input,expect,501))

	def test_CallExpr_2(self):
		input = """
				int getTwoInt(int a)
				{
					putInt(2 + 3 * 5 / 2 - 3);
					putInt(2 * a + 3);
					return a + 1;
				}

				void main()
				{
					putInt(getTwoInt(2));
				}
				"""
		expect = "673"
		self.assertTrue(TestCodeGen.test(input,expect,502))

	def test_CallExpr_3(self):
		input = """
				float getThreeFloat(int _)
				{
					if(_ <= 1){
						if(_ >= 0) putFloat(1.5);
						else putFloat(-1);
					}
					else{
						if(_ <= 10) putFloat(5.5);
						else putFloat(2.0/3);
					}
					return _;
				}

				void main()
				{
					putFloat(getThreeFloat(6));
				}
				"""
		expect = "5.56.0"
		self.assertTrue(TestCodeGen.test(input,expect,503))

	def test_CallExpr_4(self):
		input = """
				string helloWorld(string str)
				{
					return "Hello World \\n";
				}

				void main()
				{
					putStringLn(helloWorld("AAAAAAAAAAA"));
				}
				"""
		expect = "Hello World \n\n"
		self.assertTrue(TestCodeGen.test(input,expect,504))

	def test_CallExpr_5(self):

		input = """
				boolean checkBool(boolean bool)
				{
					int i;
					for(i = 0; i < 10; i = i + 1){
						putBoolLn(bool);
						bool = !bool;
					}
					return bool;
				}

				void main()
				{
					putBool(checkBool(true));
				}
				"""
		expect = "true\nfalse\ntrue\nfalse\ntrue\nfalse\ntrue\nfalse\ntrue\nfalse\ntrue"
		self.assertTrue(TestCodeGen.test(input,expect,505))

	def test_CallExpr_6(self):
		input = """	
				float globalFloat;

				void main()
				{
					putIntLn(2);
					testFloat();
					globalFloat = globalFloat + 2;
					testFloat();
				}

				void testFloat()
				{
					putFloatLn(globalFloat);
				}
				"""
		expect = "2\n0.0\n2.0\n"
		self.assertTrue(TestCodeGen.test(input,expect,506))

	def test_CallExpr_7(self):
		input = """
				void putLoop(int n)
				{
					int i;
					for(i = 0; i <= n; i = i + 1) putIntLn(i);
				}

				void main()
				{
					putLoop(10);
					putString("Your PPL score will be: ");
					putFloatLn(4.74);
				}
				"""
		expect = "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\nYour PPL score will be: 4.74\n"
		self.assertTrue(TestCodeGen.test(input,expect,507))

	def test_CallExpr_8(self):
		input = """
				int sqrt(int n){
					int i;
					for(i = 1; i < n; i = i + 1){
						if(i * i > n) return i;
					}
					return i;
				}

				boolean checkPrime(int n)
				{
					int i;
					if (n == 1) return false;
					for(i = 2; i <= sqrt(n); i = i + 1)
						if (n % i == 0) return false;
					return true;
				}

				void main()
				{
					putBoolLn(checkPrime(1));
					putBoolLn(checkPrime(21));
					putBoolLn(checkPrime(37));
					putBoolLn(checkPrime(47));
					putBoolLn(checkPrime(152));
				}
				"""
		expect = "false\nfalse\ntrue\ntrue\nfalse\n"
		self.assertTrue(TestCodeGen.test(input,expect,508))

	def test_CallExpr_9(self):
		input = """
				int sum(int a[], int l)
				{
					int temp,i;
					temp = 0;
					for(i = 0; i < l; i = i + 1) temp = temp + a[i];
					return temp;
				}

				int a[10];

				void main()
				{
					putStringLn("Test sum and mul:");

					int i;

					for(i = 0; i < 10; i = i + 1) a[i]=i;
					for(i = 0; i < 10; i = i + 1) f[i]=i+1;

					putIntLn(sum(a,10));
					putFloatLn(multiply(f,10));
				}

				float f[10];

				float multiply(float a[],int l)
				{
					float temp;
					int i;
					temp = 1;
					for(i = 0; i < l; i = i + 1) temp = temp * a[i];
					return temp;
				}
				"""
		expect = "Test sum and mul:\n45\n3628800.0\n"
		self.assertTrue(TestCodeGen.test(input,expect,509))

	def test_CallExpr_10(self):
		input = """
				void main()
				{
					putIntLn(1);
					putFloatLn(1 + 1.1 + 1.11 + 1.111);
					putBoolLn(true || false && true && false);
					putStringLn("Your results are OK");
				}
				"""
		expect = "1\n4.321\ntrue\nYour results are OK\n"
		self.assertTrue(TestCodeGen.test(input,expect,510))

	def test_Literal_1(self):
		input = """
				int test;

				void printMultipleInt()
				{
					test = test + (1 * 2 * 3 % 3 * 4 * 5) / 10000;
					putFloatLn(test);
				}

				void main()
				{
					if(false){
						test = 3 + 0;
					}else{
						test = 1;
					}
					putFloatLn(test);
					printMultipleInt();
				}
				"""
		expect = "1.0\n1.0\n"
		self.assertTrue(TestCodeGen.test(input,expect,511))

	def test_Literal_2(self):
		input = """
				void main()
				{
					b = !(true && true || false || false);
					putBool(b);
				}

				boolean b;
				"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input,expect,512))

	def test_Literal_3(self):
		input = """
				string str;

				void main()
				{
					str = getHelloString();
					putStringLn(str);
				}

				string getHelloString()
				{
					string helloS[10];
					helloS[0] = "The real Hello";
					return helloS[0];
				}
				"""
		expect = "The real Hello\n"
		self.assertTrue(TestCodeGen.test(input,expect,513))

	def test_Literal_4(self):
		input = """
				void main()
				{
					putFloatLn(getFloatLiteral());
				}

				float getFloatLiteral()
				{
					float f;
					f = 3.3;
					f = -f * 3 - 2;
					return f;
				}
				"""
		expect = "-11.9\n"
		self.assertTrue(TestCodeGen.test(input,expect,514))

	def test_Literal_5(self):
		input = """
				int a[100], i;

				void main()
				{
					for( i = 0; i < 10; i = i + 2) a[i] = (i * i) % 50 ;

					for(i = 0; i < 10; i = i + 1) putIntLn(a[i]);
				}
				"""
		expect = "0\n0\n4\n0\n16\n0\n36\n0\n14\n0\n"
		self.assertTrue(TestCodeGen.test(input,expect,515))

	def test_VarDecl_1(self):
		input = """
				int a0, a1[1], a2, a3[3], a4, a5[5];

				float f0[1], f1, f2[1], f3, f4[3];
				boolean b0,b1[1],b2,b3[3],b4;


				void declareVar()
				{
					int a0, a2, a4;
					int a1[1], a3[3], a5[5];
					putBool(b0);
				}

				void main()
				{
					declareVar();
				}
				"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input,expect,516))

	def test_VarDecl_2(self):
		input = """
				void main()
				{
					float a;
					a = 1.0;
					{
						int a;
						a = 5;
						putFloatLn(a);
						{
							a = 6;
							putFloatLn(a);
						}
					}
					putFloat(a);
				}
				"""
		expect = "5.0\n6.0\n1.0"
		self.assertTrue(TestCodeGen.test(input,expect,517))

	def test_VarDecl_3(self):
		input = """
				string a[30], b;

				void main()
				{
					int i;
					for(i = 0; i < 5; i = i + 1) a[i] = "1";
					for(i = 0; i < 5; i = i + 1) putString(a[i]);
					b = "Everything is okay";
					putStringLn(b);
				}
				"""
		expect = "11111Everything is okay\n"
		self.assertTrue(TestCodeGen.test(input,expect,518))

	def test_VarDecl_4(self):
		input = """
				int a[69];
				void main()
				{
					int a;
					{
						a = 3;
					}
					int b;
					float c;
					boolean d;
					string e;

					putInt(a);
					for(b = 0; b < 30; b = b + 1) putIntLn(b);
				}
				"""
		expect = "30\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n"
		self.assertTrue(TestCodeGen.test(input,expect,519))

	def test_VarDecl_5(self):
		input = """
				int a0[0];
				boolean b0[0];
				string c0[0];
				float d0[0];

				void main()
				{
					//Doing nothing
					putLn();
				}
				"""
		expect = "\n"
		self.assertTrue(TestCodeGen.test(input,expect,520))

	def test_BinaryOp_1(self):
		input = """
				float a;

				void main()
				{
					a = 1.11 + 2 + 3 + 1.0 + 1.1 + 1.2 + 1.3;
					putFloatLn(a / 10);
				}
				"""
		expect = "1.071\n"
		self.assertTrue(TestCodeGen.test(input,expect,521))

	def test_BinaryOp_2(self):
		input = """
				int a;
				boolean b;

				void main()
				{
					a = 2;
					b = (a >= 1) || (a < 2);
					putBoolLn(b);
				}
				"""
		expect = "true\n"
		self.assertTrue(TestCodeGen.test(input,expect,522))

	def test_BinaryOp_3(self):
		input = """
				void main()
				{	
					int i;
					for(i = 1*2*3; i <= 100; i = i * 2)
					{
						putBool(i * i >= 50);
						putBoolLn((i * i) % 2 == 0);
					}
				}
				"""
		expect = "falsetrue\ntruetrue\ntruetrue\ntruetrue\ntruetrue\n"
		self.assertTrue(TestCodeGen.test(input,expect,523))

	def test_BinaryOp_4(self):
		input = """
				int i;

				boolean cmple(int a, int b)
				{
					return (a <= b);
				}

				boolean cmpge(int a,int b)
				{
					return (a >= b);
				}

				void main()
				{
					i = 5;
					do
					{
						putString("Good job\\n");
						i = i - 1;
					}
					while (i >= 3);


					1/2/3/4/5/6/7/8/9;

					putBoolLn(cmple(6,6));
					putBoolLn(cmpge(6,6));
				}
				"""
		expect = "Good job\nGood job\nGood job\ntrue\ntrue\n"
		self.assertTrue(TestCodeGen.test(input,expect,524))

	def test_BinaryOp_5(self):
		input = """
				int tmp, i;

				void main()
				{
					tmp = 1;
					for(i = 0; i < 2019; i = i + 1) tmp = (tmp * 5) % 13;

					putIntLn(tmp);
				}
				"""
		expect = "8\n"
		self.assertTrue(TestCodeGen.test(input,expect,525))

	def test_UnaryOp_1(self):
		input = """
				int i;
				void main()
				{
					for(i = 10; i >= 5; i = i - 1) putIntLn(-i * 2);
					for(i = 10; i >= 5; i = i - 1) putBoolLn(!(i*2 > 7));
				}
				"""
		expect = "-20\n-18\n-16\n-14\n-12\n-10\nfalse\nfalse\nfalse\nfalse\nfalse\nfalse\n"
		self.assertTrue(TestCodeGen.test(input,expect,526))

	def test_UnaryOp_2(self):
		input = """
				int a[99];

				void main()
				{
					int b[99];
					b[9] = 1;
					b[b[9] + 1 + 2 + 3 + 4 + 5]= --1;
					putInt(b[17-1]);
				}
				"""
		expect = "1"
		self.assertTrue(TestCodeGen.test(input,expect,527))

	def test_UnaryOp_3(self):
		input = """
				float a;
				boolean b;

				void check() {
        		    int a[10];
        		    a[1] = --2;
        		    a[3] = ----1;
        		    a[2] = ------6;
        		    putInt(a[a[a[3 - 1 + 1 * 1 / 1]]]);
        		}

				void main()
				{
					a = ----1--2;
					putFloatLn(a);

					b = !true || !false;
					putBoolLn(b);
					check();
				}
				"""
		expect = "3.0\ntrue\n6"
		self.assertTrue(TestCodeGen.test(input,expect,528))

	def test_UnaryOp_4(self):
		input = """
				int i;

				void main()
				{
					float a;
					a = 10;

					for(i = 0; i < 99; i = i + 1) a = -a;
					putFloatLn(a);
				}
				"""
		expect = "-10.0\n"
		self.assertTrue(TestCodeGen.test(input,expect,529))

	def test_UnaryOp_5(self):
		input = """
				int i, a[10];
				boolean b;

				void setup()
				{
					for(i = 0; i < 10; i = i + 1) a[i] = i;
				}

				void main()
				{
					
					for(i = 0; i < 10; i = i + 1){
						if(a[i] > 5) b = !b;
					}
					putBoolLn(b);
				}
				"""
		expect = "false\n"
		self.assertTrue(TestCodeGen.test(input,expect,530))

	def test_Id_1(self):
		input = """
				string random;
				int one;

				string getRandomString()
				{
					return "R-A-N-D-O-M";
				}

				void main()
				{
					random = getRandomString();

					putStringLn(random);
					putFloatLn(getOne("Kidding"));
				}

				int getOne(string s)
				{
					return -1;			
				}
				"""
		expect = "R-A-N-D-O-M\n-1.0\n"
		self.assertTrue(TestCodeGen.test(input,expect,531))

	def test_Id_2(self):
		input = """
				int i;

				void main()
				{
					string a[10], b[10];

					for(i = 0; i < 10; i = i + 1) a[i] = "a";
					for(i = 0; i < 10; i = i + 1) b[i] = a[i];

					{
						for(i = 0; i < 10; i = i + 1) b[i] = "c";
					}

					for(i = 0; i < 10; i = i + 1) putString(a[i]);
					for(i = 0; i < 10; i = i + 1) putString(b[i]);
				}
				"""
		expect = "aaaaaaaaaacccccccccc"
		self.assertTrue(TestCodeGen.test(input,expect,532))

	def test_Id_3(self):

		input = """

		int i;

		void main()
		{

			for(i = 0; i < 10; i = i + 1) a[i] = "a";
			for(i = 0; i < 10; i = i + 1) b[i] = a[i];
			
			{
				string b[10];
				for(i = 0; i < 10; i = i + 1) b[i] = "c";
			}

			for(i = 0; i < 10; i = i + 1) putString(a[i]);
			for(i = 0; i < 10; i = i + 1) putString(b[i]);
		}

		string a[10],b[10];
		"""
		expect = "aaaaaaaaaaaaaaaaaaaa"
		self.assertTrue(TestCodeGen.test(input,expect,533))

	def test_Id_4(self):
		input = """
				float f;

				void main()
				{
					f = 3;

					setInt(1);

					if (f > i)
					{
						putString("Float is equal to int");
					}
					else
					{
						putString("Float is not equal to int");
					}
					setInt(5);
				}

				int i;

				void setInt(int k)
				{
					i = k;
				}
				"""
		expect = "Float is equal to int"
		self.assertTrue(TestCodeGen.test(input,expect,534))

	def test_Id_5(self):
		input = """
				int i, j, l, a[10], mul;
				
				int[] returnArray()
				{
					int a[11];
					for(j = 0; j < l; j = j + 1) a[j] = j + 1;
		
					return a;
				}
		
				void main()
				{
					l = 10;
		
					mul = 1;
					for(i = 0; i < l;i = i + 1) mul = mul * returnArray()[i];
					putIntLn(mul);
				}
				"""
		expect = "3628800\n"
		self.assertTrue(TestCodeGen.test(input,expect,535))

	def test_ArrayCell_1(self):
		input = """
				int enter(int a[]){
        		    return a[0];
        		}
        		int i;

        		void main() {
        		    int a[9];
        		    a[0] = 1;
        		    putFloat(-----enter(a));
        		}
				"""
		expect = "-1.0"
		self.assertTrue(TestCodeGen.test(input,expect,536))

	def test_ArrayCell_2(self):
		input = """
				int i[10];
				float f[100];
				boolean b[1000];

				void main()
				{
					putInt(i[----------2]);
					putFloat(f[----------3]);
					putBool(b[----------4]);
				}
				"""
		expect = "00.0false"
		self.assertTrue(TestCodeGen.test(input,expect,537))

	def test_ArrayCell_3(self):
		input = """
		 		void main() {
           		    int b;
           		    b = foo()[1];
           		    foo()[1] = -5;
           		    putFloat(b);
           		    putFloat(foo()[1]);

           		    string c;
           		    c = foo2()[1];
           		    foo2()[1] = "Fool";
           		    putString(c);
           		    putString(foo2()[1]);
           		}

           		int[] foo(){
           		    int a[10];
           		    a[1] = -5 * 5;
           		    return a;
           		}

           		string[] foo2(){
           		    string a[10];
           		    a[1] = "Anh";
           		    return a;
           		}
				"""
		expect = "-25.0-25.0AnhAnh"
		self.assertTrue(TestCodeGen.test(input,expect,538))

	def test_ArrayCell_4(self):
		input = """
				int[] returnArray()
				{
					int i;
					int a[10];
					for(i = 0; i < 10; i = i + 1) a[i] = i * i;
					return a;
				}

				void main()
				{
					int b[10];
					putIntLn(-returnArray()[8]);
				}
				"""
		expect = "-64\n"
		self.assertTrue(TestCodeGen.test(input,expect,539))

	def test_ArrayCell_5(self):
		input = """
				void main() {
        	        int a[10];
        	        int i, j, k;
        	        for (i = 0; i < 10; i = i + 1)
        	            a[i] = i;

        	        for (j = 0; j < 10; j = j + 1)
        	            putInt(a[j]);

        	        for (k = 9; k >= 0; k = k - 1)
        	            putFloat(a[k]);
        	    }
				"""
		expect = "01234567899.08.07.06.05.04.03.02.01.00.0"
		self.assertTrue(TestCodeGen.test(input,expect,540))

	def test_Block_1(self):
		input = """
				void process(int a)
				{
					{
						int a;
						{
							a = 1;
							putIntLn(a);
						}
						{
							int a;
							a = 2;
							putIntLn(a);
						}
					}
					{
						{
							int a;
							{
								{
									{
										a = 4;
									}
								}
							}
							putIntLn(a);
						}
					}
				}

				void main()
				{
					{
						process(1000);
					}
				}
				"""
		expect = "1\n2\n4\n"
		self.assertTrue(TestCodeGen.test(input,expect,541))

	def test_Block_2(self):
		input = """
				void main() {
        		    boolean a;
        		    a = false;
        		    {
        		    	boolean a;
        		    	a = 5 > 3 + 1 * 2 - 3;
        		    }
        		    putBool(a);
        		    {
        		    	boolean a;
        		    	a = 1 + 2 + 3 + 4 + 5 + 6 < 100;
        		    }
        		    putBool(a);
        		    {
        		    	boolean a;
        		    	a = a = a = a = true;
        		    }
        		    putBool(a);
        		    {
        		    	boolean a;
        		    	a = 3 == 3;
        		    }
        		    putBool(a);
					{
						boolean a;
        		    	a = 3 != 9 * 8 / 7 + 3 * 5;
        		    }
        		    putBool(a);
					{
						boolean a;
        		    	a = 5 - 2.5 < 3 * 7.1 - 15;
        		    }
        		    putBool(a);
        		}
				"""
		expect = "falsefalsefalsefalsefalsefalse"
		self.assertTrue(TestCodeGen.test(input,expect,542))

	def test_Block_3(self):
		input = """
				void main()
				{
					{
						{
							{
								{
									{
										{
											{
												{
													{
														{
															putStringLn("Too muchhhhhhhhh");
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
				"""
		expect = "Too muchhhhhhhhh\n"
		self.assertTrue(TestCodeGen.test(input,expect,543))

	def test_Block_4(self):
		input = """
				int a;
        		void main() {
        		    putInt(a);
        		    {
						{
							int a;
						}
					}
        		}
				"""
		expect = "0"
		self.assertTrue(TestCodeGen.test(input,expect,544))

	def test_Block_5(self):
		input = """
				float a;
        		void main() {
        		    putFloat(a);
        		    float a;
        		    a = 1;
        		    {
        		        float a;
        		        a = 2;
        		        {
        		            float a;
        		            a = 3;
        		            {
        		                float a;
        		                a = 4;
        		                putFloatLn(a);
        		            }
        		            putFloatLn(a);
        		        }
        		        putFloatLn(a);
        		    }
        		    putFloatLn(a);
        		}
				"""
		expect = "0.04.0\n3.0\n2.0\n1.0\n"
		self.assertTrue(TestCodeGen.test(input,expect,545))

	def test_If_1(self):
		input = """
				float PI;
				void main()
				{
					PI = 3.14;
					float b;
        		    b = PI;
        		    if (b > 3)
        		        putFloat(b);
        		    else
        		        putFloat(b/2);
		
        		    if (b < 4)
        		        putFloat(2 * b);

        		    putFloat(PI);
				}
				"""
		expect = "3.146.283.14"
		self.assertTrue(TestCodeGen.test(input,expect,546))

	def test_If_2(self):
		input = """
				void main() {
        		    int a;
        		    a = 6;
        		      
        		    putInt(a);

        		    if (a > 55 && a < 10){
        		        putInt(a);
        		    }
        		    else{
        		        putInt(a+1);
        		    }

        		    if(true)
        		        if(true)
        		            if(false)
        		                if(true)
        		                    putInt(a);
        		                else
        		                    putInt(a+1);
        		            else
        		                putInt(a+2);
        		        else
        		            putInt(a+3);
        		    else
        		        putInt(a+4);
        		}
				"""
		expect = "678"
		self.assertTrue(TestCodeGen.test(input,expect,547))

	def test_If_3(self):
		input = """
				void main() {
        		    int a;
        		    a = 10;
        		    do
        		        a = a - 1;
        		        if (a == 1) break;
        		    while(a < 10);
        		    putInt(a);
        		}
				"""
		expect = "1"
		self.assertTrue(TestCodeGen.test(input,expect,548))

	def test_If_4(self):
		input = """
				void main()
				{	
					boolean b;
					int a;
					a = 5;
					if (a >= 1) putString("true");
					else 
						if (a == 2) putBool(false);
					else putBool(true);
					putBool(b = a < 9 );
				}
				"""
		expect = "truetrue"
		self.assertTrue(TestCodeGen.test(input,expect,549))

	def test_If_5(self):
		input = """
				void setup(){
					result = 0;
					i = 0;
				}

				void main()
				{
					setup();
					for (1; i < 10; i = i + 1)
        		        if (i == 5)
        		            break;
        		        else
        		            result = result * i;
        		    putInt(result);
        		    putLn();
				}

				int result, i;
				"""
		expect = "0\n"
		self.assertTrue(TestCodeGen.test(input,expect,550))

	def test_For_1(self):
		input = """
				int n;
				void main()
				{
					putStringLn("Enter a number:");
					n = 17;
					putInt(n);
					if(checkPrime(n)){
						putStringLn(" is a prime number!");
					}
					else{
						putStringLn(" is not a prime number!");
					}
				}

				boolean checkPrime(int n){
					int i;
					i = 2;
					for(1; i < n / 2; i = i + 1){
						if(n % i != 0) continue;
						else return false;
					}
					return true;
				}
				"""
		expect = "Enter a number:\n17 is a prime number!\n"
		self.assertTrue(TestCodeGen.test(input,expect,551))

	def test_For_2(self):
		input = """
				void main() {
        		    int i, j;
        		    for (i = 0; i < 5; i){
        		        putInt(i = i + 1);
						for(j = 0; j < 5; j){
							putInt(j = j + 1);
						}
					}
        		}
				"""
		expect = "112345212345312345412345512345"
		self.assertTrue(TestCodeGen.test(input,expect,552))

	def test_For_3(self):
		input = """
				int result;
				void main() {
					int i;
					int a[10], b[10], c[10];

        		    for (i = 0; i < 10; i = i + 1){
						a[i] = i * i;
        		        putInt(a[i]);
					}
        		    for (i = 0; i < 10; i = i + 1){
						b[i] = 2 * i;
        		        putInt(b[i]);
					}
        		    for (i = 0; i < 10; i = i + 1){
						c[i] = a[i] + b[i];
        		        result = result + c[i];
					}
					putInt(result);
        		}
				"""
		expect = "0149162536496481024681012141618375"
		self.assertTrue(TestCodeGen.test(input,expect,553))

	def test_For_4(self):
		input = """
				int a;

				int testFor()
				{
					int i;
					for(i = 0; i <= 10; i = i + 1) a = a * 2;
					{
						int a;
						a = 1;
						for(1;true;1)
						{
							putIntLn(a = a + 1);
							if (a == 10) break;
						}					
					}
					return a;
				}

				void main()
				{
					putIntLn(testFor());
				}
				"""
		expect = "2\n3\n4\n5\n6\n7\n8\n9\n10\n0\n"
		self.assertTrue(TestCodeGen.test(input,expect,554))

	def test_For_5(self):
		input = """
				void loop(int n){
					int i;
					i = 0;
					for(1 + 2 + 3; i < n; 5.0 / 2){
						putInt(i = i + 1);
					}
				}

				void main(){
					int a;
					a = 1;
					for(1; true; 1){
						loop(a = a + 1);
						if(a == 4) break;
					}
				}
				"""
		expect = "121231234"
		self.assertTrue(TestCodeGen.test(input,expect,555))

	def test_Dowhile_1(self):
		input = """
				void main() 
				{
        		    int i;
					i = 0;
					do
						i = i + 1;
					while(false);
					putInt(i);
        		}	
				"""
		expect = "1"
		self.assertTrue(TestCodeGen.test(input,expect,556))

	def test_Dowhile_2(self):
		input = """
				void main() {
        		    int j, result;
        		    result = j = 0;

        		    
        		    do
        		        {
							{
								{
									if (j <= 5)
        		            			result = result + 2;
        		        			else
        		            			result = result + 1;
								}
							}
						}
        		        j = j + 1;
        		    while (j < 10);
        		    putInt(result + j);
        		}
				"""
		expect = "26"
		self.assertTrue(TestCodeGen.test(input,expect,557))

	def test_Dowhile_3(self):
		input = """
				void main()
				{
					int i;
					i = 0;
				   	do
				   	{
						putStringLn("Still looping");
				  	}
				  	while((i = i + 1) < 5 * 2);
				   	putString("Out of loop");
				}
				"""
		expect = "Still looping\nStill looping\nStill looping\nStill looping\nStill looping\nStill looping\nStill looping\nStill looping\nStill looping\nStill looping\nOut of loop"
		self.assertTrue(TestCodeGen.test(input,expect,558))

	def test_Dowhile_4(self):
		input = """
				void main()
				{    
					int i, number;
					number = i = 0;
					do
					{    
						putIntLn((number = number + 1) * (i = i + 1));
					}
					while(i <= 10);    
				}    
				"""
		expect = "1\n4\n9\n16\n25\n36\n49\n64\n81\n100\n121\n"
		self.assertTrue(TestCodeGen.test(input,expect,559))

	def test_Dowhile_5(self):
		input = """
		void main()
		{
			int i, j;
			i = 1;
			j = 3;
			putStringLn("Enter a number: ");    
			do
			{    
				putString("This number = ");    
				i = j = i + 1;
			}
			{   
				putInt(j);
			}
			while(i <= 5);    
		}
		"""
		expect = "Enter a number: \nThis number = 2This number = 3This number = 4This number = 5This number = 6"
		self.assertTrue(TestCodeGen.test(input,expect,560))


	def test_Continue_1(self):
		input = """
				void main() {
					int i, j;
					for(i = 0; i <= 10; i = i + 1){
						if(i >= 5) continue;
						else{
							putInt(i);
							for(j = 0; j <= 10; j = j + 1){
								if(j >= 5) continue;
								else putInt(j);
							}
						}
					}
				}
				"""
		expect = "001234101234201234301234401234"
		self.assertTrue(TestCodeGen.test(input,expect,561))

	def test_Continue_2(self):
		input = """
		void main() {
			int i;

			for (i = 0; i < 10; i = i + 1)
			{
				int a;
				a = 6;
				for(1; true; 1){
					{
						putInt(a);
						{
							{
								if(a > 5 && a < 10){
									a = a + 1;
									continue;
								}
								else break;
							}
						}
					}
					putInt(a);
				}
			}
			putInt(i);

		}
		"""
		expect = "67891067891067891067891067891067891067891067891067891067891010"
		self.assertTrue(TestCodeGen.test(input,expect,562))

	def test_Continue_3(self):
		input = """
				void main()
				{
					int j;
					for (j = 0; j <= 10; j = j + 1)
				   	{
				      	if(j * j < 81) continue;

				       	putInt(j);
				       	putString(" ");
				    }
				}
				"""
		expect = "9 10 "
		self.assertTrue(TestCodeGen.test(input,expect,563))

	def test_Continue_4(self):
		input = """
				void main()
				{
					int a;
					a = 10;

					do 
					{
						if(a == 12){
							a = a + 1;
							continue;
						}
						a = a + 1;
						putInt(a);
					} 
					while(a < 14);
				}
				"""
		expect = "111214"
		self.assertTrue(TestCodeGen.test(input,expect,564))

	def test_Continue_5(self):
		input = """
				void main()
				{
					int j;
					j = 0;
				   	do
				   	{
				      	if(j == 7)
				      	{
				         	j = j * 2;
				         	continue;
				      	}
				      	putInt(j);
				      	putString(" ");
				      	j = j + 1;
				   	}
				   	while(j < 10);
				}
				"""
		expect = "0 1 2 3 4 5 6 14 "
		self.assertTrue(TestCodeGen.test(input,expect,565))

	def test_Continue_6(self):
		input = """
				int a, b[99];
				void main()
				{
					for(a; a < 6; a = a + 1){
						if(True() && (a == 4)){
							putInt(a);
							continue;
						}
						else{
							putString("Stop");
							break;
						}
					}
				}

				boolean True(){
					return true;
				}
				"""
		expect = "Stop"
		self.assertTrue(TestCodeGen.test(input,expect,566))

	def test_Continue_7(self):
		input = """
				int arr[15];
				int i;
				void main()
				{

					putStringLn("We have an array: ");
					for(1; i < 15; i = i + 1){
						arr[i] = i;
						if(i % 2 == 0) continue;
					}

					if(arr[i - 1] % 2 == 0){
						putStringLn("It's even");
					}
					else{
						putStringLn("It's odd");
					}
				}
				"""
		expect = "We have an array: \nIt's even\n"
		self.assertTrue(TestCodeGen.test(input,expect,567))

	def test_Continue_8(self):
		input = """
				int i;
				void main()
				{
					for (1; i <= 10; i = i + 1)
					{  
				        if (i == 6)  
				            continue; 
				        else
				        {
							putInt(i);
							putString("//");
				        } 
	    		    }

				}
				"""
		expect = "0//1//2//3//4//5//7//8//9//10//"
		self.assertTrue(TestCodeGen.test(input,expect,568))

	def test_Continue_9(self):
		input = """
				boolean even(int n){
					return n % 2 == 0;
				}
				void main()
				{
					int n;
					for(n = 0; n < 20; n = n + 1){
						if(even(n)) continue;
						else{
							if(odd(n/2)) putInt(n);
						}
					}
				}
				boolean odd(int n){
					return n % 2 == 1;
				}
				"""
		expect = "37111519"
		self.assertTrue(TestCodeGen.test(input,expect,569))

	def test_Continue_10(self):
		input = """
				void print(string s){
					putStringLn(s);
				}

				void main()
				{
					n = 3.14;
					if(n > 3){
						for(1; n < 7; 1){
							print("Loop for n");
							n = n + 1;
						}
					}
					else{
						print("Love PPL");
					}
					
				}

				float n;
				"""
		expect = "Loop for n\nLoop for n\nLoop for n\nLoop for n\n"
		self.assertTrue(TestCodeGen.test(input,expect,570))

	def test_Break_1(self):
		input = """
				void main()
				{
					for(1; true; 1) break;
				}
				"""
		expect = ""
		self.assertTrue(TestCodeGen.test(input,expect,571))

	def test_Break_2(self):
		input = """
				void main()
				{
					int i, j;
					i = j = 0;
					for(1; i <= 5; i = i + 1){
						for(1; j <= 7; j = j + 2){
							if(i * j > 20) break;
							putInt(i * j);
						}
					}
				}
				"""
		expect = "0000"
		self.assertTrue(TestCodeGen.test(input,expect,572))

	def test_Break_3(self):
		input = """
				void main(){
					int arr[10], n;
					int i;
					for(i = 0; i < 10; i = i + 1){
						arr[i] = i * i;
					}
					findValue(arr, 10, 64);
				}

				void findValue(int arr[], int size, int value){
					int i;
					for(i = 0; i < size; i = i + 1){
						if(arr[i] == value){
							putString("Found value(");
							putInt(value);
							putString(") at position: ");
							putIntLn(i);
							break;
						}
					}
				}
				"""
		expect = "Found value(64) at position: 8\n"
		self.assertTrue(TestCodeGen.test(input,expect,573))

	def test_Break_4(self):
		input = """
				void main()
				{
					string str[3];
					str[0] = "Oh no";
					str[1] = "Yessss";
					str[2] = "Damn.....";

					int i;
					for(i = 0; i < 3; i = i + 1){
						if(i == 2) break;
						putStringLn(clinit(str[i]));
					}
				}

				string clinit(string s){
					putString("Init");
					return s;
				}
				"""
		expect = "InitOh no\nInitYessss\n"
		self.assertTrue(TestCodeGen.test(input,expect,574))

	def test_Break_5(self):
		input = """
				void main()
				{
					int i;
				    float number, sum;
				    sum = 0.0;
				    for(i = 5; i >= -5; i = i-1)
				    {
					
				        putString("Enter a n:");
				        number = i - 2;
				        if(number < 0.0)
				        {
				            break;
				        }
				        sum = sum + number; 		    
				    }
				    putString("sum = ");
				    putFloatLn(sum);
				}
				"""
		expect = "Enter a n:Enter a n:Enter a n:Enter a n:Enter a n:sum = 6.0\n"
		self.assertTrue(TestCodeGen.test(input,expect,575))

	def test_Return_1(self):
		input = """
				void main()
				{
					one();
					two();
				}

				int one(){
					return 1;
				}

				float two(){
					return 2.0;
				}
				"""
		expect = ""
		self.assertTrue(TestCodeGen.test(input,expect,576))

	def test_Return_2(self):
		input = """
				void main()
				{
					putInt(one());
					putFloat(one());
					putFloat(two());
				}
				
				int one(){
					return 1;
				}

				float two(){
					return 2.0;
				}
				"""
		expect = "11.02.0"
		self.assertTrue(TestCodeGen.test(input,expect,577))

	def test_Return_3(self):
		input = """
				void main()
				{
					putInt(one());
					putFloat(one());
					putFloat(two());
					putString(getString("HAHAHA"));
				}
				
				int one(){
					return 1;
				}

				float two(){
					return 2.0;
				}

				string getString(string s){
					return s;
				}
				"""
		expect = "11.02.0HAHAHA"
		self.assertTrue(TestCodeGen.test(input,expect,578))

	def test_Return_4(self):
		input = """
				void main()
				{
					putInt(one());
					putFloat(one());
					putFloat(two());
					putInt(arr()[0]);
				}
				
				int one(){
					return 1;
				}

				float two(){
					return 2.0;
				}

				int[] arr(){
					int arr[1];
					arr[0] = 4;
					return arr;
				}
				"""
		expect = "11.02.04"
		self.assertTrue(TestCodeGen.test(input,expect,579))

	def test_Return_5(self):
		input = """
				int arr[9];
				void main()
				{
					putFloat(getArr(arr)[0]);
					changeArr(3);
					putFloat(getArr(arr)[0]);
				}

				int[] getArr(int arr[]){
					return arr;
				}

				void changeArr(int val){
					int i;
					for(i = 0; i < 9; i = i + 1){
						arr[i] = val;
					}
				}
				"""
		expect = "0.03.0"
		self.assertTrue(TestCodeGen.test(input,expect,580))

	def test_All_1(self):
		input = """
				int i;
				void main(){
                    for(1; i < 0; i = i + 1){
                        return;
                    }

                    putInt(1);
					putFloat(1);
					putBool(true);
					putString("Yeah");
                }
				"""
		expect = "11.0trueYeah"
		self.assertTrue(TestCodeGen.test(input,expect,581))

	def test_All_2(self):
		input = """
				int a[10];

				void main(){
                    int b;
                    b = 1;
                    a[b + 1] = b;

					check(a);
                }

				int check(int arr[]){
					int i;
					for(i = 0; i < 10; i = i + 1){
						if(arr[i] != 0){
							putString("Found a value!");
							return 1;
						}
					}
					putString("No value found!");
					return 0;
				}
				"""
		expect = "Found a value!"
		self.assertTrue(TestCodeGen.test(input,expect,582))

	def test_All_3(self):
		input = """
				int a[10];
				boolean global;

                void main(){
                    int b;
                    b = 1;
                    a[b + 1] = b;
                    int x;
                    {
                        string x;
                        {
                            {
                                {
                                    string x;
                                    {
                                        x = "OK";
                                    }
                                }
                            }
                        }
						x = "OK";
                        string b;
                        b = x;
                        
						putStringLn(b);
						check(a);
                    }
                    return;
                }

				int check(int arr[]){
					int i;
					for(i = 0; i < 10; i = i + 1){
						if(arr[i] != 0){
							putString("Found a value!");
							return 1;
						}
					}
					putString("No value found!");
					return 0;
				}
				"""
		expect = "OK\nFound a value!"
		self.assertTrue(TestCodeGen.test(input,expect,583))

	def test_All_4(self):
		input = """
				float maximum(float a, float b, float c){
                    if (a > b)
                    {
                        if (a > c) return a;
                        else return c;
                    }
                    else{
                        if (b > c) return b;
                        else return c;
                        }
                }

                float minimum(float a, float b, float c)
                {
                    if (a < b)
                    {
                        if (a < c) return a;
                        else return c;
                    }
                    else {
                	    if (b < c) return b;
                        else return c;
                    }
                }

		        void main(){
		        	putFloat(minimum(1, 3, 9) + maximum(99, 199, 299));
		        }
				"""
		expect = "300.0"
		self.assertTrue(TestCodeGen.test(input,expect,584))

	def test_All_5(self):
		input = """
				int first;
                boolean array[1000];
                
				void main(){
                    do{
                        array[first / 3] = (array[Return(Return(Return(Return(1))))] == true);
                    }
					while(array[first]);
                    putBool(array[first/3]);
                }

                int Return(int a){
                    return a;
                }
				"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input,expect,585))

	def test_All_6(self):
		input = """
				int first;

                void main(){
                    for(first = 0; first < 7; first = first + 1){
                        array();
                    }

					for(first = 0; first < 3; first = first + 1){
						putInt(array()[first]);
					}
                }

                int[] array(){
                    int input[3];
                    input[0] = 0;
                    input[1] = 1;
                    input[2] = 2;
                    return input;
                }

                int num(){
                    return first + 1;
                }
				"""
		expect = "012"
		self.assertTrue(TestCodeGen.test(input,expect,586))

	def test_All_7(self):
		input = """
				string str;
                boolean bool[99];
                void main(){
                    for(3; wrong(); 3){
                        do
                            str = "ABC";
                            putString(str);
                        while(bool[0]);
                    }
                }

                boolean wrong(){
                    return false;
                }
				"""
		expect = ""
		self.assertTrue(TestCodeGen.test(input,expect,587))

	def test_All_8(self):

		input = """
				float many;
				int man;
                void main(){
                    for(0; man <= many; man = man + 1){
                        for(1; true; 1){
                            print("Upin Ipin >.<");
							break;
                        }
                    }
                }

                void print(string str){
                    putStringLn(str);
                }
				"""
		expect = "Upin Ipin >.<\n"
		self.assertTrue(TestCodeGen.test(input,expect,588))

	def test_All_9(self):
		input = """
				int factorial(int n){
					int result, i;
					result = 1;
					for(i = 2; i <= n; i = i + 1){
						result = result * i;
					}
					return result;
				}

				void main(){
					putStringLn("Factorial of 10 is: ");
					putIntLn(factorial(10));
				}
				"""
		expect = "Factorial of 10 is: \n3628800\n"
		self.assertTrue(TestCodeGen.test(input,expect,589))

	def test_All_10(self):
		input = """
				void reverse(string s[], int size){
					int max, i;
					max = 2;
					for(i = 0; i <= max; i = i + 1){
						string temp;
						temp = s[i];
						s[i] = s[size - i - 1];
						s[size - i - 1] = temp;
					}
					for(i = 0; i < size; i = i + 1){
						putString(s[i]);
					}
				}

				string s[6];

				void main(){
					s[0] = "R";
					s[1] = "E";
					s[2] = "D";
					s[3] = "R";
					s[4] = "U";
					s[5] = "M";
					reverse(s, 6);
				}
		
				"""
		expect = "MURDER"
		self.assertTrue(TestCodeGen.test(input,expect,590))

	def test_All_11(self):
		input = """
                boolean b[999];

				void main(){
                    float a[3];
					a[2] = 3;
                    if(b[998] && true){
                        if(b[0] == true){
                            return;
                        }
                    }
					else{
                        a[--------------------------------2] = a[----------2] / 3;
                    }
                    putFloat(a[2]);
                }
				"""
		expect = "1.0"
		self.assertTrue(TestCodeGen.test(input,expect,591))

	def test_All_12(self):
		input = """
				void main(){
                    putInt(GCD(36, 6 * 17));
                }

                int GCD(int a, int b){
                    if (a == b) return a;
                    else {
						if(b > a) return GCD(a, b - a);
                        else return GCD(a - b, b);
                    }
                }
				"""
		expect = "6"
		self.assertTrue(TestCodeGen.test(input,expect,592))

	def test_All_13(self):

		input = """
				void main(){
                    int a[5];
					a[0] = 3;
					a[1] = 6;
					a[2] = 7;
					a[3] = 14;
					a[4] = 2;
					mulGCD(a, 5);
                }

				void mulGCD(int a[], int size){
					int mul;
					mul = 1;
					int i;
					for(i = 0; i < size - 1; i = i + 1){
						mul = mul * GCD(a[i], a[i + 1]);
					}
					putInt(mul);
				}

                int GCD(int a, int b){
                    if (a == b) return a;
                    else {
						if(b > a) return GCD(a, b - a);
                        else return GCD(a - b, b);
                    }
                }
				"""
		expect = "42"
		self.assertTrue(TestCodeGen.test(input,expect,593))

	def test_All_14(self):
		input = """
				void binary(int n){
					if(n == 0 || n == 1) putInt(n);
					else{
						binary(n / 2);
						putInt(n % 2);
					}
				}

				void main(){
					binary(54);
				}
				"""
		expect = "110110"
		self.assertTrue(TestCodeGen.test(input,expect,594))

	def test_All_15(self):
		input = """
				void trinary(int n){
					if(n == 0 || n == 1 || n == 2) putInt(n);
					else{
						trinary(n / 3);
						putInt(n % 3);
					}
				}

				void main(){
					trinary(54);
				}
				"""
		expect = "2000"
		self.assertTrue(TestCodeGen.test(input,expect,543))

	def test_All_16(self):
		input = """
				void message(string s){
					putString("Message: ");
					putStringLn(s);
				}

				void thank(string s){
					putString("Thanks to: ");
					putStringLn(s);
				}

				void wish(string s){
					putString("Wish: ");
					putStringLn(s);
				}

				void main(){
					thank("Mr.Phung");
					message("PPL is really cool");
					wish("All my best wishes!!!");
				}
				"""
		expect = "Thanks to: Mr.Phung\nMessage: PPL is really cool\nWish: All my best wishes!!!\n"
		self.assertTrue(TestCodeGen.test(input,expect,596))

	def test_All_17(self):
		input = """
				void message(string s){
					putString("Message: ");
					putStringLn(s);
				}

				void thank(string s){
					putString("Thanks to: ");
					putStringLn(s);
				}

				void wish(string s){
					putString("Wish: ");
					putStringLn(s);
				}

				void main(){
					thank("U");
					message("Running out of ideas and time to write testcases");
					message("Sorryyyyyyyyyyyyyyyyyyyyyy");
					wish("We all shall pass PPL <3");
				}
				"""
		expect = "Thanks to: U\nMessage: Running out of ideas and time to write testcases\nMessage: Sorryyyyyyyyyyyyyyyyyyyyyy\nWish: We all shall pass PPL <3\n"
		self.assertTrue(TestCodeGen.test(input,expect,597))

	def test_All_18(self):
		input = """
				void message(string s){
					putString("Message: ");
					putStringLn(s);
				}

				void thank(string s){
					putString("Thanks to: ");
					putStringLn(s);
				}

				void wish(string s){
					putString("Wish: ");
					putStringLn(s);
				}

				void main(){
					thank("");
					message("4 assignments in a course is insane!!!!");
					message("But hashtag #WorthIt");
					wish("We all shall pass PPL <3");
				}
				"""
		expect = "Thanks to: \nMessage: 4 assignments in a course is insane!!!!\nMessage: But hashtag #WorthIt\nWish: We all shall pass PPL <3\n"
		self.assertTrue(TestCodeGen.test(input,expect,598))

	def test_All_19(self):
		input = """
				void main(){
					putStringLn("OK it's enough!");
					putStringLn("To you who are reading this");
					putStringLn("Love yourself <3 you are better than who you think you are");
				}
				"""
		expect = "OK it's enough!\nTo you who are reading this\nLove yourself <3 you are better than who you think you are\n"
		self.assertTrue(TestCodeGen.test(input,expect,599))

	def test_All_20(self):
		input = """
				void main(){
					putStringLn("Good bye :))))))))))))))))");
				}
				"""
		expect = "Good bye :))))))))))))))))\n"
		self.assertTrue(TestCodeGen.test(input,expect,600))

