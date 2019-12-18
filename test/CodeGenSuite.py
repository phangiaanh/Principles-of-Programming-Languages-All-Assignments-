import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
	# def test_func_decl_0(self):

	# 	input = """

	# 	void cmp()
	# 	{
	# 		float m;
	# 		m=1.2;

	# 		int x;
	# 		x=2;

	# 		if (m>5) x=2;
	# 	}


	# 	void main()
	# 	{
	# 		putInt(2);
	# 	}

	# 	"""
	# 	expect = "2"
	# 	self.assertTrue(TestCodeGen.test(input,expect,500))

	# def test_func_decl_1(self):

	# 	input = """

	# 	int get()
	# 	{
	# 		putInt(2+3);
	# 		putInt(3+5);
	# 		return 1;
	# 	}

	# 	void main()
	# 	{
	# 		get();
	# 	}
	# 	"""
	# 	expect = "58"
	# 	self.assertTrue(TestCodeGen.test(input,expect,501))

	# def test_func_decl_2(self):

	# 	input = """

	# 	float get()
	# 	{
	# 		return 1.0;
	# 	}

	# 	void main()
	# 	{
	# 		putFloat(get());
	# 	}
	# 	"""
	# 	expect = "1.0"
	# 	self.assertTrue(TestCodeGen.test(input,expect,502))

	# def test_func_decl_3(self):

	# 	input = """

	# 	string enter()
	# 	{
	# 		return "hello";
	# 	}

	# 	void main()
	# 	{
	# 		putString(enter());
	# 	}
	# 	"""
	# 	expect = "hello"
	# 	self.assertTrue(TestCodeGen.test(input,expect,503))

	# def test_func_decl_4(self):

	# 	input = """

	# 	boolean check()
	# 	{
	# 		return true;
	# 	}

	# 	void main()
	# 	{
	# 		putBool(check());
	# 	}
	# 	"""
	# 	expect = "true"
	# 	self.assertTrue(TestCodeGen.test(input,expect,504))

	# def test_call_expr_5(self):

	# 	input = """	

	# 	float f;

	# 	void main()
	# 	{
	# 		f=3;

	# 		putIntLn(2);
	# 		testFloat(f);
	# 	}
		
	# 	void testFloat(float f)
	# 	{
	# 		putFloatLn(f);
	# 	}


	# 	"""
	# 	expect = "2\n3.0\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,505))

	# def test_call_expr_6(self):

	# 	input = """

	# 	void enter(int n)
	# 	{
	# 		int i;
	# 		for(i=1;i<=n;i=i+1) putIntLn(i);
	# 	}

	# 	void main()
	# 	{
	# 		enter(10);
	# 		putFloatLn(2.39+2.3);
	# 	}
	# 	"""
	# 	expect = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n4.69\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,506))

	# def test_call_expr_7(self):

	# 	input = """

	# 	boolean checkPrime(int n)
	# 	{
	# 		int i;
	# 		if (n==1) return false;
	# 		for(i=2;i<=n-1;i=i+1)
	# 			if (n%i==0) return false;
	# 		return true;
	# 	}

	# 	void main()
	# 	{
	# 		putBoolLn(true||false&&true&&false);

	# 		putBool(checkPrime(1));
	# 		putBool(checkPrime(2));
	# 		putBool(checkPrime(3));
	# 		putBool(checkPrime(4));
	# 		putBool(checkPrime(5));
	# 	}
	# 	"""
	# 	expect = "true\nfalsetruetruefalsetrue"
	# 	self.assertTrue(TestCodeGen.test(input,expect,507))

	# def test_call_expr_8(self):

	# 	input = """

	# 	int sum(int a[],int l)
	# 	{
	# 		int tmp,i;
	# 		tmp=0;
	# 		for(i=0;i<l;i=i+1) tmp=tmp+a[i];
	# 		return tmp;
	# 	}

	# 	int ia[10];


	# 	void main()
	# 	{
	# 		putStringLn("2.3");

	# 		int i;
			
	# 		for(i=0;i<10;i=i+1) ia[i]=i;
	# 		for(i=0;i<10;i=i+1) fa[i]=i+1;
			
	# 		putIntLn(sum(ia,10));
	# 		putFloatLn(multiply(fa,10));
	# 	}
		
		
	# 	float fa[10];

	# 	float multiply(float a[],int l)
	# 	{
	# 		float tmp;
	# 		int i;
	# 		tmp=1;
	# 		for(i=0;i<l;i=i+1) tmp=tmp*a[i];
	# 		return tmp;
	# 	}
		
	# 	"""
	# 	expect = "2.3\n45\n3628800.0\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,508))

	# def test_call_expr_9(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		putIntLn(2);
	# 		putFloatLn(2.3+2.3);
	# 		putBoolLn(true||false&&true&&false);
	# 		putStringLn("2.3");
	# 	}
	# 	"""
	# 	expect = "2\n4.6\ntrue\n2.3\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,509))

	# def test_int_literal_10(self):

	# 	input = """

	# 	int a;

	# 	void printMultipleInt()
	# 	{
	# 		a=1*2*3/3*4*5;
	# 		putFloatLn(a);
	# 	}

	# 	void main()
	# 	{
	# 		a=1+2+3+4+5+6+7+8+9+10;
	# 		putFloatLn(a);
	# 		printMultipleInt();
	# 	}
	# 	"""
	# 	expect = "55.0\n40.0\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,510))

	# def test_bool_literal_11(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		b=!(true&&true||false||false);
	# 		putBool(b);
	# 	}

	# 	boolean b;
	# 	"""
	# 	expect = "false"
	# 	self.assertTrue(TestCodeGen.test(input,expect,511))

	# def test_string_literal_12(self):

	# 	input = """

	# 	string a;

	# 	void main()
	# 	{
	# 		a=getHelloString();
	# 		putStringLn(a);
	# 	}

	# 	string getHelloString()
	# 	{
	# 		return "hello";
	# 	}
	# 	"""
	# 	expect = "hello\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,512))

	# def test_float_literal_13(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		putFloatLn(getFloatLiteral());
	# 	}

	# 	float getFloatLiteral()
	# 	{
	# 		float m;
	# 		m=1;
	# 		m=1-2;
	# 		return m;
	# 	}
	# 	"""
	# 	expect = "-1.0\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,513))

	# def test_array_literal_14(self):

	# 	input = """

	# 	int a[100],i;

	# 	void main()
	# 	{
	# 		for(i=1;i<10;i=i+2) a[i]=i%2;

	# 		for(i=0;i<10;i=i+1) putIntLn(a[i]);
	# 	}
	# 	"""
	# 	expect = "0\n1\n0\n1\n0\n1\n0\n1\n0\n1\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,514))

	# def test_var_decl_15(self):

	# 	input = """

	# 	int a0,a1[1],a2,a3[3],a4,a5[5];

	# 	float f0[1],f1,f2[1],f3,f4[3];
	# 	boolean b0,b1[1],b2,b3[3],b4;


	# 	void declareVar()
	# 	{
	# 		int a0,a2,a4;
	# 		int a1[1],a3[3],a5[5];
	# 		putBool(b0);
	# 	}

	# 	void main()
	# 	{
	# 		declareVar();
	# 	}
	# 	"""
	# 	expect = "false"
	# 	self.assertTrue(TestCodeGen.test(input,expect,515))

	# def test_var_decl_16(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		float a;
	# 		a=1.0;
	# 		{
	# 			int a;
	# 			a=5;
	# 			putFloatLn(a);
	# 		}
	# 		putFloat(a);
	# 	}
	# 	"""
	# 	expect = "5.0\n1.0"
	# 	self.assertTrue(TestCodeGen.test(input,expect,516))

	# def test_var_decl_17(self):

	# 	input = """
	# 	string a[30],b;

	# 	void main()
	# 	{
	# 		int i;
	# 		for(i=0;i<5;i=i+1) a[i]="1";
	# 		for(i=0;i<5;i=i+1) putString(a[i]);
	# 		b=a[4];
	# 		putStringLn(b);
	# 	}
	# 	"""
	# 	expect = "111111\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,517))

	# def test_var_decl_18(self):

	# 	input = """
	# 	int a[30];
	# 	void main()
	# 	{
	# 		{
	# 			int a;
	# 		}
	# 		int b;
	# 		float c;
	# 		boolean d;
	# 		string e;

	# 		for(b=0;b<30;b=b+1) putIntLn(b);
	# 	}
	# 	"""
	# 	expect = "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,518))

	# def test_var_decl_19(self):

	# 	input = """

	# 	int a0[0];
	# 	boolean b0[0];
	# 	string c0[0];
	# 	float d0[0];

	# 	void main()
	# 	{
	# 	}
	# 	"""
	# 	expect = ""
	# 	self.assertTrue(TestCodeGen.test(input,expect,519))

	# def test_binary_op_20(self):

	# 	input = """

	# 	float a;

	# 	void main()
	# 	{
	# 		a=1+2+3+1.0+1.1+1.2+1.3;
	# 		putFloatLn(a+10);
	# 	}
	# 	"""
	# 	expect = "20.6\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,520))

	# def test_binary_op_21(self):

	# 	input = """
		
	# 	int a;
	# 	boolean b;

	# 	void main()
	# 	{
	# 		a=2;
	# 		b=a==1 || a==2;
	# 		putBoolLn(b);
	# 	}
	# 	"""
	# 	expect = "true\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,521))

	# def test_binary_op_22(self):

	# 	input = """

	# 	void main()
	# 	{	
	# 		int i;
	# 		for(i=1+2+3;i>=0;i=i-1)
	# 		{
	# 			putBool(i*i>=5);
	# 			putBoolLn((i*i)%2==1-1);
	# 		}
	# 	}
	# 	"""
	# 	expect = "truetrue\ntruefalse\ntruetrue\ntruefalse\nfalsetrue\nfalsefalse\nfalsetrue\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,522))

	# def test_binary_op_23(self):

	# 	input = """
		
	# 	int i;

	# 	boolean cmpGE(int a,int b)
	# 	{
	# 		return (a>=b);
	# 	}

	# 	boolean cmpLE(int a,int b)
	# 	{
	# 		return (a<=b);
	# 	}
	
	# 	void main()
	# 	{
	# 		i=5;
	# 		do
	# 		{
	# 			putString("Just for fun\\n");
	# 		}
	# 		while (i>=5+1+2+3+4+5+6);
		
			
	# 		1*2*3*4*5*6*7*8*9;
	# 		i==6;
	
	# 		putBoolLn(cmpGE(6,6));
	# 		putBoolLn(cmpGE(6,6));
	# 	}
	# 	"""
	# 	expect = "Just for fun\ntrue\ntrue\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,523))

	# def test_binary_op_24(self):

	# 	input = """
		
	# 	int tmp,i;

	# 	void main()
	# 	{
	# 		tmp=1;
	# 		for(i=0;i<2019;i=i+1) tmp=(tmp*5)%13;

	# 		putIntLn(tmp);
	# 	}
	# 	"""
	# 	expect = "8\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,524))

	# def test_unary_op_25(self):

	# 	input = """
	# 	int i;
	# 	void main()
	# 	{
	# 		for(i=10;i>=5;i=i-1) putIntLn(-i*2);
	# 		for(i=10;i>=5;i=i-1) putBoolLn(!(i*2==10));
	# 	}
	# 	"""
	# 	expect = "-20\n-18\n-16\n-14\n-12\n-10\ntrue\ntrue\ntrue\ntrue\ntrue\nfalse\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,525))

	# def test_unary_op_26(self):

	# 	input = """
	# 	int a[99];

	# 	void main()
	# 	{
	# 		int b[99];
	# 		b[--0*-0]=--1;
	# 		putInt(b[0]);
	# 	}
	# 	"""
	# 	expect = "1"
	# 	self.assertTrue(TestCodeGen.test(input,expect,526))

	# def test_unary_op_27(self):

	# 	input = """

	# 	float a;
	# 	boolean b;

	# 	void check() {
    #         int a[10];
    #         a[1] = --2;
    #         a[3] = ----1;
    #         a[2] = ------6;
    #         putInt(a[a[a[3-1+1*1/1]]]);
    #     }

	# 	void main()
	# 	{
	# 		a=----1--2;
	# 		putFloatLn(a);

	# 		b=!true || !false;
	# 		putBoolLn(b);
	# 		check();
	# 	}
	# 	"""
	# 	expect = "3.0\ntrue\n6"
	# 	self.assertTrue(TestCodeGen.test(input,expect,527))

	# def test_unary_op_28(self):

	# 	input = """
	# 	int i;

	# 	void main()
	# 	{
	# 		float a;
	# 		a=10;

	# 		for(i=0;i<10;i=i+1) a=-a;
	# 		putFloatLn(a);
	# 	}
	# 	"""
	# 	expect = "10.0\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,528))

	# def test_unary_op_29(self):

	# 	input = """
		
	# 	int i,a[20];
	# 	string b;

	# 	void setup()
	# 	{
	# 		for(i=0;i<10;i=i+1) a[i]=i;
	# 	}

	# 	void main()
	# 	{
	# 		b="--12";
	# 		setup();
			
	# 		for(i=2;i<10;i=i+1) a[i]=a[a[i-1]*(--1)];
	# 		for(i=0;i<10;i=i+1) putIntLn(a[i]);
	# 		putStringLn(b);
	# 	}
	# 	"""
	# 	expect = "0\n1\n1\n1\n1\n1\n1\n1\n1\n1\n--12\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,529))

	# def test_id_30(self):

	# 	input = """

	# 	string random;
	# 	int one;

	# 	string getRandomString()
	# 	{
	# 		return "random";
	# 	}

	# 	void main()
	# 	{
	# 		random=getRandomString();
	# 		one=getOne();

	# 		putStringLn(random);
	# 		putIntLn(one);
	# 	}

	# 	int getOne()
	# 	{
	# 		return 1;			
	# 	}
	# 	"""
	# 	expect = "random\n1\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,530))

	# def test_id_31(self):

	# 	input = """
	# 	int i;

	# 	void main()
	# 	{
	# 		string a[10],b[10];

	# 		for(i=0;i<10;i=i+1) a[i]="a";
	# 		for(i=0;i<10;i=i+1) b[i]=a[i];
			
	# 		for(i=0;i<10;i=i+1) putString(a[i]);
	# 		for(i=0;i<10;i=i+1) putString(b[i]);
	# 	}

	# 	"""
	# 	expect = "aaaaaaaaaaaaaaaaaaaa"
	# 	self.assertTrue(TestCodeGen.test(input,expect,531))

	# def test_id_32(self):

	# 	input = """

	# 	int i;

	# 	void main()
	# 	{
	# 		for(i=0;i<10;i=i+1) a[i]="a";
	# 		for(i=0;i<10;i=i+1) b[i]=a[i];

	# 		{
	# 			string b[10];
	# 			for(i=0;i<10;i=i+1) b[i]="b";
	# 		}

	# 		for(i=0;i<10;i=i+1) putString(a[i]);
	# 		for(i=0;i<10;i=i+1) putString(b[i]);
	# 	}

	# 	string a[10],b[10];
	# 	"""
	# 	expect = "aaaaaaaaaaaaaaaaaaaa"
	# 	self.assertTrue(TestCodeGen.test(input,expect,532))

	# # def test_id_33(self):

	# # 	input = """
	# # 	void main()
	# # 	{
	# # 		float f;
	# # 		f=1;
			
	# # 		setInt(1);

	# # 		if (f==i)
	# # 		{
	# # 			putString("Float is equal to int");
	# # 		}
	# # 		else
	# # 		{
	# # 			putString("Float is not equal to int");
	# # 		}
	# # 	}

	# # 	int i;

	# # 	void setInt(int k)
	# # 	{
	# # 		i=k;
	# # 	}
	# # 	"""
	# # 	expect = "Float is equal to int"
	# # 	self.assertTrue(TestCodeGen.test(input,expect,533))

	# def test_id_34(self):

	# 	input = """
	# 	int i,j,l,a[10],mul;
		
	# 	int[] returnArray()
	# 	{
	# 		int a[11];
	# 		for(j=0;j<l;j=j+1) a[j]=j+1;

	# 		return a;
	# 	}

	# 	void main()
	# 	{
	# 		l=10;

	# 		mul=1;
	# 		for(i=0;i<l;i=i+1) mul=mul*returnArray()[i];
	# 		putIntLn(mul);
	# 	}
	# 	"""
	# 	expect = "3628800\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,534))

	# def test_array_cell_35(self):

	# 	input = """

	# 	int enter(int a[]){
    #         return a[0];
    #     }
    #     int i;

    #     void main() {
    #         int a[9];
    #         a[0] = 1;
    #         putFloat(enter(a));
			
    #     }
	# 	"""
	# 	expect = "1.0"
	# 	self.assertTrue(TestCodeGen.test(input,expect,535))

	# def test_array_cell_36(self):

	# 	input = """

	# 	int i[10];
	# 	float f[100];
	# 	boolean b[1000];

	# 	void main()
	# 	{
	# 		putInt(i[2]);
	# 		putFloat(f[3]);
	# 		putBool(b[4]);
	# 	}
	# 	"""
	# 	expect = "00.0false"
	# 	self.assertTrue(TestCodeGen.test(input,expect,536))

	# def test_array_cell_37(self):

	# 	input = """
	# 	 void main() {
    #             int b;
    #             b = foo()[1];
    #             foo()[1] = 5;
    #             putInt(b);
    #             putInt(foo()[1]);

    #             string c;
    #             c = foo2()[1];
    #             foo2()[1] = "haha";
    #             putString(c);
    #             putString(foo2()[1]);
    #         }

    #         int[] foo(){
    #             int a[10];
    #             a[1] = 5;
    #             return a;
    #         }

    #         string[] foo2(){
    #             string a[10];
    #             a[1] = "thong";
    #             return a;
    #         }
	# 	"""
	# 	expect = "55thongthong"
	# 	self.assertTrue(TestCodeGen.test(input,expect,537))

	# def test_array_cell_38(self):

	# 	input = """

	# 	int[] returnArray()
	# 	{
	# 		int i;
	# 		int a[10];
	# 		for(i=0;i<10;i=i+1) a[i]=i;
	# 		return a;
	# 	}

	# 	void main()
	# 	{
	# 		int b[10];
	# 		putIntLn(returnArray()[9]);
	# 	}
	# 	"""
	# 	expect = "9\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,538))

	# def test_array_cell_39(self):

	# 	input = """
	# 	 void main() {
    #             int a[10];
    #             int i,j,k;
    #             for (i = 0; i < 10; i = i + 1)
    #                 a[i] = i;

    #             for (j = 0; j < 10; j = j + 1)
    #                 putInt(a[j]);

    #             for (k = 9; k >= 0; k = k - 1)
    #                 putInt(a[k]);
    #         }
	# 	"""
	# 	expect = "01234567899876543210"
	# 	self.assertTrue(TestCodeGen.test(input,expect,539))

	# def test_block_40(self):

	# 	input = """
	# 	void process(int a)
	# 	{
	# 		{
	# 			{
	# 				int a;
	# 				a=1;
	# 				putIntLn(a);
	# 			}
	# 			{
	# 				int a;
	# 				a=2;
	# 				putIntLn(a);
	# 			}
	# 		}
	# 		{
	# 			{
	# 				int a;
	# 				a=3;
	# 				putIntLn(a);
	# 			}
	# 			{
	# 				int a;
	# 				a=4;
	# 				putIntLn(a);
	# 			}
	# 		}
	# 	}

	# 	void main()
	# 	{
	# 		{
	# 			process(1000);
	# 		}
	# 	}
	# 	"""
	# 	expect = "1\n2\n3\n4\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,540))

	# def test_block_41(self):

	# 	input = """
	# 	void main() {
    #         boolean a;
    #         a=false;


    #         {
    #         	boolean a;
    #         	a = 5 > 3 + 1;
    #         }
    #         putBool(a);


    #         {
    #         	boolean a;
    #         	a = 5+1-------1 <= 5;
    #         }
    #         putBool(a);

    #         {
    #         	boolean a;
    #         	a = 5*9 >= 9*5;
    #         }
    #         putBool(a);


    #         {
    #         	boolean a;
    #         	a = 5*30 == 3*7;
    #         }
    #         putBool(a);
			
	# 		{
	# 			boolean a;
    #         	a = 5 != 3+2;
    #         }
    #         putBool(a);
			
	# 		{
	# 			boolean a;
    #         	a = 5 - 2.5 < 3 * 7.1 -15;
    #         }
    #         putBool(a);

    #         {
    #         	boolean a;
    #         	a = 5*3 == 3*5;
    #         }
    #         putBool(a);
    #     }
	# 	"""
	# 	expect = "falsefalsefalsefalsefalsefalsefalse"
	# 	self.assertTrue(TestCodeGen.test(input,expect,541))

	# def test_block_42(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		{{{{{{{putLn();}}}}}}}
	# 	}
	# 	"""
	# 	expect = "\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,542))

	# def test_block_43(self):

	# 	input = """
		
	# 	int a;
    #     void main() {
    #         putInt(a);
    #         int a;
    #     }

	# 	"""
	# 	expect = "0"
	# 	self.assertTrue(TestCodeGen.test(input,expect,543))

	# def test_block_44(self):

	# 	input = """
	# 	float a;
    #     void main() {
    #         putFloat(a);
    #         float a;
    #         a = 1;
    #         {
    #             float a;
    #             a = 2;
    #             {
    #                 float a;
    #                 a = 3;
    #                 {
    #                     float a;
    #                     a = 4;
    #                     putFloat(a);
    #                 }
    #                 putFloat(a);
    #             }
    #             putFloat(a);
    #         }
    #         putFloat(a);
    #     }
	# 	"""
	# 	expect = "0.04.03.02.01.0"
	# 	self.assertTrue(TestCodeGen.test(input,expect,544))

	# def test_if_45(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int a;
    #         a = 6;
    #         if (a > 7)
    #             putInt(a);
    #         else
    #             putInt(a+1);

    #         if (a < 10)
    #             putInt(a+2);
    #         putInt(a+3);
	# 	}
	# 	"""
	# 	expect = "789"
	# 	self.assertTrue(TestCodeGen.test(input,expect,545))

	# def test_if_46(self):

	# 	input = """
	# 	void main() {
    #         int a;
    #         a = 6;
    #         if (a > 5 && a < 10)
    #             putInt(a);
			
    #         if (a > 5)
    #             if (a < 10)
    #                 putInt(a);
			
    #         if (a > 5 && a < 10){
    #             int a;
    #             a = 11;
    #             putInt(a);
    #             putInt(a+1);
    #             putInt(a+2);
    #         }
    #         putInt(a);

    #         if (a > 55 && a < 10){
    #             putInt(a);
    #         }
    #         else{
    #             putInt(a+1);
    #         }

    #         if(true)
    #             if(true)
    #                 if(false)
    #                     if(true)
    #                         putInt(a);
    #                     else
    #                         putInt(a+1);
    #                 else
    #                     putInt(a+2);
    #             else
    #                 putInt(a+3);
    #         else
    #             putInt(a+4);
    #     }
	# 	"""
	# 	expect = "66111213678"
	# 	self.assertTrue(TestCodeGen.test(input,expect,546))

	# def test_if_47(self):

	# 	input = """
	# 	void main() {
    #         int a;
    #         a = 0;
    #         do
    #             a = a + 1;
    #             if (a==1) break;
    #         while(a < 10);
    #         putInt(a);
    #     }
	# 	"""
	# 	expect = "1"
	# 	self.assertTrue(TestCodeGen.test(input,expect,547))

	# def test_if_48(self):

	# 	input = """
	# 	void main()
	# 	{	
	# 		int a;
	# 		a=5;
	# 		if (a==1) putBool(true);
	# 		else 
	# 			if (a==2) putBool(false);
	# 		else putBool(true);
	# 	}
	# 	"""
	# 	expect = "true"
	# 	self.assertTrue(TestCodeGen.test(input,expect,548))

	# def test_if_49(self):

	# 	input = """

	# 	void main()
	# 	{
	# 		result=0;
	# 		for (i = 0; i < 10; i = i + 1)
    #             if (i == 5)
    #                 break;
    #             else
    #                 result = result + 1;
    #         putInt(result);
    #         putLn();
	# 	}

	# 	int result,i;
	# 	"""
	# 	expect = "5\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,549))

	# def test_for_50(self):

	# 	input = """
	# 	void main()
	# 	{
	# 		int n, i, flag;
	# 		flag=0;
	# 	    putStringLn("Enter a positive integer: ");
	# 	    n=13;
	# 	    for (i = 2; i <= n / 2; i=i+1) {
	# 	        if (n%  i== 0) {
	# 	            flag = 1;
	# 	            break;
	# 	        }
	# 	    }
	# 	    if (n == 1) {
	# 	        putStringLn("1 is neither prime nor composite.");
	# 	    }
	# 	    else {
	# 	        if (flag == 0)
	# 	        {
	# 	        	putInt(n);
	# 	            putStringLn(" is a prime number.");
	# 	        }
	# 	        else
	# 	        {
	# 	        	putInt(n);
	# 	            putStringLn(" is not a prime number.");
	# 	        }
	# 	    }		
	# 	}
	# 	"""
	# 	expect = "Enter a positive integer: \n13 is a prime number.\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,550))

	# def test_for_51(self):

	# 	input = """
	# 	void main() {
    #         int i,t;
    #         for (i = 0; i < 10; i = i + 1)
    #             putInt(i);
		   
    #         t = -10;
    #         for (1; t < 10; t = t + 2)
    #             putInt(i);
    #     }
	# 	"""
	# 	expect = "012345678910101010101010101010"
	# 	self.assertTrue(TestCodeGen.test(input,expect,551))

	# def test_for_52(self):

	# 	input = """
	# 	void main() {
    #         int i, j, result;
    #         result = 0;
    #         for (i = 0; i < 10; i = i + 1)
    #             for (j = 0; j < 10; j = j + 1)
    #                 result = result + 1;
    #         putInt(result);

    #         for (i = 0; i < 10; i = i + 1){
    #             result = result + 2;
    #         }
    #         putInt(result);

    #         int a[10];
    #         for (i = 0; i < 10; i = i + 1)
    #             putInt(a[i]);
    #         for (i = 0; i < 10; i = i + 1)
    #             a[i] = i;
    #         for (i = 0; i < 10; i = i + 1)
    #             putInt(a[i]);
    #         for (i = 0; i < 10; i = i + 1)
    #             result = result + a[i];
    #         putInt(result);
    #     }
	# 	"""
	# 	expect = "10012000000000000123456789165"
	# 	self.assertTrue(TestCodeGen.test(input,expect,552))

	# def test_for_53(self):

	# 	input = """
	# 	int a;

	# 	void testFor()
	# 	{
	# 		int i;
	# 		for(i=0;i<=10;i=i+1) a=a*2;
	# 		putIntLn(a);
	# 		int a;
	# 		for(a=9;true;a=a+1)
	# 		{
	# 			putIntLn(a);
	# 			if (a==20) break;
	# 		}
	# 	}

	# 	void main()
	# 	{
	# 		testFor();
	# 	}
	# 	"""
	# 	expect = "0\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,553))

	# def test_for_54(self):

	# 	input = """
	# 	int a;

	# 	void testFor()
	# 	{
	# 		int i;
	# 		for(i=0;i<=10;i=i+1) a=a*2;
	# 		putIntLn(a);
	# 		foo();
	# 	}

	# 	void main()
	# 	{
	# 		testFor();
	# 	}

	# 	void foo()
	# 	{
	# 		int a;
	# 		float f;
	# 		f=-1*2*3;
	# 		for(a=9;f<=11;a=a+1)
	# 		{
	# 			putIntLn(a);
	# 			f=f*-2;
	# 		}
	# 	}
	# 	"""
	# 	expect = "0\n9\n"
	# 	self.assertTrue(TestCodeGen.test(input,expect,554))

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

	def test_program_80(self):

		input = """
		void main()
		{
			int a;
			a = 0;
			a;
		}
		"""
		expect = ""
		self.assertTrue(TestCodeGen.test(input,expect,580))

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

