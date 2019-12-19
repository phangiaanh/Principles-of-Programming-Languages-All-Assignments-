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

	# def test_do_while_55(self):

	# 	input = """
	# 	void main() 
	# 	{
    #         testDoWhile();
    #     }

    #     void testDoWhile()
    #     {
	# 		int a;
    #         a = 0;
    #         do
    #             a = a + 1;
    #         while(a < 10);
    #         putInt(a);
    #     }	
	# 	"""
	# 	expect = "10"
	# 	self.assertTrue(TestCodeGen.test(input,expect,555))

	# def test_do_while_56(self):

	# 	input = """
	# 	void main() {
    #         int a;
    #         a = 0;
    #         do{
    #             int a;
    #             a = 7;
    #             a = a + 1;
    #         }
    #         a = a + 1;
    #         while(a < 10);
    #         putInt(a);

    #         int i, j, result;
    #         i = 0;
    #         j = 0;
    #         result = 0;

    #         j = 0;
    #         result = 0;
    #         do
    #             if (j == 5)
    #                 result = result + 2;
    #             else
    #                 result = result + 1;
    #             j = j + 1;
    #         while (j < 10);
    #         putInt(result);
    #     }
	# 	"""
	# 	expect = "1011"
	# 	self.assertTrue(TestCodeGen.test(input,expect,556))

	# def test_do_while_57(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int i;
	# 		i=0;
	# 	   	do
	# 	   	{
	# 			putStringLn("while vs do-while");
	# 	  	}
	# 	  	while(i==1);
	# 	   	putString("Out of loop");
	# 	}
	# 	"""
	# 	expect = "while vs do-while\nOut of loop"
	# 	self.assertTrue(TestCodeGen.test(input,expect,557))

	# def test_do_while_58(self):

	# 	input = """
	# 	void main()
	# 	{    
	# 		int i,number;
	# 		i=1;
	# 		number=0;    
	# 		putStringLn("Enter a number: ");    
	# 		number=10;
	# 		do
	# 		{    
	# 			putIntLn(number*i);    
	# 			i=i+1;
	# 		}
	# 		while(i<=10);    
	# 	}    
	# 	"""
	# 	expect = "Enter a number: \n10\n20\n30\n40\n50\n60\n70\n80\n90\n100\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,558))

	# def test_do_while_59(self):
	# 	input = """
	# 	void main()
	# 	{
	# 		int i,j,number;
	# 		i=1;
	# 		j=3;
	# 		putStringLn("Enter a number: ");    
	# 		number=10;
	# 		do
	# 		{    
	# 			putString("number * i = ");
	# 			putIntLn(number*i);    
	# 			i=i+1;
	# 		}
	# 		{
	# 			putString("number * j = ");
	# 			putIntLn(number*j);    
	# 			j=j+1;
	# 		}
	# 		while(i<=5);    
	# 	}
	# 	"""
	# 	expect = "Enter a number: \nnumber * i = 10\nnumber * j = 30\nnumber * i = 20\nnumber * j = 40\nnumber * i = 30\nnumber * j = 50\nnumber * i = 40\nnumber * j = 60\nnumber * i = 50\nnumber * j = 70\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,559))


	# def test_continue_60(self):

	# 	input = """
	# 	void main() {
	# 		int i,j;
	# 		i = 0;
	# 		do
	# 			i = i + 1;
	# 			if (i == 5)
	# 				break;
	# 		while (i < 10);
	# 		putInt(i);

	# 		j = 0;
	# 		i = 0;
	# 		do
	# 			i = i + 1;
	# 			if (i == 5)
	# 				continue;
	# 			j = j + 1;
	# 		while (i < 10);
	# 		putInt(i);
	# 		putInt(j);
	# 	}
	# 	"""
	# 	expect = "5109"
	# 	self.assertTrue(TestCodeGen.test(input,expect,560))

	# def test_continue_61(self):

	# 	input = """
	# 	void main() {
	# 		int i,j,result;
	# 		result = 0;

	# 		for (i = 0; i < 10; i = i + 1)
	# 		{
	# 			if (i == 5)
	# 				break;
	# 			else
	# 				result = result + 1;
	# 		}
	# 		putInt(result);
			

	# 		for (i = 0; i < 10; i = i + 1){
	# 			if (i == 100){
	# 				i = i + 100;
	# 				continue;
	# 			}
	# 			putInt(i);
	# 		}

	# 		putInt(i);

	# 	}
	# 	"""
	# 	expect = "5012345678910"
	# 	self.assertTrue(TestCodeGen.test(input,expect,561))

	# def test_continue_62(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int j;
	# 		for (j=0; j<=8; j=j+1)
	# 	   	{
		   		
	# 	      	if (j==4) continue;
		       	
	# 	       	putInt(j);
	# 	       	putString(" ");
	# 	    }
	# 	}
	# 	"""
	# 	expect = "0 1 2 3 5 6 7 8 "
	# 	self.assertTrue(TestCodeGen.test(input,expect,562))

	# def test_continue_63(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int a;
	# 		a=10;

	# 		do 
	# 		{
	# 			if(a == 15) {
	# 				a = a + 1;
	# 				continue;
	# 			}
					
	# 			putString("value of a: ");
	# 			putInt(a);
	# 			a=a+1;
	# 		} 
	# 		while( a < 20 );
	# 	}
	# 	"""
	# 	expect = "value of a: 10value of a: 11value of a: 12value of a: 13value of a: 14value of a: 16value of a: 17value of a: 18value of a: 19"
	# 	self.assertTrue(TestCodeGen.test(input,expect,563))

	# def test_continue_64(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int j;
	# 		j=0;
	# 	   	do
	# 	   	{
	# 	      	if (j==7)
	# 	      	{
	# 	         	j=j+1;
	# 	         	continue;
	# 	      	}
	# 	      	putInt(j);
	# 	      	putString(" ");
	# 	      	j=j+1;
	# 	   	}
	# 	   	while(j<10);
	# 	}

	# 	"""
	# 	expect = "0 1 2 3 4 5 6 8 9 "
	# 	self.assertTrue(TestCodeGen.test(input,expect,564))

	# def test_continue_65(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int i,j;
	# 		i=1;
	# 		j=1;  
	# 		for(i=1;i<=3;i=i+1)
	# 		{      
	# 			for(j=1;j<=3;j=j+1)
	# 			{    
	# 				if(i==2 && j==2){    
	# 					continue;   
	# 				} 
	# 			}    
	# 			putInt(i);
	# 			putString(" ");
	# 			putInt(j);
	# 			putStringLn("");
	# 		}    
	# 	}
	# 	"""
	# 	expect = "1 4\n2 4\n3 4\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,565))

	# def test_continue_66(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int i, number;

	# 		putString("\\nPlease Enter any integer\\n");
	# 		number=5;

	# 		for(i=1;i<= number; i=i+1)
	# 		{
	# 		   	if(i%2 != 0)
	# 		   	{
	# 		     	putString("\\nOdd Numbers = ");
	# 		     	putInt(i);
	# 		     	putStringLn(" (Skipped By Continue)");
	# 		     	continue;
	# 		   	}

	# 		   	putString("\\nEven numbers = ");
	# 		   	putIntLn(i);
	# 		}
	# 	}
	# 	"""
	# 	expect = "\nPlease Enter any integer\n\nOdd Numbers = 1 (Skipped By Continue)\n\nEven numbers = 2\n\nOdd Numbers = 3 (Skipped By Continue)\n\nEven numbers = 4\n\nOdd Numbers = 5 (Skipped By Continue)\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,566))

	# def test_continue_67(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int i;
	# 		for (i = 1; i <= 10; i=i+1)
	# 		{  
	# 	        if (i == 6)  
	# 	            continue; 
	# 	        else
	# 	        {
	# 				putInt(i);
	# 				putString(" ");
	# 	        } 
	#         }
  
	# 	}
	# 	"""
	# 	expect = "1 2 3 4 5 7 8 9 10 "
	# 	self.assertTrue(TestCodeGen.test(input,expect,567))

	# def test_continue_68(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int i,j,k;
	# 		for (i = 0; i < 10; i=i+1) 
	# 		{
	# 	        if (i != 5) continue;
	# 	        putInt(i);
	# 	        putString(" ");
	# 	    }
	# 	 	putLn();
		 
	# 	    for (j = 0; j < 2; j=j+1) {
	# 	        for (k = 0; k < 5; k=k+1) {   
	# 	            if (k == 3) continue;
	# 	            putInt(j);
	# 	            putInt(k);
	# 	            putString(" ");
	# 	        }
	# 	    }
	# 	}
	# 	"""
	# 	expect = "5 \n00 01 02 04 10 11 12 14 "
	# 	self.assertTrue(TestCodeGen.test(input,expect,568))

	# def test_continue_69(self):
	# 	input = """
	# 	void main()
	# 	{
	# 		for (num=0; num<=6; num=num+2) {
    
	# 		    if (num==3) {
	# 		        continue;
	# 		    }
	# 		    putInt(num);
	# 		    putString(" ");
   	# 		}
	# 	}

	# 	int num;
	# 	"""
	# 	expect = "0 2 4 6 "
	# 	self.assertTrue(TestCodeGen.test(input,expect,569))

	# def test_break_70(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int i;  
	# 	    for(i = 0; i<10; i=i+1)  
	# 	    {  
	# 	    	putInt(i);
	# 	    	putString(" ");
	# 	        if(i == 5) break;  
	# 	    }  
	# 	    putLn();
	# 	    putString("came outside of loop i = ");
	# 	    putIntLn(i);
	# 	}
	# 	"""
	# 	expect = "0 1 2 3 4 5 \ncame outside of loop i = 5\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,570))

	# def test_break_71(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int i,j;
	# 		i=1;
	# 		j=1;   
	# 		for(i=1;i<=3;i=i+1)
	# 		{      
	# 			for(j=1;j<=3;j=j+1)
	# 			{    
	# 				putInt(i);
	# 				putString(" ");
	# 				putInt(j);
	# 				putLn();    
	# 				if(i==2 && j==2)
	# 				{    
	# 					break;   
	# 				}		    
	# 			}
	# 		}
	# 	}
	# 	"""
	# 	expect = "1 1\n1 2\n1 3\n2 1\n2 2\n3 1\n3 2\n3 3\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,571))

	# def test_break_72(self):

	# 	input = """
	# 	void findElement(int arr[], int size, int key) 
	# 	{ 
	# 		int i;
	# 	    for (i = 0; i < size; i=i+1) { 
	# 	        if (arr[i] == key) { 
		  			
	# 	  			putString("Element found at position: ");
	# 	  			putIntLn(i+1);
	# 	            break; 
	# 	        } 
	# 	    } 
	# 	} 
		  
	# 	void main() 
	# 	{ 
	# 		int arr[6],i,n,key;
	# 		n=6;
	# 		key=3;
	# 		for(i=1;i<=6;i=i+1) arr[i-1]=i;
	# 	    findElement(arr, n, key); 
	# 	} 
	# 	"""
	# 	expect = "Element found at position: 3\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,572))

	# def test_break_73(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int n,i,choice;
	# 		n=20;  
			
	# 		do  
	# 		{  
	# 		    choice=n%17;
	# 		    if(choice == 0)  
	# 		    {  
	# 		        break;  
	# 		    }  
	# 		    n=n+1;  
	# 		}
	# 		while(true);  

	# 		putIntLn(n);
	# 	}
	# 	"""
	# 	expect = "34\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,573))

	# def test_break_74(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int i;
	# 	    float number, sum;
	# 	    sum=0.0;
	# 	    for(i=5; i >= -5; i=i-1)
	# 	    {

	# 	        putString("Enter a n:");
	# 	        number=i-2;
	# 	        if(number < 0.0)
	# 	        {
	# 	            break;
	# 	        }
	# 	        sum = sum + number; 		    
	# 	    }
	# 	    putString("sum = ");
	# 	    putFloatLn(sum);
	# 	}
	# 	"""
	# 	expect = "Enter a n:Enter a n:Enter a n:Enter a n:Enter a n:sum = 6.0\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,574))

	# def test_return_75(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,575))

	# def test_return_76(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,576))

	# def test_return_77(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,577))

	# def test_return_78(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,578))

	# def test_return_79(self):
	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,579))

	# def test_program_80(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int a;
	# 		a = 2;
	# 		int b;
	# 		b = a;
	# 		a;
	# 		1+1;
	# 		putInt(b);
	# 	}
	# 	"""
	# 	expect = "2"
	# 	self.assertTrue(TestCodeGen.test(input,expect,580))

	# def test_program_81(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,581))

	# def test_program_82(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,582))

	# def test_program_83(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,583))

	# def test_program_84(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,584))

	# def test_program_85(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,585))

	# def test_program_86(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,586))

	# def test_program_87(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,587))

	# def test_program_88(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,588))

	# def test_program_89(self):
	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,589))

	# def test_program_90(self):
	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,590))

	# def test_program_91(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,591))

	# def test_program_92(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,592))

	# def test_program_93(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,593))

	# def test_program_94(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,594))

	# def test_program_95(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,595))

	# def test_program_96(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,596))

	# def test_program_97(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,597))

	# def test_program_98(self):

	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,598))

	# def test_program_99(self):
	# 	input = """
	# 	void main()
	# 	{
		
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,599))

