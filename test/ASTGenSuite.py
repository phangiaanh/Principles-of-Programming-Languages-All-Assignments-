import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):


#========================================TEST DECLARATIONS========================================
	def test_Decl_1(self):
		input = """int XXX, XXX[999];"""
		expect = str(Program([VarDecl("XXX",IntType()),VarDecl("XXX",ArrayType(999,IntType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,301))
	def test_Decl_2(self):
		input = """
				float XXX;
				string YYY[000];
				"""
		expect = str(Program([VarDecl("XXX",FloatType()),VarDecl("YYY",ArrayType(0,StringType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,302))
	def test_Decl_3(self):
		input = """
				boolean XXX,YYY,ZZZ;
				string UUU()
				{
					string XXX,YYY,ZZZ[999];
				}
				"""
		expect=str(Program([VarDecl("XXX",BoolType()),VarDecl("YYY",BoolType()),VarDecl("ZZZ",BoolType()),FuncDecl(Id("UUU"),[],StringType(),Block([VarDecl("XXX",StringType()),VarDecl("YYY",StringType()),VarDecl("ZZZ",ArrayType(999,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,303))
	def test_Decl_4(self):
		input = """float AAA,BBB[999],CCC,DDD[999],EEE,FFF[999];"""
		expect = str(Program([VarDecl("AAA",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("FFF",ArrayType(999,FloatType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,304))
	def test_Decl_5(self):
		input = """boolean AAA[999],BBB[000],CCC[999],DDD[000];"""
		expect = str(Program([VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(0,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(0,BoolType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,305))
	def test_Decl_6(self):
		input = """
				int AAA,BBB,CCC;
				float AAA[999],BBB[999],CCC,DDD,EEE;
				string AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				"""
		expect = str(Program([VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),VarDecl("CCC",IntType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("DDD",FloatType()),VarDecl("EEE",FloatType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,306))
	def test_Decl_7(self):
		input = """
				int AAA()
				{
		 			int AAA,BBB,CCC;
		 			float AAA[999],BBB[999],CCC,DDD,EEE;
		 			string AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect = str(Program([FuncDecl(Id("AAA"),[],IntType(),Block([VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),VarDecl("CCC",IntType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("DDD",FloatType()),VarDecl("EEE",FloatType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,307))
	def test_Decl_8(self):
		input = """
				float AAA(){
					int AAA,BBB,CCC;
		 			float AAA[999],BBB[999],CCC,DDD,EEE;
		 			string AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];

					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect = str(Program([FuncDecl(Id("AAA"),[],FloatType(),Block([VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),VarDecl("CCC",IntType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("DDD",FloatType()),VarDecl("EEE",FloatType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,308))
	def test_Decl_9(self):
		input = """
				float[] AAA()
				{
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect=str(Program([FuncDecl(Id("AAA"),[],ArrayPointerType(FloatType()),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,309))
	def test_Decl_10(self):
		input = """
				float AAA()
				{	
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect = str(Program([FuncDecl(Id("AAA"),[],FloatType(),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,310))
	def test_Decl_11(self):
		input = """
				boolean AAA()
				{	
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}	


				boolean[] AAA()
				{
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect = str(Program([FuncDecl(Id("AAA"),[],BoolType(),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))])),FuncDecl(Id("AAA"),[],ArrayPointerType(BoolType()),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,311))
	def test_Decl_12(self):
		input = """
				int AAA()
				{	
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}	


				void BBB()
				{
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}

				float CCC()
				{	
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}	


				string DDD()
				{
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect = str(Program([FuncDecl(Id("AAA"),[],IntType(),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))])),FuncDecl(Id("BBB"),[],VoidType(),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))])),FuncDecl(Id("CCC"),[],FloatType(),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))])),FuncDecl(Id("DDD"),[],StringType(),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,312))
	def test_Decl_13(self):
		input = """
				int[] AAA()
				{	
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}	


				float[] BBB()
				{
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}

				string[] CCC()
				{
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}

				boolean[] DDD()
				{	
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}	

				void EEE()
				{
					float AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			boolean AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect = str(Program([FuncDecl(Id("AAA"),[],ArrayPointerType(IntType()),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))])),FuncDecl(Id("BBB"),[],ArrayPointerType(FloatType()),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))])),FuncDecl(Id("CCC"),[],ArrayPointerType(StringType()),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))])),FuncDecl(Id("DDD"),[],ArrayPointerType(BoolType()),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))])),FuncDecl(Id("EEE"),[],VoidType(),Block([VarDecl("AAA",FloatType()),VarDecl("BBB",FloatType()),VarDecl("CCC",FloatType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,313))
	def test_Decl_14(self):
		input = """
				boolean[] BBB()
				{
					int AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			int AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
					int AAA,BBB,CCC;
		 			int AAA[999],BBB[999],CCC,DDD,EEE;
		 			int AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect = str(Program([FuncDecl(Id("BBB"),[],ArrayPointerType(BoolType()),Block([VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),VarDecl("CCC",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),VarDecl("CCC",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("DDD",IntType()),VarDecl("EEE",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,314))
	def test_Decl_15(self):
		input = """
				int AAA,BBB,CCC;
		 		boolean AAA[999],BBB[999],CCC,DDD,EEE;
		 		string AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
	 			float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				"""
		expect = str(Program([VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),VarDecl("CCC",IntType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("DDD",BoolType()),VarDecl("EEE",BoolType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,315))
	def test_Decl_16(self):
		input = """
	 			float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				"""
		expect = str(Program([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,316))
	def test_Decl_17(self):
		input = """
				int AAA(float BBB[], int AAA, string CCC[])
				{
				}
				"""
		expect = str(Program([FuncDecl(Id("AAA"),[VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("AAA",IntType()),VarDecl("CCC",ArrayPointerType(StringType()))],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,317))
	def test_Decl_18(self):
		input = """
				int[] AAA(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
				{
				}

				float[] BBB(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
				{
				}
				
				string[] CCC(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
				{
				}
				
				boolean[] DDD(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
				{
				}
				
				void EEE(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
				{
				}
				"""
		expect = str(Program([FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],ArrayPointerType(IntType()),Block([])),FuncDecl(Id("BBB"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],ArrayPointerType(FloatType()),Block([])),FuncDecl(Id("CCC"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],ArrayPointerType(StringType()),Block([])),FuncDecl(Id("DDD"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],ArrayPointerType(BoolType()),Block([])),FuncDecl(Id("EEE"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],VoidType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,318))
	def test_Decl_19(self):
		input = """
				int AAA(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect = str(Program([FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],IntType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,319))
	def test_Decl_20(self):
		input = """
				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];

				int AAA(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect = str(Program([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],IntType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,320))
	def test_Decl_21(self):
		input = """
				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];

				int AAA(int AAA[], float BBB[], string CCC[], boolean DDD[])
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect = str(Program([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),FuncDecl(Id("AAA"),[VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",ArrayPointerType(BoolType()))],IntType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,321))
	def test_Decl_22(self):
		input = """
				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 			float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				
				int[] AAA(int AAA[], float BBB[], string CCC[], boolean DDD[])
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}

				void AAA(int AAA, float BBB, string CCC, boolean DDD)
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect = str(Program([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),FuncDecl(Id("AAA"),[VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",ArrayPointerType(BoolType()))],ArrayPointerType(IntType()),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))])),FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("BBB",FloatType()),VarDecl("CCC",StringType()),VarDecl("DDD",BoolType())],VoidType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,322))
	def test_Decl_23(self):
		input = """
				boolean[] BBB()
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}

				string[] CCC(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
				{
				}
				"""
		expect = str(Program([FuncDecl(Id("BBB"),[],ArrayPointerType(BoolType()),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))])),FuncDecl(Id("CCC"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],ArrayPointerType(StringType()),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,323))
	def test_Decl_24(self):
		input = """
		int AAA,BBB,CCC;
		float AAA[999],BBB[999],CCC,DDD,EEE;
		string AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
		boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];

		int AAA(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
		{
			float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 		string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 		int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 		boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 		boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 		int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 		string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 		float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
		}
		"""
		expect = str(Program([VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),VarDecl("CCC",IntType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("DDD",FloatType()),VarDecl("EEE",FloatType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],IntType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,324))
	def test_Decl_25(self):
		input = """
				int AAA()
				{
					int AAA,BBB,CCC;
					float AAA[999],BBB[999],CCC,DDD,EEE;
					string AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
					boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect = str(Program([FuncDecl(Id("AAA"),[],IntType(),Block([VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),VarDecl("CCC",IntType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("DDD",FloatType()),VarDecl("EEE",FloatType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,325))
	def test_Decl_26(self):
		input = """
				void AAA()
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}

				void BBB()
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}

				void CCC()
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect=str(Program([FuncDecl(Id("AAA"),[],VoidType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))])),FuncDecl(Id("BBB"),[],VoidType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))])),FuncDecl(Id("CCC"),[],VoidType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,326))
	def test_Decl_27(self):
		input = """
				string AAA(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD)
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}

				int[] BBB(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD)
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect=str(Program([FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",BoolType())],StringType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))])),FuncDecl(Id("BBB"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",BoolType())],ArrayPointerType(IntType()),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,327))
	def test_Decl_28(self):
		input = """
				boolean AAA()
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}

				int AAA(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD)
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect=str(Program([FuncDecl(Id("AAA"),[],BoolType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))])),FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",BoolType())],IntType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,328))
	def test_Decl_29(self):
		input = """
				float[] BBB(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD)
				{
				}

				int CCC(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD)
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect=str(Program([FuncDecl(Id("BBB"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",BoolType())],ArrayPointerType(FloatType()),Block([])),FuncDecl(Id("CCC"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",BoolType())],IntType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,329))
	def test_Decl_30(self):
		input = """
				string AAA(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD)
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				boolean[] AAA(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD)
				{
				}
				float[] AAA(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD)
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				void AAA(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD)
				{
				}

				int BBB()
				{
					int AAA,BBB,CCC;
					float AAA[999],BBB[999],CCC,DDD,EEE;
					string AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
					boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect=str(Program([FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",BoolType())],StringType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))])),FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",BoolType())],ArrayPointerType(BoolType()),Block([])),FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",BoolType())],ArrayPointerType(FloatType()),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))])),FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",BoolType())],VoidType(),Block([])),FuncDecl(Id("BBB"),[],IntType(),Block([VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),VarDecl("CCC",IntType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("DDD",FloatType()),VarDecl("EEE",FloatType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,330))
	def test_Decl_31(self):
		input = """
				int[] AAA(int AAA, float BBB, string CCC, boolean DDD)
				{
					int AAA,BBB,CCC;
					float AAA[999],BBB[999],CCC,DDD,EEE;
					string AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
					boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];

				}
				"""
		expect=str(Program([FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("BBB",FloatType()),VarDecl("CCC",StringType()),VarDecl("DDD",BoolType())],ArrayPointerType(IntType()),Block([VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),VarDecl("CCC",IntType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("DDD",FloatType()),VarDecl("EEE",FloatType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,331))
	def test_Decl_32(self):
		input = """
				int AAA(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
				{
					int AAA,BBB,CCC;
					float AAA[999],BBB[999],CCC,DDD,EEE;
					string AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
					boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}

				void AAA(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
				{
					int AAA,BBB,CCC;
					float AAA[999],BBB[999],CCC,DDD,EEE;
					string AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
					boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect=str(Program([FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],IntType(),Block([VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),VarDecl("CCC",IntType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("DDD",FloatType()),VarDecl("EEE",FloatType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType()))])),FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],VoidType(),Block([VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),VarDecl("CCC",IntType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("DDD",FloatType()),VarDecl("EEE",FloatType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,332))
	def test_Decl_33(self):
		input = """
				int[] AAA(int AAA, float BBB, string CCC, boolean DDD)
				{
					
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect=str(Program([FuncDecl(Id("AAA"),[VarDecl("AAA",IntType()),VarDecl("BBB",FloatType()),VarDecl("CCC",StringType()),VarDecl("DDD",BoolType())],ArrayPointerType(IntType()),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,333))
	def test_Decl_34(self):
		input = """
				boolean AAA(boolean AAA, boolean AAA[], boolean BBB, boolean BBB[], boolean CCC, boolean CCC[], boolean DDD, boolean DDD[])
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}

				boolean[] BBB(boolean BBB[])
				{
				}
				"""
		expect=str(Program([FuncDecl(Id("AAA"),[VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayPointerType(BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayPointerType(BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayPointerType(BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],BoolType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))])),FuncDecl(Id("BBB"),[VarDecl("BBB",ArrayPointerType(BoolType()))],ArrayPointerType(BoolType()),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,334))
	def test_Decl_35(self):
		input = """
				string CCC(string AAA, string BBB, string CCC[], string DDD[])
				{
					string AAA,BBB,CCC;
					string AAA[999],BBB[999],CCC,DDD,EEE;
					string AAA[999],BBB[999],CCC[999],DDD[999],EEE[999];
					string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}

				string[] DDD()
				{
				}
				"""
		expect=str(Program([FuncDecl(Id("CCC"),[VarDecl("AAA",StringType()),VarDecl("BBB",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",ArrayPointerType(StringType()))],StringType(),Block([VarDecl("AAA",StringType()),VarDecl("BBB",StringType()),VarDecl("CCC",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("DDD",StringType()),VarDecl("EEE",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType()))])),FuncDecl(Id("DDD"),[],ArrayPointerType(StringType()),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,335))
	def test_Decl_36(self):
		input = """
				float DDD(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect=str(Program([FuncDecl(Id("DDD"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],FloatType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,336))
	def test_Decl_37(self):
		input = """
				void AAA()
				{
				}

				void BBB(int AAA, float BBB, string CCC, boolean DDD)
				{
				}

				void CCC(int AAA, int AAA[], float BBB, float BBB[], string CCC, string CCC[], boolean DDD, boolean DDD[])
				{
					float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				boolean AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				int AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				string AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
	 				float AAA,AAA[999],BBB,BBB[999],CCC,CCC[999],DDD,DDD[999],EEE,EEE[999];
				}
				"""
		expect=str(Program([FuncDecl(Id("AAA"),[],VoidType(),Block([])),FuncDecl(Id("BBB"),[VarDecl("AAA",IntType()),VarDecl("BBB",FloatType()),VarDecl("CCC",StringType()),VarDecl("DDD",BoolType())],VoidType(),Block([])),FuncDecl(Id("CCC"),[VarDecl("AAA",IntType()),VarDecl("AAA",ArrayPointerType(IntType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayPointerType(FloatType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayPointerType(StringType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayPointerType(BoolType()))],VoidType(),Block([VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),VarDecl("BBB",BoolType()),VarDecl("BBB",ArrayType(999,BoolType())),VarDecl("CCC",BoolType()),VarDecl("CCC",ArrayType(999,BoolType())),VarDecl("DDD",BoolType()),VarDecl("DDD",ArrayType(999,BoolType())),VarDecl("EEE",BoolType()),VarDecl("EEE",ArrayType(999,BoolType())),VarDecl("AAA",IntType()),VarDecl("AAA",ArrayType(999,IntType())),VarDecl("BBB",IntType()),VarDecl("BBB",ArrayType(999,IntType())),VarDecl("CCC",IntType()),VarDecl("CCC",ArrayType(999,IntType())),VarDecl("DDD",IntType()),VarDecl("DDD",ArrayType(999,IntType())),VarDecl("EEE",IntType()),VarDecl("EEE",ArrayType(999,IntType())),VarDecl("AAA",StringType()),VarDecl("AAA",ArrayType(999,StringType())),VarDecl("BBB",StringType()),VarDecl("BBB",ArrayType(999,StringType())),VarDecl("CCC",StringType()),VarDecl("CCC",ArrayType(999,StringType())),VarDecl("DDD",StringType()),VarDecl("DDD",ArrayType(999,StringType())),VarDecl("EEE",StringType()),VarDecl("EEE",ArrayType(999,StringType())),VarDecl("AAA",FloatType()),VarDecl("AAA",ArrayType(999,FloatType())),VarDecl("BBB",FloatType()),VarDecl("BBB",ArrayType(999,FloatType())),VarDecl("CCC",FloatType()),VarDecl("CCC",ArrayType(999,FloatType())),VarDecl("DDD",FloatType()),VarDecl("DDD",ArrayType(999,FloatType())),VarDecl("EEE",FloatType()),VarDecl("EEE",ArrayType(999,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,337))
#=================================================================================================



#========================================TEST STATEMENTS========================================
	def test_Stmt_1(self):
		input = """
				boolean AAA, AAA[999];
                string BBB(int BBB, boolean BBB[]){
                    {
                        {}
                    }
                }
                float DDD(){}
                int EEE;
				"""
		expect=str(Program([VarDecl("AAA",BoolType()),VarDecl("AAA",ArrayType(999,BoolType())),FuncDecl(Id("BBB"),[VarDecl("BBB",IntType()),VarDecl("BBB",ArrayPointerType(BoolType()))],StringType(),Block([Block([Block([])])])),FuncDecl(Id("DDD"),[],FloatType(),Block([])),VarDecl("EEE",IntType())]))
		self.assertTrue(TestAST.checkASTGen(input,expect,338))
	def test_Stmt_2(self):
		input = """
				boolean AAA;
                boolean BBB(int CCC){
                    int DDD, DDD;
                    DDD = EEE;
                    EEE = DDD;
                    {}
                }
				"""
		expect=str(Program([VarDecl("AAA",BoolType()),FuncDecl(Id("BBB"),[VarDecl("CCC",IntType())],BoolType(),Block([VarDecl("DDD",IntType()),VarDecl("DDD",IntType()),BinaryOp("=",Id("DDD"),Id("EEE")),BinaryOp("=",Id("EEE"),Id("DDD")),Block([])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,339))
	def test_Stmt_3(self):
		input = """
				int AAA, BBB;
                boolean[] BBB(float DDD[]){
                    DDD("AAA");
                    return;
                }
				"""
		expect=str(Program([VarDecl("AAA",IntType()),VarDecl("BBB",IntType()),FuncDecl(Id("BBB"),[VarDecl("DDD",ArrayPointerType(FloatType()))],ArrayPointerType(BoolType()),Block([CallExpr(Id("DDD"),[StringLiteral("AAA")]),Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,340))
	def test_Stmt_4(self):
		input = """
				void AAA(int BBB){
                    if(AAA == 0) 
                        BBB("CCC");
                    else
                        BBB("BBB");
                    return;
                }
				"""
		expect=str(Program([FuncDecl(Id("AAA"),[VarDecl("BBB",IntType())],VoidType(),Block([If(BinaryOp("==",Id("AAA"),IntLiteral(0)),CallExpr(Id("BBB"),[StringLiteral("CCC")]),CallExpr(Id("BBB"),[StringLiteral("BBB")])),Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,341))
	def test_Stmt_5(self):
		input = """
				float[] amIEmpty(int a){
                    if(smile) 
                        difficult = difficult / 2;
                    else
                        difficult = difficult * 2;
                    return Hollow;
                }
				"""
		expect=str(Program([FuncDecl(Id("amIEmpty"),[VarDecl("a",IntType())],ArrayPointerType(FloatType()),Block([If(Id("smile"),BinaryOp("=",Id("difficult"),BinaryOp("/",Id("difficult"),IntLiteral(2))),BinaryOp("=",Id("difficult"),BinaryOp("*",Id("difficult"),IntLiteral(2)))),Return(Id("Hollow"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,342))
	def test_Stmt_6(self):
		input = """
				void amIEmpty(int a){
                    if(falling)
                        Flying();
                    int var;
                    float var[3];
                }
				"""
		expect=str(Program([FuncDecl(Id("amIEmpty"),[VarDecl("a",IntType())],VoidType(),Block([If(Id("falling"),CallExpr(Id("Flying"),[])),VarDecl("var",IntType()),VarDecl("var",ArrayType(3,FloatType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,343))
	def test_Stmt_7(self):
		input = """
				string[] moreThanICanSay(string toYou){
                    printf("I love you!");
                }
                float[] countNumbers(){}
                int var, var1, var2[999];
                boolean var[999], bool[0];
				"""
		expect=str(Program([FuncDecl(Id("moreThanICanSay"),[VarDecl("toYou",StringType())],ArrayPointerType(StringType()),Block([CallExpr(Id("printf"),[StringLiteral("I love you!")])])),FuncDecl(Id("countNumbers"),[],ArrayPointerType(FloatType()),Block([])),VarDecl("var",IntType()),VarDecl("var1",IntType()),VarDecl("var2",ArrayType(999,IntType())),VarDecl("var",ArrayType(999,BoolType())),VarDecl("bool",ArrayType(0,BoolType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,344))
	def test_Stmt_8(self):
		input = """
				void main(){
                    if((life == difficult) || (feeling == depression)){
                        hug = 3000;
                        You = Someone(hug);
                    }
                    else
                        printf("Have a good day!");
                }
				"""
		expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("||",BinaryOp("==",Id("life"),Id("difficult")),BinaryOp("==",Id("feeling"),Id("depression"))),Block([BinaryOp("=",Id("hug"),IntLiteral(3000)),BinaryOp("=",Id("You"),CallExpr(Id("Someone"),[Id("hug")]))]),CallExpr(Id("printf"),[StringLiteral("Have a good day!")]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,345))
	def test_Stmt_9(self):
		input = """ 
				void main(){
                    if((life == difficult) || (feeling == depression))
                        if(beHumble())
                            if(beKind())
                                if(bePositive())
                                    believeInTheFuture(you);
                    else
                        printf("Have a good day!");
                }
				"""
		expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("||",BinaryOp("==",Id("life"),Id("difficult")),BinaryOp("==",Id("feeling"),Id("depression"))),If(CallExpr(Id("beHumble"),[]),If(CallExpr(Id("beKind"),[]),If(CallExpr(Id("bePositive"),[]),CallExpr(Id("believeInTheFuture"),[Id("you")]),CallExpr(Id("printf"),[StringLiteral("Have a good day!")])))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,346))
	def test_Stmt_10(self):
		input = """
				void main(){
                    if(goDown(floor4))
                        if(goDown(floor3))
                            if(goDown(floor2))
                                if(goDown(floor1))
                                    if(goDown(basement))
                                        printf("Hello Annabelle!");
                                    else
                                        goUp();
                                else
                                    goUp();
                            else
                                goUp();
                        else
                            printf("You shouldn't go to the basement :)))");
                }
				"""
		expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(CallExpr(Id("goDown"),[Id("floor4")]),If(CallExpr(Id("goDown"),[Id("floor3")]),If(CallExpr(Id("goDown"),[Id("floor2")]),If(CallExpr(Id("goDown"),[Id("floor1")]),If(CallExpr(Id("goDown"),[Id("basement")]),CallExpr(Id("printf"),[StringLiteral("Hello Annabelle!")]),CallExpr(Id("goUp"),[])),CallExpr(Id("goUp"),[])),CallExpr(Id("goUp"),[])),CallExpr(Id("printf"),[StringLiteral("You shouldn't go to the basement :)))")])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,347))
	def test_Stmt_11(self):
		input = """
				void main(){
                    letMakeAStair(true);
                    if(stair){
                        //do nothing
                    }
                    else
                        if(stair){
                            //do nothing}}}}}}
                        }
                        else
                            if(stair){
                                {// do nothing}
                            }}
                            else{
                                {// do nothing}
                }}}
				"""
		expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("letMakeAStair"),[BooleanLiteral(True)]),If(Id("stair"),Block([]),If(Id("stair"),Block([]),If(Id("stair"),Block([Block([])]),Block([Block([])]))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,348))
	def test_Stmt_12(self):
		input = """
				void main(){
                    chanceOfMeetingYourFutureWife = 0;
                    if(meetSomeone(aGirl)){
                        {
                            {
                                shy(you);
                                runAway(you);
                            }
                        }
                        she = smile("looking at you");
                    }
                    if(meetSomeone(aGirl)){
                        beStrong = true;
                        chanceOfMeetingYourFutureWife = 1;
                    }
                }
				"""
		expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("chanceOfMeetingYourFutureWife"),IntLiteral(0)),If(CallExpr(Id("meetSomeone"),[Id("aGirl")]),Block([Block([Block([CallExpr(Id("shy"),[Id("you")]),CallExpr(Id("runAway"),[Id("you")])])]),BinaryOp("=",Id("she"),CallExpr(Id("smile"),[StringLiteral("looking at you")]))])),If(CallExpr(Id("meetSomeone"),[Id("aGirl")]),Block([BinaryOp("=",Id("beStrong"),BooleanLiteral(True)),BinaryOp("=",Id("chanceOfMeetingYourFutureWife"),IntLiteral(1))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,349))
	def test_Stmt_13(self):
		input = """
				void main(){
                    if(believe == true)
                        stronger = yes;
                        if(kind == true)
                            better = yes;
                            if(fear == no)
                                success = yes;
                    else{
                        cout("Keep fighting!");
                    }
                }
				"""
		expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",Id("believe"),BooleanLiteral(True)),BinaryOp("=",Id("stronger"),Id("yes"))),If(BinaryOp("==",Id("kind"),BooleanLiteral(True)),BinaryOp("=",Id("better"),Id("yes"))),If(BinaryOp("==",Id("fear"),Id("no")),BinaryOp("=",Id("success"),Id("yes")),Block([CallExpr(Id("cout"),[StringLiteral("Keep fighting!")])]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,350))
	def test_Stmt_14(self):
		input = """
				void main(){
                    if(1)
                        if(2)
                            if(3)
                                if(4)
                                    if(5)
                    stopSayingIf();
                    action(true);
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(IntLiteral(1),If(IntLiteral(2),If(IntLiteral(3),If(IntLiteral(4),If(IntLiteral(5),CallExpr(Id("stopSayingIf"),[])))))),CallExpr(Id("action"),[BooleanLiteral(True)])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,351))
	def test_Stmt_15(self):
		input = """
				float main(){
                    if(sky)
                        if(sea){}
                    else{earth;}
                    else{rain;}
                    if(light){}
                    else{dark;}
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],FloatType(),Block([If(Id("sky"),If(Id("sea"),Block([]),Block([Id("earth")])),Block([Id("rain")])),If(Id("light"),Block([]),Block([Id("dark")]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,352))
	def test_Stmt_16(self):
		input = """
				void main(){
                    do{
                        {
                            printf("Easy testcase");
                        }
                    }
                    while(busy == false);

                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([Block([CallExpr(Id("printf"),[StringLiteral("Easy testcase")])])])],BinaryOp("==",Id("busy"),BooleanLiteral(False)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,353))
	def test_Stmt_17(self):
		input = """
				void main(){
                    do{
                        {
                            printf("Easy testcase");
                        }
                    }
                    while(busy == false);
                    int shitHappens;
                    guessWhatWrongInThisTestcase(viewer);
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([Block([CallExpr(Id("printf"),[StringLiteral("Easy testcase")])])])],BinaryOp("==",Id("busy"),BooleanLiteral(False))),VarDecl("shitHappens",IntType()),CallExpr(Id("guessWhatWrongInThisTestcase"),[Id("viewer")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,354))
	def test_Stmt_18(self):
		input = """
				void main(){
                    int bePatient;
                    do
                    bePatient = 0;
                    bePatient = 1;
                    bePatient = 2;
                    if(bePatient > 3)
                        dontBePatientAnymore(":)");
                    while(mood < usualState);
                    do number1 + number2;
                    while(number1 > number2);
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("bePatient",IntType()),Dowhile([BinaryOp("=",Id("bePatient"),IntLiteral(0)),BinaryOp("=",Id("bePatient"),IntLiteral(1)),BinaryOp("=",Id("bePatient"),IntLiteral(2)),If(BinaryOp(">",Id("bePatient"),IntLiteral(3)),CallExpr(Id("dontBePatientAnymore"),[StringLiteral(":)")]))],BinaryOp("<",Id("mood"),Id("usualState"))),Dowhile([BinaryOp("+",Id("number1"),Id("number2"))],BinaryOp(">",Id("number1"),Id("number2")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,355))
	def test_Stmt_19(self):
		input = """
				void main(){
                    do
                        do
                            do
                                do
                                    tooManyDos("stop");
                                while(free);
                            while(free);
                        while(notFree);
                    while(busy == false);
				}
				"""
		expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Dowhile([Dowhile([Dowhile([CallExpr(Id("tooManyDos"),[StringLiteral("stop")])],Id("free"))],Id("free"))],Id("notFree"))],BinaryOp("==",Id("busy"),BooleanLiteral(False)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,356))
	def test_Stmt_20(self):
		input = """
				void main(){
                    do{
                        sitDown;
                        beHumble;
                    }while(living);
                    WhiLe(feeling);
                    WhiLe(breathing);
                    WhIle(youStillCan);
                }
				"""		
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([Id("sitDown"),Id("beHumble")])],Id("living")),CallExpr(Id("WhiLe"),[Id("feeling")]),CallExpr(Id("WhiLe"),[Id("breathing")]),CallExpr(Id("WhIle"),[Id("youStillCan")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,357))
	def test_Stmt_21(self):
		input = """
				void main(){
                    do{
                        anythingYouWant();
                        butNotIllegal();
                    }
                    whiLe(doingSomething);
                    becomeABetterPerson = 1;
                    while(enjoyLife);
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([CallExpr(Id("anythingYouWant"),[]),CallExpr(Id("butNotIllegal"),[])]),CallExpr(Id("whiLe"),[Id("doingSomething")]),BinaryOp("=",Id("becomeABetterPerson"),IntLiteral(1))],Id("enjoyLife"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,358))
	def test_Stmt_22(self):
		input = """
				void main(){
                    do
                        do
                            do
                                do
                                    DO;
                                while(youStillCan);
                            while(youStillCan);
                        while(youStillCan);
                    while(youStillCan);
                }
				"""
		expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Dowhile([Dowhile([Dowhile([Id("DO")],Id("youStillCan"))],Id("youStillCan"))],Id("youStillCan"))],Id("youStillCan"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,359))
	def test_Stmt_23(self):
		input = """
				void main(){
                    int i;
                    for(i = 3; i < infinity; i = i + 1)
                        do
                            statement1;
                            statement2;
                            statement3;
                        while(somethingThatIsTrue);
                    int endline;
                    string line;
                }
				"""
		expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(3)),BinaryOp("<",Id("i"),Id("infinity")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Dowhile([Id("statement1"),Id("statement2"),Id("statement3")],Id("somethingThatIsTrue"))),VarDecl("endline",IntType()),VarDecl("line",StringType())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,360))
	def test_Stmt_24(self):
		input = """
				void main(){
                    int i;
                    for(a;a;a)
                        feelingEmpty = true;
                    int endline;
                    string line;
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),For(Id("a"),Id("a"),Id("a"),BinaryOp("=",Id("feelingEmpty"),BooleanLiteral(True))),VarDecl("endline",IntType()),VarDecl("line",StringType())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,361))
	def test_Stmt_25(self):
		input = """
				void main(){
                    int i;
                    for(i = 3; i < infinity; i = i + 1){
                        for(something; something; something){
                            {//do nothing
                        }}
                    }
                    break;
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(3)),BinaryOp("<",Id("i"),Id("infinity")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(Id("something"),Id("something"),Id("something"),Block([Block([])]))])),Break()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,362))
	def test_Stmt_26(self):
		input = """
				void main(){
                    int i;
                    for(i = 3; i < infinity; i = i + 1)
                        if(shitHappens)
                            whoCares();
                    for(exp; exp; exp){
                        {
                            stillWhoCares();
                        }
                    }
                    {
                        nowThisIsFun();
                    }
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(3)),BinaryOp("<",Id("i"),Id("infinity")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(Id("shitHappens"),CallExpr(Id("whoCares"),[]))),For(Id("exp"),Id("exp"),Id("exp"),Block([Block([CallExpr(Id("stillWhoCares"),[])])])),Block([CallExpr(Id("nowThisIsFun"),[])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,363))
	def test_Stmt_27(self):
		input = """
				void main(){
                    int i;
                    for(i = 3; i < infinity; i = i + 1)
                        continue;
                        return (Continue + Break);
                    break;
                    for(something; something; something)
                        do{}
                        while(something);
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(3)),BinaryOp("<",Id("i"),Id("infinity")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Continue()),Return(BinaryOp("+",Id("Continue"),Id("Break"))),Break(),For(Id("something"),Id("something"),Id("something"),Dowhile([Block([])],Id("something")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,364))
	def test_Stmt_28(self):
		input = """
				void main(){
                    for(something;something;something)
                        if(thatMakesYouHappy){}
                        else{
                            print("dontDoThat");
                        }
                    for(something;something;something){
                        a = 3;
                        a = a * 3 + 4;
                    }
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(Id("something"),Id("something"),Id("something"),If(Id("thatMakesYouHappy"),Block([]),Block([CallExpr(Id("print"),[StringLiteral("dontDoThat")])]))),For(Id("something"),Id("something"),Id("something"),Block([BinaryOp("=",Id("a"),IntLiteral(3)),BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("*",Id("a"),IntLiteral(3)),IntLiteral(4)))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,365))
	def test_Stmt_29(self):
		input = """
				void main(){
                    int i,j;
                    i = j = 0;
                    for( i = 0; i <= j; i = i + 1){
                        {
                            {
                                // do nothing
                            }
                            var = arr[3];
                        }
                    }
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),VarDecl("j",IntType()),BinaryOp("=",Id("i"),BinaryOp("=",Id("j"),IntLiteral(0))),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),Id("j")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Block([Block([]),BinaryOp("=",Id("var"),ArrayCell(Id("arr"),IntLiteral(3)))])]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,366))
	def test_Stmt_30(self):
		input = """
				void main(){
                    for(life = sea; you = fish; living = swimming){
                        if(fish(sea) != swimming)
                            sea = false;
                        else
                            swimming = swimming + 1;
                    }
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("life"),Id("sea")),BinaryOp("=",Id("you"),Id("fish")),BinaryOp("=",Id("living"),Id("swimming")),Block([If(BinaryOp("!=",CallExpr(Id("fish"),[Id("sea")]),Id("swimming")),BinaryOp("=",Id("sea"),BooleanLiteral(False)),BinaryOp("=",Id("swimming"),BinaryOp("+",Id("swimming"),IntLiteral(1))))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,367))
	def test_Stmt_31(self):
		input = """
				void main(){
                    int i;
                    if(willIBeBetter)
                        return nothing;
                    break;
                }
				"""
		expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),If(Id("willIBeBetter"),Return(Id("nothing"))),Break()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,368))
	def test_Stmt_32(self):
		input = """
				void main(){
                    funcall(a, a + 1);
                    if(PPL)
                        return "Runnnnnnnnnn";
                    else
                        return;
                    return "Still runnnnnnn";
                }
				"""
		expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("funcall"),[Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))]),If(Id("PPL"),Return(StringLiteral("Runnnnnnnnnn")),Return()),Return(StringLiteral("Still runnnnnnn"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,369))
	def test_Stmt_33(self):
		input = """
				void main(){
                    do
                        do
                            do
                                continue;
                            while("...Yeah no need to check here...");
                            while("...Yeah no need to check here...");
                            while("...Yeah no need to check here...");
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Dowhile([Dowhile([Continue()],StringLiteral("...Yeah no need to check here..."))],StringLiteral("...Yeah no need to check here..."))],StringLiteral("...Yeah no need to check here..."))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,370))
	def test_Stmt_34(self):
		input = """
				void main(){
                    for(test; all; statements)
                        if(thisTestcase == true)
                            do
                                "Yeah you nailed the statements";
                                break;
                                return true;
                                continue;
                            while(stillRunning());
                    printf("Congrats!");
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(Id("test"),Id("all"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue()],CallExpr(Id("stillRunning"),[])))),CallExpr(Id("printf"),[StringLiteral("Congrats!")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,371))
	def test_Stmt_35(self):
		input = """
				void main(){
                    "So this is nearly the last testcase of this section!";
                    for(test; all; statements)
                        for(test; all_again; statements)
                            if(thisTestcase == true)
                            do
                                "Yeah you nailed the statements";
                                break;
                                return true;
                                continue;
                                do
                                    statement1;
                                    statement2;
                                    statement3;
                                while(stillRunning);
                            while(stillRunning());
                            else{
                                if(yeahHopeYouPassedThis[3000]){
                                    do
                                        maybeThisIsEnough;
                                    while(goodLuck);
                                }
                            }

                    printf("Congrats!");
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([StringLiteral("So this is nearly the last testcase of this section!"),For(Id("test"),Id("all"),Id("statements"),For(Id("test"),Id("all_again"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue(),Dowhile([Id("statement1"),Id("statement2"),Id("statement3")],Id("stillRunning"))],CallExpr(Id("stillRunning"),[])),Block([If(ArrayCell(Id("yeahHopeYouPassedThis"),IntLiteral(3000)),Block([Dowhile([Id("maybeThisIsEnough")],Id("goodLuck"))]))])))),CallExpr(Id("printf"),[StringLiteral("Congrats!")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,372))
	def test_Stmt_36(self):
		input = """
				void main(){
                    "So this is the last testcase of this section! Good luck!";
                    for(test; all; statements)
                        for(test; all_again; statements)
                            if(thisTestcase == true)
                            do
                                "Yeah you nailed the statements";
                                break;
                                return true;
                                continue;
                                do
                                    statement1;
                                    if(youCanPassedThis)
                                        yourStatement = good;
                                    else
                                        needToCheck();
                                while(stillRunning);
                            while(stillRunning());
                            else{
                                if(yeahHopeYouPassedThis[3000]){
                                    do
                                        do
                                            do
                                                for(1;2;3){
                                                    what = doesnot;
                                                    kill = you;
                                                    makes = youStronger;
                                                }
                                                passed = stronger;
                                            while(thisIsGoingToEnd);
                                        while(butThereAreStillManyToCome());
                                    while(goodLuck);
                                }
                            }

                    printf("Congrats!");
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([StringLiteral("So this is the last testcase of this section! Good luck!"),For(Id("test"),Id("all"),Id("statements"),For(Id("test"),Id("all_again"),Id("statements"),If(BinaryOp("==",Id("thisTestcase"),BooleanLiteral(True)),Dowhile([StringLiteral("Yeah you nailed the statements"),Break(),Return(BooleanLiteral(True)),Continue(),Dowhile([Id("statement1"),If(Id("youCanPassedThis"),BinaryOp("=",Id("yourStatement"),Id("good")),CallExpr(Id("needToCheck"),[]))],Id("stillRunning"))],CallExpr(Id("stillRunning"),[])),Block([If(ArrayCell(Id("yeahHopeYouPassedThis"),IntLiteral(3000)),Block([Dowhile([Dowhile([Dowhile([For(IntLiteral(1),IntLiteral(2),IntLiteral(3),Block([BinaryOp("=",Id("what"),Id("doesnot")),BinaryOp("=",Id("kill"),Id("you")),BinaryOp("=",Id("makes"),Id("youStronger"))])),BinaryOp("=",Id("passed"),Id("stronger"))],Id("thisIsGoingToEnd"))],CallExpr(Id("butThereAreStillManyToCome"),[]))],Id("goodLuck"))]))])))),CallExpr(Id("printf"),[StringLiteral("Congrats!")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,373))
#===============================================================================================



#========================================TEST EXPRESSIONS========================================
	def test_Expr_1(self):
		input = """
				void main(){
                    a = foo(a) + c -2*a;
                    array[3] = foo(array[2] *3) + 34;
                    for(a/b; b%c; c||d)
                        foo(a+b, a-b, arr[3000]);
                }
				"""
		expect=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("+",CallExpr(Id("foo"),[Id("a")]),Id("c")),BinaryOp("*",IntLiteral(2),Id("a")))),BinaryOp("=",ArrayCell(Id("array"),IntLiteral(3)),BinaryOp("+",CallExpr(Id("foo"),[BinaryOp("*",ArrayCell(Id("array"),IntLiteral(2)),IntLiteral(3))]),IntLiteral(34))),For(BinaryOp("/",Id("a"),Id("b")),BinaryOp("%",Id("b"),Id("c")),BinaryOp("||",Id("c"),Id("d")),CallExpr(Id("foo"),[BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("a"),Id("b")),ArrayCell(Id("arr"),IntLiteral(3000))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,374))
	def test_Expr_2(self):
		input = """
				void main(){
                    if(a < b && b >= c && c > d)
                        doThis();
                    else
                        doThat();
                    exp = a < b == c ;
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",BinaryOp("&&",BinaryOp("<",Id("a"),Id("b")),BinaryOp(">=",Id("b"),Id("c"))),BinaryOp(">",Id("c"),Id("d"))),CallExpr(Id("doThis"),[]),CallExpr(Id("doThat"),[])),BinaryOp("=",Id("exp"),BinaryOp("==",BinaryOp("<",Id("a"),Id("b")),Id("c")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,375))
	def test_Expr_3(self):
		input = """
				void main(){
                    for(a < b + c; a >= b; c[3] + 5){
                        a = b != c <= d;
                    }    
                    do
                        makeThis(a*b*c*d/d%e);
                        makeThat(arr[arr[arr[3]]]);
                    while(true);
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("<",Id("a"),BinaryOp("+",Id("b"),Id("c"))),BinaryOp(">=",Id("a"),Id("b")),BinaryOp("+",ArrayCell(Id("c"),IntLiteral(3)),IntLiteral(5)),Block([BinaryOp("=",Id("a"),BinaryOp("!=",Id("b"),BinaryOp("<=",Id("c"),Id("d"))))])),Dowhile([CallExpr(Id("makeThis"),[BinaryOp("%",BinaryOp("/",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("a"),Id("b")),Id("c")),Id("d")),Id("d")),Id("e"))]),CallExpr(Id("makeThat"),[ArrayCell(Id("arr"),ArrayCell(Id("arr"),ArrayCell(Id("arr"),IntLiteral(3))))])],BooleanLiteral(True))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,376))
	def test_Expr_4(self):
		input = """
				void main(){
                    for(-3; -arr[4]; !(arr[3] + b)){
                        a = b = c + d;
                        a != (arr[3] + foo(4));
                    }
                    b = arr && arr = (arr[4] + foo())[3];
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(UnaryOp("-",IntLiteral(3)),UnaryOp("-",ArrayCell(Id("arr"),IntLiteral(4))),UnaryOp("!",BinaryOp("+",ArrayCell(Id("arr"),IntLiteral(3)),Id("b"))),Block([BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("+",Id("c"),Id("d")))),BinaryOp("!=",Id("a"),BinaryOp("+",ArrayCell(Id("arr"),IntLiteral(3)),CallExpr(Id("foo"),[IntLiteral(4)])))])),BinaryOp("=",Id("b"),BinaryOp("=",BinaryOp("&&",Id("arr"),Id("arr")),ArrayCell(BinaryOp("+",ArrayCell(Id("arr"),IntLiteral(4)),CallExpr(Id("foo"),[])),IntLiteral(3))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,377))
	def test_Expr_5(self):
		input = """
				void main(){
                    funcall(a, a + 1);
                    a = funcall(funcall(a[funcall(a[funcall()])]));
                    !a = (ABC + AB[5])*3;
                    return 0;
                }
                int main;	
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("funcall"),[Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))]),BinaryOp("=",Id("a"),CallExpr(Id("funcall"),[CallExpr(Id("funcall"),[ArrayCell(Id("a"),CallExpr(Id("funcall"),[ArrayCell(Id("a"),CallExpr(Id("funcall"),[]))]))])])),BinaryOp("=",UnaryOp("!",Id("a")),BinaryOp("*",BinaryOp("+",Id("ABC"),ArrayCell(Id("AB"),IntLiteral(5))),IntLiteral(3))),Return(IntLiteral(0))])),VarDecl("main",IntType())]))
		self.assertTrue(TestAST.checkASTGen(input,expect,378))
	def test_Expr_6(self):
		input = """
				void main(){
                    {/*
                        This happens inside the scope!
                    }*/
                    if(ABC[ABC[5]]){
                        thereIsSomethingWrong(l3ookup);
                    }
                }}
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Block([If(ArrayCell(Id("ABC"),ArrayCell(Id("ABC"),IntLiteral(5))),Block([CallExpr(Id("thereIsSomethingWrong"),[Id("l3ookup")])]))])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,379))
	def test_Expr_7(self):
		input = """
				void main(){
                    for(foo(a[3]); !fap(a+b,a*b[3+2*6[3]]); i = i + 3.3e-12)
                        do
                            A = A(((((3)))));
                            B = (3.e-2+0.e3)[(4.5+2)[abc]];
                        while(A || B && C || D && E == F);
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(CallExpr(Id("foo"),[ArrayCell(Id("a"),IntLiteral(3))]),UnaryOp("!",CallExpr(Id("fap"),[BinaryOp("+",Id("a"),Id("b")),BinaryOp("*",Id("a"),ArrayCell(Id("b"),BinaryOp("+",IntLiteral(3),BinaryOp("*",IntLiteral(2),ArrayCell(IntLiteral(6),IntLiteral(3))))))])),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),FloatLiteral(3.3e-12))),Dowhile([BinaryOp("=",Id("A"),CallExpr(Id("A"),[IntLiteral(3)])),BinaryOp("=",Id("B"),ArrayCell(BinaryOp("+",FloatLiteral(0.03),FloatLiteral(0.0)),ArrayCell(BinaryOp("+",FloatLiteral(4.5),IntLiteral(2)),Id("abc"))))],BinaryOp("||",BinaryOp("||",Id("A"),BinaryOp("&&",Id("B"),Id("C"))),BinaryOp("&&",Id("D"),BinaryOp("==",Id("E"),Id("F"))))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,380))
	def test_Expr_8(self):
		input = """
				string[] createString(int b){
                    for(i = 0; i <= length; i = i + 1){
                        array[i] = (char)*b;
                    }
                }
                void main(){
                    makeThisInt(3)[a+"3.2"];
                    do
                        job1;
                        job2();
                        job3(a[a[a[a[a[job(4)]]]]]);
                    while(working);
                    for(job(); job(); job(job())){
                        if(isJobDone == true)
                            printf("Partyyyy");
                    }
                }
				"""
		expect = str(Program([FuncDecl(Id("createString"),[VarDecl("b",IntType())],ArrayPointerType(StringType()),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),Id("length")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",ArrayCell(Id("array"),Id("i")),BinaryOp("*",Id("char"),Id("b")))]))])),FuncDecl(Id("main"),[],VoidType(),Block([ArrayCell(CallExpr(Id("makeThisInt"),[IntLiteral(3)]),BinaryOp("+",Id("a"),StringLiteral("3.2"))),Dowhile([Id("job1"),CallExpr(Id("job2"),[]),CallExpr(Id("job3"),[ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),CallExpr(Id("job"),[IntLiteral(4)]))))))])],Id("working")),For(CallExpr(Id("job"),[]),CallExpr(Id("job"),[]),CallExpr(Id("job"),[CallExpr(Id("job"),[])]),Block([If(BinaryOp("==",Id("isJobDone"),BooleanLiteral(True)),CallExpr(Id("printf"),[StringLiteral("Partyyyy")]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,381))
	def test_Expr_9(self):
		input = """
				void main(){
                    monitor = "This is some real shit!";
                    A = B * C = C % D / 3.2e-2 && arr[arr(3.4)] || ABC && -3.5 = !true;
                    do{
                        A = B= C = D = E;
                    }{
                        _+_+_+_+_+_+_+_+_+_+_+_+_+_+_;
                    }{
                        _-_-_-_-_-_-_-_-_-_-_-_-_-_;
                    }
                    while(beCrazy());
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("monitor"),StringLiteral("This is some real shit!")),BinaryOp("=",Id("A"),BinaryOp("=",BinaryOp("*",Id("B"),Id("C")),BinaryOp("=",BinaryOp("||",BinaryOp("&&",BinaryOp("/",BinaryOp("%",Id("C"),Id("D")),FloatLiteral(0.032)),ArrayCell(Id("arr"),CallExpr(Id("arr"),[FloatLiteral(3.4)]))),BinaryOp("&&",Id("ABC"),UnaryOp("-",FloatLiteral(3.5)))),UnaryOp("!",BooleanLiteral(True))))),Dowhile([Block([BinaryOp("=",Id("A"),BinaryOp("=",Id("B"),BinaryOp("=",Id("C"),BinaryOp("=",Id("D"),Id("E")))))]),Block([BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_"))]),Block([BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("-",Id("_"),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_")),Id("_"))])],CallExpr(Id("beCrazy"),[]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,382))
	def test_Expr_10(self):
		input = """
				void main(){
                    funcall(a, a + 1);
                    if(youMeetSomeone)
                        return say("Hi");
                    else
                        return A+B*C(a[a[3]]);
                    return "Still runnnnnnn";
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("funcall"),[Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))]),If(Id("youMeetSomeone"),Return(CallExpr(Id("say"),[StringLiteral("Hi")])),Return(BinaryOp("+",Id("A"),BinaryOp("*",Id("B"),CallExpr(Id("C"),[ArrayCell(Id("a"),ArrayCell(Id("a"),IntLiteral(3)))]))))),Return(StringLiteral("Still runnnnnnn"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,383))
	def test_Expr_11(self):
		input = """
				void main(){
                    for(A != B; B = C = D = -E; i+_){
                        for(A%b; C%D; C[D%E]){
                            createString(createString(createString(a[a[a[4]]])));
                        }
                    }
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("!=",Id("A"),Id("B")),BinaryOp("=",Id("B"),BinaryOp("=",Id("C"),BinaryOp("=",Id("D"),UnaryOp("-",Id("E"))))),BinaryOp("+",Id("i"),Id("_")),Block([For(BinaryOp("%",Id("A"),Id("b")),BinaryOp("%",Id("C"),Id("D")),ArrayCell(Id("C"),BinaryOp("%",Id("D"),Id("E"))),Block([CallExpr(Id("createString"),[CallExpr(Id("createString"),[CallExpr(Id("createString"),[ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),IntLiteral(4))))])])])]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,384))
	def test_Expr_12(self):
		input = """
				void main(){
                    testSomeMassiveThings(true);
                    arr[0] = -arr((arr[1] + arr[2])*(arr[3] * arr[4] / arr[5]))[arr[6]=arr[7]=arr[8] > arr[9]] <= arr[10];
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("testSomeMassiveThings"),[BooleanLiteral(True)]),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(0)),BinaryOp("<=",UnaryOp("-",ArrayCell(CallExpr(Id("arr"),[BinaryOp("*",BinaryOp("+",ArrayCell(Id("arr"),IntLiteral(1)),ArrayCell(Id("arr"),IntLiteral(2))),BinaryOp("/",BinaryOp("*",ArrayCell(Id("arr"),IntLiteral(3)),ArrayCell(Id("arr"),IntLiteral(4))),ArrayCell(Id("arr"),IntLiteral(5))))]),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(6)),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(7)),BinaryOp(">",ArrayCell(Id("arr"),IntLiteral(8)),ArrayCell(Id("arr"),IntLiteral(9))))))),ArrayCell(Id("arr"),IntLiteral(10))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,385))
	def test_Expr_13(self):
		input = """
				void main(){
                    funcall(a, a + 1);
                    do
                        do
                            do
                                A = nonAss(a[ass])[ass];
                                B != C = D + E == 6.e-12;
							while(A);
							while(A);
							while(A);
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("funcall"),[Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))]),Dowhile([Dowhile([Dowhile([BinaryOp("=",Id("A"),ArrayCell(CallExpr(Id("nonAss"),[ArrayCell(Id("a"),Id("ass"))]),Id("ass"))),BinaryOp("=",BinaryOp("!=",Id("B"),Id("C")),BinaryOp("==",BinaryOp("+",Id("D"),Id("E")),FloatLiteral(6e-12)))],Id("A"))],Id("A"))],Id("A"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,386))
	def test_Expr_14(self):
		input = """
				void main(){
                    funcall(a, a + 1);
                    if(char*b+arr[char*char(b)])
                        for(smt;smt;smt){}
                    else
                        return;
                    arr[arr[arr[3]]];
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("funcall"),[Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))]),If(BinaryOp("+",BinaryOp("*",Id("char"),Id("b")),ArrayCell(Id("arr"),BinaryOp("*",Id("char"),CallExpr(Id("char"),[Id("b")])))),For(Id("smt"),Id("smt"),Id("smt"),Block([])),Return()),ArrayCell(Id("arr"),ArrayCell(Id("arr"),ArrayCell(Id("arr"),IntLiteral(3))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,387))
	def test_Expr_15(self):
		input = """
				void main(){
                    funcall(a, a + 1);
                    do
                        do
                            do
                                A = (nonAss(a[ass])[ass])[ass];
                                B != C = D + E == 6.e-12;
                                While(true);
                            while(true);
                        while(true);
                    while(true);
                    return exit(0);
                }
				"""
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("funcall"),[Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))]),Dowhile([Dowhile([Dowhile([BinaryOp("=",Id("A"),ArrayCell(ArrayCell(CallExpr(Id("nonAss"),[ArrayCell(Id("a"),Id("ass"))]),Id("ass")),Id("ass"))),BinaryOp("=",BinaryOp("!=",Id("B"),Id("C")),BinaryOp("==",BinaryOp("+",Id("D"),Id("E")),FloatLiteral(6e-12))),CallExpr(Id("While"),[BooleanLiteral(True)])],BooleanLiteral(True))],BooleanLiteral(True))],BooleanLiteral(True)),Return(CallExpr(Id("exit"),[IntLiteral(0)]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,388))
#================================================================================================



#========================================TEST OVERALLS========================================
	def test_Over_1(self):
		input = """
				int isInterrupt;
                int countNumber;
                //countNumber = 0;
                void ISR(int isInterrupt){
                    interruptEnable(true);
                    interruptSet(10);
                    interrupt();
                }
                int main(){
                    int count;
                    count = 0;
                    do{
                        checkInterrupt();
                        if(countNumber % 3 == 0) return interruptVector[countNumber];
                        else
                            for(count; count+count; isInterrupt)
                                countNumber = checkInterrupt(interruptVector[countNumber[count]]);
                        noInterrupt();
                    }
                    while(true);
                }
				"""
		expect = str(Program([VarDecl("isInterrupt",IntType()),VarDecl("countNumber",IntType()),FuncDecl(Id("ISR"),[VarDecl("isInterrupt",IntType())],VoidType(),Block([CallExpr(Id("interruptEnable"),[BooleanLiteral(True)]),CallExpr(Id("interruptSet"),[IntLiteral(10)]),CallExpr(Id("interrupt"),[])])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("count",IntType()),BinaryOp("=",Id("count"),IntLiteral(0)),Dowhile([Block([CallExpr(Id("checkInterrupt"),[]),If(BinaryOp("==",BinaryOp("%",Id("countNumber"),IntLiteral(3)),IntLiteral(0)),Return(ArrayCell(Id("interruptVector"),Id("countNumber"))),For(Id("count"),BinaryOp("+",Id("count"),Id("count")),Id("isInterrupt"),BinaryOp("=",Id("countNumber"),CallExpr(Id("checkInterrupt"),[ArrayCell(Id("interruptVector"),ArrayCell(Id("countNumber"),Id("count")))])))),CallExpr(Id("noInterrupt"),[])])],BooleanLiteral(True))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,389))
	def test_Over_2(self):
		input = """
				int timer0, timer1;
                int threshhold;
                boolean[] checkTimers(){
                    if(timer0 == threshhold)
                        if(timer1 == threshhold)
                            for(i = 0; timer0 == threshhold; i = i + getCycle())
                                do
                                    timer0 = timer1[getCycle * cycle] + checkTimers(timer[timer[timer[checkTimers()]]]);
                                    timer1 = getCycle(cycle1 && cycle2 - 3 * cycle3 != 0);
                                while(timer0 != 0);
                        else
                            checkTimers();
                        timer1 = 0;
                        timer0 = timer1 && checkTimers(checkTimers(timer0[timer1[timer0]]));
                        return 0;
                }
				"""
		expect = str(Program([VarDecl("timer0",IntType()),VarDecl("timer1",IntType()),VarDecl("threshhold",IntType()),FuncDecl(Id("checkTimers"),[],ArrayPointerType(BoolType()),Block([If(BinaryOp("==",Id("timer0"),Id("threshhold")),If(BinaryOp("==",Id("timer1"),Id("threshhold")),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("==",Id("timer0"),Id("threshhold")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),CallExpr(Id("getCycle"),[]))),Dowhile([BinaryOp("=",Id("timer0"),BinaryOp("+",ArrayCell(Id("timer1"),BinaryOp("*",Id("getCycle"),Id("cycle"))),CallExpr(Id("checkTimers"),[ArrayCell(Id("timer"),ArrayCell(Id("timer"),ArrayCell(Id("timer"),CallExpr(Id("checkTimers"),[]))))]))),BinaryOp("=",Id("timer1"),CallExpr(Id("getCycle"),[BinaryOp("&&",Id("cycle1"),BinaryOp("!=",BinaryOp("-",Id("cycle2"),BinaryOp("*",IntLiteral(3),Id("cycle3"))),IntLiteral(0)))]))],BinaryOp("!=",Id("timer0"),IntLiteral(0)))),CallExpr(Id("checkTimers"),[]))),BinaryOp("=",Id("timer1"),IntLiteral(0)),BinaryOp("=",Id("timer0"),BinaryOp("&&",Id("timer1"),CallExpr(Id("checkTimers"),[CallExpr(Id("checkTimers"),[ArrayCell(Id("timer0"),ArrayCell(Id("timer1"),Id("timer0")))])]))),Return(IntLiteral(0))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,390))
	def test_Over_3(self):
		input = """
				int timer0, timer1;
                int threshhold;
                boolean[] checkTimers(){
                    if(timer0 == threshhold)
                        if(timer1 == threshhold)
                            for(i = 0; timer0 == threshhold; i = i + getCycle())
                                do
                                    timer0 = timer1[getCycle * cycle] + checkTimers(timer[timer[timer[checkTimers()]]]);
                                    timer1 = getCycle(cycle1 && cycle2 - 3 * cycle3 != 0);
                                while(timer0 != 0);
                        else
                            checkTimers();
                    timer1 = 0;
                    timer0 = timer1 && checkTimers(checkTimers(timer0[timer1[timer0]]));
                    return 0;
                }        
                int main(){
                    // doing nothing
                }
				"""
		expect = str(Program([VarDecl("timer0",IntType()),VarDecl("timer1",IntType()),VarDecl("threshhold",IntType()),FuncDecl(Id("checkTimers"),[],ArrayPointerType(BoolType()),Block([If(BinaryOp("==",Id("timer0"),Id("threshhold")),If(BinaryOp("==",Id("timer1"),Id("threshhold")),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("==",Id("timer0"),Id("threshhold")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),CallExpr(Id("getCycle"),[]))),Dowhile([BinaryOp("=",Id("timer0"),BinaryOp("+",ArrayCell(Id("timer1"),BinaryOp("*",Id("getCycle"),Id("cycle"))),CallExpr(Id("checkTimers"),[ArrayCell(Id("timer"),ArrayCell(Id("timer"),ArrayCell(Id("timer"),CallExpr(Id("checkTimers"),[]))))]))),BinaryOp("=",Id("timer1"),CallExpr(Id("getCycle"),[BinaryOp("&&",Id("cycle1"),BinaryOp("!=",BinaryOp("-",Id("cycle2"),BinaryOp("*",IntLiteral(3),Id("cycle3"))),IntLiteral(0)))]))],BinaryOp("!=",Id("timer0"),IntLiteral(0)))),CallExpr(Id("checkTimers"),[]))),BinaryOp("=",Id("timer1"),IntLiteral(0)),BinaryOp("=",Id("timer0"),BinaryOp("&&",Id("timer1"),CallExpr(Id("checkTimers"),[CallExpr(Id("checkTimers"),[ArrayCell(Id("timer0"),ArrayCell(Id("timer1"),Id("timer0")))])]))),Return(IntLiteral(0))])),FuncDecl(Id("main"),[],IntType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,391))
	def test_Over_4(self):
		input = """
				int timer0, timer1;
                int threshhold;
                boolean[] checkTimers(){
                    if(timer0 == threshhold)
                        if(timer1 == threshhold)
                            for(i = 0; timer0 == threshhold; i = i + getCycle())
                                do
                                    timer0 = timer1[getCycle * cycle] + checkTimers(timer[timer[timer[checkTimers()]]]);
                                    timer1 = getCycle(cycle1 && cycle2 - 3 * cycle3 != 0);
                                while(timer0 != 0);
                        else
                            checkTimers();
                    timer1 = 0;
                    timer0 = timer1 && checkTimers(checkTimers(timer0[timer1[timer0]]));                        return 0;
                }
                int main(){
                    int main;
                    break;
                    continue;
                    for(-timer; !timer; timer()){
                        for(i; j; k){
                            if(timer1 !=- timer2 = timer)
                                DO(something);
                        }
                        do
                            for(i; j; k){
                                if(timer1 !=- timer2 < timer)
                                    DO(something);
                            do 
                                makeFile(makeFile[makeFile()]);
                            while(true);
                            }
                        while(true);
                    }
                }
				"""
		expect = str(Program([VarDecl("timer0",IntType()),VarDecl("timer1",IntType()),VarDecl("threshhold",IntType()),FuncDecl(Id("checkTimers"),[],ArrayPointerType(BoolType()),Block([If(BinaryOp("==",Id("timer0"),Id("threshhold")),If(BinaryOp("==",Id("timer1"),Id("threshhold")),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("==",Id("timer0"),Id("threshhold")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),CallExpr(Id("getCycle"),[]))),Dowhile([BinaryOp("=",Id("timer0"),BinaryOp("+",ArrayCell(Id("timer1"),BinaryOp("*",Id("getCycle"),Id("cycle"))),CallExpr(Id("checkTimers"),[ArrayCell(Id("timer"),ArrayCell(Id("timer"),ArrayCell(Id("timer"),CallExpr(Id("checkTimers"),[]))))]))),BinaryOp("=",Id("timer1"),CallExpr(Id("getCycle"),[BinaryOp("&&",Id("cycle1"),BinaryOp("!=",BinaryOp("-",Id("cycle2"),BinaryOp("*",IntLiteral(3),Id("cycle3"))),IntLiteral(0)))]))],BinaryOp("!=",Id("timer0"),IntLiteral(0)))),CallExpr(Id("checkTimers"),[]))),BinaryOp("=",Id("timer1"),IntLiteral(0)),BinaryOp("=",Id("timer0"),BinaryOp("&&",Id("timer1"),CallExpr(Id("checkTimers"),[CallExpr(Id("checkTimers"),[ArrayCell(Id("timer0"),ArrayCell(Id("timer1"),Id("timer0")))])]))),Return(IntLiteral(0))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("main",IntType()),Break(),Continue(),For(UnaryOp("-",Id("timer")),UnaryOp("!",Id("timer")),CallExpr(Id("timer"),[]),Block([For(Id("i"),Id("j"),Id("k"),Block([If(BinaryOp("=",BinaryOp("!=",Id("timer1"),UnaryOp("-",Id("timer2"))),Id("timer")),CallExpr(Id("DO"),[Id("something")]))])),Dowhile([For(Id("i"),Id("j"),Id("k"),Block([If(BinaryOp("!=",Id("timer1"),BinaryOp("<",UnaryOp("-",Id("timer2")),Id("timer"))),CallExpr(Id("DO"),[Id("something")])),Dowhile([CallExpr(Id("makeFile"),[ArrayCell(Id("makeFile"),CallExpr(Id("makeFile"),[]))])],BooleanLiteral(True))]))],BooleanLiteral(True))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,392))
	def test_Over_5(self):
		input = """
				int timer0, timer1;
                int threshhold;
                boolean[] checkTimers(){
                    if(timer0 == threshhold)
                        if(timer1 == threshhold)
                            for(i = 0; timer0 == threshhold; i = i + getCycle())
                                do
                                    timer0 = timer1[getCycle * cycle] + checkTimers(timer[timer[timer[checkTimers()]]]);
                                    timer1 = getCycle(cycle1 && cycle2 - 3 * cycle3 != 0);
                                while(timer0 != 0);
                        else
                            checkTimers();
                    timer1 = 0;
                    timer0 = timer1 && checkTimers(checkTimers(timer0[timer1[timer0]]));                        return 0;
                }
                int main(){
                    int main;
                    break;
                    continue;
                    for(-timer; !timer; timer()){
                        for(i; j; k){
                            if(timer1 !=- timer2 = timer)
                                DO(something);
                        }
                        do
                            for(i; j; k){
                                if(timer1 !=- timer2 = timer)
                                    DO(something);
                            do 
                                makeFile(makeFile[makeFile()]);
                                !timer1 && timer0 || timer1 = timer0 = timer1 = timer[timer[timer1 + _[timer0[timer0]]]];
                            while(true);
                            }
                        while(true);
                    }
                }
				"""
		expect = str(Program([VarDecl("timer0",IntType()),VarDecl("timer1",IntType()),VarDecl("threshhold",IntType()),FuncDecl(Id("checkTimers"),[],ArrayPointerType(BoolType()),Block([If(BinaryOp("==",Id("timer0"),Id("threshhold")),If(BinaryOp("==",Id("timer1"),Id("threshhold")),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("==",Id("timer0"),Id("threshhold")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),CallExpr(Id("getCycle"),[]))),Dowhile([BinaryOp("=",Id("timer0"),BinaryOp("+",ArrayCell(Id("timer1"),BinaryOp("*",Id("getCycle"),Id("cycle"))),CallExpr(Id("checkTimers"),[ArrayCell(Id("timer"),ArrayCell(Id("timer"),ArrayCell(Id("timer"),CallExpr(Id("checkTimers"),[]))))]))),BinaryOp("=",Id("timer1"),CallExpr(Id("getCycle"),[BinaryOp("&&",Id("cycle1"),BinaryOp("!=",BinaryOp("-",Id("cycle2"),BinaryOp("*",IntLiteral(3),Id("cycle3"))),IntLiteral(0)))]))],BinaryOp("!=",Id("timer0"),IntLiteral(0)))),CallExpr(Id("checkTimers"),[]))),BinaryOp("=",Id("timer1"),IntLiteral(0)),BinaryOp("=",Id("timer0"),BinaryOp("&&",Id("timer1"),CallExpr(Id("checkTimers"),[CallExpr(Id("checkTimers"),[ArrayCell(Id("timer0"),ArrayCell(Id("timer1"),Id("timer0")))])]))),Return(IntLiteral(0))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("main",IntType()),Break(),Continue(),For(UnaryOp("-",Id("timer")),UnaryOp("!",Id("timer")),CallExpr(Id("timer"),[]),Block([For(Id("i"),Id("j"),Id("k"),Block([If(BinaryOp("=",BinaryOp("!=",Id("timer1"),UnaryOp("-",Id("timer2"))),Id("timer")),CallExpr(Id("DO"),[Id("something")]))])),Dowhile([For(Id("i"),Id("j"),Id("k"),Block([If(BinaryOp("=",BinaryOp("!=",Id("timer1"),UnaryOp("-",Id("timer2"))),Id("timer")),CallExpr(Id("DO"),[Id("something")])),Dowhile([CallExpr(Id("makeFile"),[ArrayCell(Id("makeFile"),CallExpr(Id("makeFile"),[]))]),BinaryOp("=",BinaryOp("||",BinaryOp("&&",UnaryOp("!",Id("timer1")),Id("timer0")),Id("timer1")),BinaryOp("=",Id("timer0"),BinaryOp("=",Id("timer1"),ArrayCell(Id("timer"),ArrayCell(Id("timer"),BinaryOp("+",Id("timer1"),ArrayCell(Id("_"),ArrayCell(Id("timer0"),Id("timer0")))))))))],BooleanLiteral(True))]))],BooleanLiteral(True))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,393))
	def test_Over_6(self):
		input = """
				int matrix1, matrix2;
                int sum;
                string[] mul(int matrix1, int matrix2){
                    countMatric = 0;
                    for(i = 0; i < length(sum(matrix1,matrix2)); i = i * countMatrix){
                        countMatrix == matrix1[matrix2[matrix1(countMatrix)]];
                        matrix1 = matrix1 + matrix2 * matrix2(matrix3 * matrix4[matrix(-matrix % matrix5)]);
                        if(matrix1 + matrix2(matrix2(matrix2(countMatrix)))[matrix1+matrix2+countNumber]){
                            return true;
                            break;
                            continue;
                        }
                        else{
                            crateMatrix(matrix1, matrix2, sumMatrix(matrix1, matrix2));
                            do{
                                if(matrix1 * matrix2[matrix2-matrix3[countNumber[_[_[3]]]]]){
                                    replace(matrix1) = !matrix2 - matrix4 * -matrix5;
                                }
                                do
                                    for(matrix1[matrix2 - matrix3(matrix1)]; matrix1(matrix1(matrix1[matrix2()])); !matrix1 - matrix2*(matrix1 - matrix2*(matrix1 * matrix2))){
                                        matrix1 = - matrix2;
                                    }
                                while(matrix1 != -matrix2);
                            }
                            while(matrix1 == matrix2);
                        }
                    }
                }
				"""
		expect = str(Program([VarDecl("matrix1",IntType()),VarDecl("matrix2",IntType()),VarDecl("sum",IntType()),FuncDecl(Id("mul"),[VarDecl("matrix1",IntType()),VarDecl("matrix2",IntType())],ArrayPointerType(StringType()),Block([BinaryOp("=",Id("countMatric"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),CallExpr(Id("length"),[CallExpr(Id("sum"),[Id("matrix1"),Id("matrix2")])])),BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),Id("countMatrix"))),Block([BinaryOp("==",Id("countMatrix"),ArrayCell(Id("matrix1"),ArrayCell(Id("matrix2"),CallExpr(Id("matrix1"),[Id("countMatrix")])))),BinaryOp("=",Id("matrix1"),BinaryOp("+",Id("matrix1"),BinaryOp("*",Id("matrix2"),CallExpr(Id("matrix2"),[BinaryOp("*",Id("matrix3"),ArrayCell(Id("matrix4"),CallExpr(Id("matrix"),[BinaryOp("%",UnaryOp("-",Id("matrix")),Id("matrix5"))])))])))),If(BinaryOp("+",Id("matrix1"),ArrayCell(CallExpr(Id("matrix2"),[CallExpr(Id("matrix2"),[CallExpr(Id("matrix2"),[Id("countMatrix")])])]),BinaryOp("+",BinaryOp("+",Id("matrix1"),Id("matrix2")),Id("countNumber")))),Block([Return(BooleanLiteral(True)),Break(),Continue()]),Block([CallExpr(Id("crateMatrix"),[Id("matrix1"),Id("matrix2"),CallExpr(Id("sumMatrix"),[Id("matrix1"),Id("matrix2")])]),Dowhile([Block([If(BinaryOp("*",Id("matrix1"),ArrayCell(Id("matrix2"),BinaryOp("-",Id("matrix2"),ArrayCell(Id("matrix3"),ArrayCell(Id("countNumber"),ArrayCell(Id("_"),ArrayCell(Id("_"),IntLiteral(3)))))))),Block([BinaryOp("=",CallExpr(Id("replace"),[Id("matrix1")]),BinaryOp("-",UnaryOp("!",Id("matrix2")),BinaryOp("*",Id("matrix4"),UnaryOp("-",Id("matrix5")))))])),Dowhile([For(ArrayCell(Id("matrix1"),BinaryOp("-",Id("matrix2"),CallExpr(Id("matrix3"),[Id("matrix1")]))),CallExpr(Id("matrix1"),[CallExpr(Id("matrix1"),[ArrayCell(Id("matrix1"),CallExpr(Id("matrix2"),[]))])]),BinaryOp("-",UnaryOp("!",Id("matrix1")),BinaryOp("*",Id("matrix2"),BinaryOp("-",Id("matrix1"),BinaryOp("*",Id("matrix2"),BinaryOp("*",Id("matrix1"),Id("matrix2")))))),Block([BinaryOp("=",Id("matrix1"),UnaryOp("-",Id("matrix2")))]))],BinaryOp("!=",Id("matrix1"),UnaryOp("-",Id("matrix2"))))])],BinaryOp("==",Id("matrix1"),Id("matrix2")))]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,394))
	def test_Over_7(self):
		input = """
				int matrix1, matrix2;
                int sum;
                string[] mul(int matrix1, int matrix2){
                    countMatric = 0;
                    for(i = 0; i < length(sum(matrix1,matrix2)); i = i * countMatrix){
                        countMatrix == matrix1[matrix2[matrix1(countMatrix)]];
                        matrix1 = matrix1 + matrix2 * matrix2(matrix3 * matrix4[matrix(-matrix % matrix5)]);
                        if(matrix1 + matrix2(matrix2(matrix2(countMatrix)))[matrix1+matrix2+countNumber]){
                            return true;
                            break;
                            continue;
                        }
                        else{
                            crateMatrix(matrix1, matrix2, sumMatrix(matrix1, matrix2));
                            do{
                                if(matrix1 * matrix2[matrix2-matrix3[countNumber[_[_[3]]]]]){
                                    replace(matrix1) = !matrix2 - matrix4 * -matrix5;
                                }
                                do
                                    for(matrix1[matrix2 - matrix3(matrix1)]; matrix1(matrix1(matrix1[matrix2()])); !matrix1 - matrix2*(matrix1 - matrix2*(matrix1 * matrix2))){
                                        matrix1 = - matrix2;
                                    }
                                while(matrix1 != -matrix2);
                            }
                            while(matrix1 == matrix2);
                        }
                    }
                }
                int main(){
                    int count;
                    float set;
                    string matrix;
                    for(matrix1[matrix2[matrix2()]]; matrix1 * ( matrix1 * matrix2(matrix1 * matrix2)); matrix1(matrix1(matrix1 + matrix2 && matrix1 - matrix2 || matrix2))){
                        for(matrix1*matrix2*matrix3*matrix4; matrix1+matrix2+matrix3+matrix4; -matrix1-matrix2-matrix3-matrix4){
                            do
                                createMatrix(matrix1%matrix2%matrix, matrix1 < matrix3 || matrix2 >= matrix4);
                                if(matrix1 <= -matrix2 + matrix2[matrix3()]){
                                    matrix2 = matrix3 * matrix3[matrix2[matrix3]];
                                }
                                else{
                                    createMatrix(matrix1&&matrix2,matrix1||matrix3,matrix4());
                                }
                            while(true);
                        }
                    }
                } 
				"""
		expect = str(Program([VarDecl("matrix1",IntType()),VarDecl("matrix2",IntType()),VarDecl("sum",IntType()),FuncDecl(Id("mul"),[VarDecl("matrix1",IntType()),VarDecl("matrix2",IntType())],ArrayPointerType(StringType()),Block([BinaryOp("=",Id("countMatric"),IntLiteral(0)),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),CallExpr(Id("length"),[CallExpr(Id("sum"),[Id("matrix1"),Id("matrix2")])])),BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),Id("countMatrix"))),Block([BinaryOp("==",Id("countMatrix"),ArrayCell(Id("matrix1"),ArrayCell(Id("matrix2"),CallExpr(Id("matrix1"),[Id("countMatrix")])))),BinaryOp("=",Id("matrix1"),BinaryOp("+",Id("matrix1"),BinaryOp("*",Id("matrix2"),CallExpr(Id("matrix2"),[BinaryOp("*",Id("matrix3"),ArrayCell(Id("matrix4"),CallExpr(Id("matrix"),[BinaryOp("%",UnaryOp("-",Id("matrix")),Id("matrix5"))])))])))),If(BinaryOp("+",Id("matrix1"),ArrayCell(CallExpr(Id("matrix2"),[CallExpr(Id("matrix2"),[CallExpr(Id("matrix2"),[Id("countMatrix")])])]),BinaryOp("+",BinaryOp("+",Id("matrix1"),Id("matrix2")),Id("countNumber")))),Block([Return(BooleanLiteral(True)),Break(),Continue()]),Block([CallExpr(Id("crateMatrix"),[Id("matrix1"),Id("matrix2"),CallExpr(Id("sumMatrix"),[Id("matrix1"),Id("matrix2")])]),Dowhile([Block([If(BinaryOp("*",Id("matrix1"),ArrayCell(Id("matrix2"),BinaryOp("-",Id("matrix2"),ArrayCell(Id("matrix3"),ArrayCell(Id("countNumber"),ArrayCell(Id("_"),ArrayCell(Id("_"),IntLiteral(3)))))))),Block([BinaryOp("=",CallExpr(Id("replace"),[Id("matrix1")]),BinaryOp("-",UnaryOp("!",Id("matrix2")),BinaryOp("*",Id("matrix4"),UnaryOp("-",Id("matrix5")))))])),Dowhile([For(ArrayCell(Id("matrix1"),BinaryOp("-",Id("matrix2"),CallExpr(Id("matrix3"),[Id("matrix1")]))),CallExpr(Id("matrix1"),[CallExpr(Id("matrix1"),[ArrayCell(Id("matrix1"),CallExpr(Id("matrix2"),[]))])]),BinaryOp("-",UnaryOp("!",Id("matrix1")),BinaryOp("*",Id("matrix2"),BinaryOp("-",Id("matrix1"),BinaryOp("*",Id("matrix2"),BinaryOp("*",Id("matrix1"),Id("matrix2")))))),Block([BinaryOp("=",Id("matrix1"),UnaryOp("-",Id("matrix2")))]))],BinaryOp("!=",Id("matrix1"),UnaryOp("-",Id("matrix2"))))])],BinaryOp("==",Id("matrix1"),Id("matrix2")))]))]))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("count",IntType()),VarDecl("set",FloatType()),VarDecl("matrix",StringType()),For(ArrayCell(Id("matrix1"),ArrayCell(Id("matrix2"),CallExpr(Id("matrix2"),[]))),BinaryOp("*",Id("matrix1"),BinaryOp("*",Id("matrix1"),CallExpr(Id("matrix2"),[BinaryOp("*",Id("matrix1"),Id("matrix2"))]))),CallExpr(Id("matrix1"),[CallExpr(Id("matrix1"),[BinaryOp("||",BinaryOp("&&",BinaryOp("+",Id("matrix1"),Id("matrix2")),BinaryOp("-",Id("matrix1"),Id("matrix2"))),Id("matrix2"))])]),Block([For(BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("matrix1"),Id("matrix2")),Id("matrix3")),Id("matrix4")),BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("matrix1"),Id("matrix2")),Id("matrix3")),Id("matrix4")),BinaryOp("-",BinaryOp("-",BinaryOp("-",UnaryOp("-",Id("matrix1")),Id("matrix2")),Id("matrix3")),Id("matrix4")),Block([Dowhile([CallExpr(Id("createMatrix"),[BinaryOp("%",BinaryOp("%",Id("matrix1"),Id("matrix2")),Id("matrix")),BinaryOp("||",BinaryOp("<",Id("matrix1"),Id("matrix3")),BinaryOp(">=",Id("matrix2"),Id("matrix4")))]),If(BinaryOp("<=",Id("matrix1"),BinaryOp("+",UnaryOp("-",Id("matrix2")),ArrayCell(Id("matrix2"),CallExpr(Id("matrix3"),[])))),Block([BinaryOp("=",Id("matrix2"),BinaryOp("*",Id("matrix3"),ArrayCell(Id("matrix3"),ArrayCell(Id("matrix2"),Id("matrix3")))))]),Block([CallExpr(Id("createMatrix"),[BinaryOp("&&",Id("matrix1"),Id("matrix2")),BinaryOp("||",Id("matrix1"),Id("matrix3")),CallExpr(Id("matrix4"),[])])]))],BooleanLiteral(True))]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,395))
	def test_Over_8(self):
		input = """
				int return_to_easy_testases;
                float[] function(int a, string b, boolean c){
                    for(i = 0; i <= 9; i = i * 3){
                        if(arr[i] == 3) return true;
                        else continue;
                        do
                            A = B + C * D % E == F && G;
                            return B != -C+D*EF[EF[EF()]];
                            a;
                        while(A == B = C);
                    }
                    float String;
                }
				"""
		expect = str(Program([VarDecl("return_to_easy_testases",IntType()),FuncDecl(Id("function"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",BoolType())],ArrayPointerType(FloatType()),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(9)),BinaryOp("=",Id("i"),BinaryOp("*",Id("i"),IntLiteral(3))),Block([If(BinaryOp("==",ArrayCell(Id("arr"),Id("i")),IntLiteral(3)),Return(BooleanLiteral(True)),Continue()),Dowhile([BinaryOp("=",Id("A"),BinaryOp("&&",BinaryOp("==",BinaryOp("+",Id("B"),BinaryOp("%",BinaryOp("*",Id("C"),Id("D")),Id("E"))),Id("F")),Id("G"))),Return(BinaryOp("!=",Id("B"),BinaryOp("+",UnaryOp("-",Id("C")),BinaryOp("*",Id("D"),ArrayCell(Id("EF"),ArrayCell(Id("EF"),CallExpr(Id("EF"),[]))))))),Id("a")],BinaryOp("=",BinaryOp("==",Id("A"),Id("B")),Id("C")))])),VarDecl("String",FloatType())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,396))
	def test_Over_9(self):
		input = """
				int a;
                float b;
                
                float[] function(int a, string b, boolean c){
                    if(a == b && b != c[c*c[3*4]]){
                        createString(a,b,c[3.4e-112]);
                        do
                            youAlmostThere = 1;
                            name = "Phan Gia Anh";
                        while(true);
                        for(fun; sad; tear){
                            A = B = C = D = E % F % G && H && I && J;
                        }
                    }
                }
				"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",FloatType()),FuncDecl(Id("function"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",BoolType())],ArrayPointerType(FloatType()),Block([If(BinaryOp("&&",BinaryOp("==",Id("a"),Id("b")),BinaryOp("!=",Id("b"),ArrayCell(Id("c"),BinaryOp("*",Id("c"),ArrayCell(Id("c"),BinaryOp("*",IntLiteral(3),IntLiteral(4))))))),Block([CallExpr(Id("createString"),[Id("a"),Id("b"),ArrayCell(Id("c"),FloatLiteral(3.4e-112))]),Dowhile([BinaryOp("=",Id("youAlmostThere"),IntLiteral(1)),BinaryOp("=",Id("name"),StringLiteral("Phan Gia Anh"))],BooleanLiteral(True)),For(Id("fun"),Id("sad"),Id("tear"),Block([BinaryOp("=",Id("A"),BinaryOp("=",Id("B"),BinaryOp("=",Id("C"),BinaryOp("=",Id("D"),BinaryOp("&&",BinaryOp("&&",BinaryOp("&&",BinaryOp("%",BinaryOp("%",Id("E"),Id("F")),Id("G")),Id("H")),Id("I")),Id("J"))))))]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,397))
	def test_Over_10(self):
		input = """
				int a;
                string b;
                boolean c;

                boolean[] create(){
                    int main;
                    float main;
                    string main;
                    for(smt1; smt2; smt3){
                        smt1((((((((smt2))))))));
                    }
                }
				"""
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",BoolType()),FuncDecl(Id("create"),[],ArrayPointerType(BoolType()),Block([VarDecl("main",IntType()),VarDecl("main",FloatType()),VarDecl("main",StringType()),For(Id("smt1"),Id("smt2"),Id("smt3"),Block([CallExpr(Id("smt1"),[Id("smt2")])]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,398))
	def test_Over_11(self):
		input = """
				int a[99999999];
                float b[00000000000000000000000];
                string c[666666666666666];
                int[] main(){
                    for(a[a[a[a[a[45]]]]]; fun((((((3)))))); a[fun(a[fun(a[fun()])])]){
                        for(a*(a*(a*(a*(3)))); a-(a-(a-(a-(4)))); a+(a+(a+(a+(a+(5)))))){
                            if(a/3/4/5/6/7/8){
                                createString(a*b[b[b[b[b[3]]]]]-a(a(a(a(3)))));
                                for( i = a[i=a[i=a[i=a[3]]]]; i >= 0 && b - c * a[2]; i = i + a[i+a[i+a[i+a[3]]]]){
                                    do
                                        do
                                            for(a[a[a[3]]]; foo(foo(foo(3))); a[foo(a[foo()])]) printf("Hope you passed this");
                                        while(a == b = c = d = e);
                                    while(a+a+a+a+a+a+a+a+a+a+a+a);
                                }
                            }
                            else{
                                do
                                    // doing nothing here
                                    do
                                        do{}
                                            // still doing nothing here
                                        while(true);
                                    while(true);
                                while(true);
                            }
                        }
                        if(A=(B=(C=(D=(a))))){
                            for(something; something; something){
                                for(something; something; something){
                                    /* doing nothing here */
                                }
                            }
                        }
                    }
                }
				"""
		expect = str(Program([VarDecl("a",ArrayType(99999999,IntType())),VarDecl("b",ArrayType(0,FloatType())),VarDecl("c",ArrayType(666666666666666,StringType())),FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([For(ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),IntLiteral(45)))))),CallExpr(Id("fun"),[IntLiteral(3)]),ArrayCell(Id("a"),CallExpr(Id("fun"),[ArrayCell(Id("a"),CallExpr(Id("fun"),[ArrayCell(Id("a"),CallExpr(Id("fun"),[]))]))])),Block([For(BinaryOp("*",Id("a"),BinaryOp("*",Id("a"),BinaryOp("*",Id("a"),BinaryOp("*",Id("a"),IntLiteral(3))))),BinaryOp("-",Id("a"),BinaryOp("-",Id("a"),BinaryOp("-",Id("a"),BinaryOp("-",Id("a"),IntLiteral(4))))),BinaryOp("+",Id("a"),BinaryOp("+",Id("a"),BinaryOp("+",Id("a"),BinaryOp("+",Id("a"),BinaryOp("+",Id("a"),IntLiteral(5)))))),Block([If(BinaryOp("/",BinaryOp("/",BinaryOp("/",BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("a"),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)),IntLiteral(6)),IntLiteral(7)),IntLiteral(8)),Block([CallExpr(Id("createString"),[BinaryOp("-",BinaryOp("*",Id("a"),ArrayCell(Id("b"),ArrayCell(Id("b"),ArrayCell(Id("b"),ArrayCell(Id("b"),ArrayCell(Id("b"),IntLiteral(3))))))),CallExpr(Id("a"),[CallExpr(Id("a"),[CallExpr(Id("a"),[CallExpr(Id("a"),[IntLiteral(3)])])])]))]),For(BinaryOp("=",Id("i"),ArrayCell(Id("a"),BinaryOp("=",Id("i"),ArrayCell(Id("a"),BinaryOp("=",Id("i"),ArrayCell(Id("a"),BinaryOp("=",Id("i"),ArrayCell(Id("a"),IntLiteral(3))))))))),BinaryOp("&&",BinaryOp(">=",Id("i"),IntLiteral(0)),BinaryOp("-",Id("b"),BinaryOp("*",Id("c"),ArrayCell(Id("a"),IntLiteral(2))))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),ArrayCell(Id("a"),BinaryOp("+",Id("i"),ArrayCell(Id("a"),BinaryOp("+",Id("i"),ArrayCell(Id("a"),BinaryOp("+",Id("i"),ArrayCell(Id("a"),IntLiteral(3)))))))))),Block([Dowhile([Dowhile([For(ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),IntLiteral(3)))),CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[IntLiteral(3)])])]),ArrayCell(Id("a"),CallExpr(Id("foo"),[ArrayCell(Id("a"),CallExpr(Id("foo"),[]))])),CallExpr(Id("printf"),[StringLiteral("Hope you passed this")]))],BinaryOp("=",BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("c"),BinaryOp("=",Id("d"),Id("e")))))],BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")))]))]),Block([Dowhile([Dowhile([Dowhile([Block([])],BooleanLiteral(True))],BooleanLiteral(True))],BooleanLiteral(True))]))])),If(BinaryOp("=",Id("A"),BinaryOp("=",Id("B"),BinaryOp("=",Id("C"),BinaryOp("=",Id("D"),Id("a"))))),Block([For(Id("something"),Id("something"),Id("something"),Block([For(Id("something"),Id("something"),Id("something"),Block([]))]))]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,399))
	def test_Over_12(self):
		input = """
				int a[99999999];
                float b[00000000000000000000000];
                string c[666666666666666];
                int[] main(){
                    for(a[a[a[a[a[45]]]]]; fun((((((3)))))); a[fun(a[fun(a[fun()])])]){
                        for(a*(a*(a*(a*(3)))); a-(a-(a-(a-(4)))); a+(a+(a+(a+(a+(5)))))){
                            if(a/3/4/5/6/7/8){
                                createString(a*b[b[b[b[b[3]]]]]-a(a(a(a(3)))));
                                for( i = a[i=a[i=a[i=a[3]]]]; i >= 0 && b - c * a[2]; i = i + a[i+a[i+a[i+a[3]]]]){
                                    do
                                        do
                                            for(a[a[a[3]]]; foo(foo(foo(3))); a[foo(a[foo()])]) printf("Hope you passed this");
                                        while(a == b = c = d = e);
                                    while(a+a+a+a+a+a+a+a+a+a+a+a);
                                }
                            }
                            else{
                                do
                                    for(a(((((a))))); b(((((b))))); c[c[c[c[c[c[c]]]]]]){
                                        do
                                            if(condition == true || false || notTrueOrFalse && condition[true]){
                                                createWorld("Hello World" + "HelloW World"["Hello World" + _[_[_[_]]]]);
                                            }
                                            do
                                                makeThis(makeThis(makeThis()));
                                                makeThat[makeThat[makeThat[expression]]];
                                                do
                                                {
                                                    for(i - i[i-i[i-i[i-i[3]]]]; something; something){
                                                        return foo(A*A*A*A*A*A*A*A*A*A*A*A);
                                                    }
                                                }
                                                while(true);
                                            while(true);
                                        while(true);
                                    }
                                    do
                                        do{
                                            for(something; something; something){
                                                if(thisIsTrue)
                                                    printf("Well done");
                                                else
                                                    printf("Try again");
                                            }
                                        }
                                        while(true);
                                    while(true);
                                while(true);
                            }
                        }
                        if(A=(B=(C=(D=(a))))){
                            for(something; something; something){
                                for(something; something; something){
                                    if(youCanMakeThis){
                                        printf("Congratulations!");
                                        printf("Well done!");
                                    }
                                }
                            }
                        }
                    }
                } 
				"""
		expect = str(Program([VarDecl("a",ArrayType(99999999,IntType())),VarDecl("b",ArrayType(0,FloatType())),VarDecl("c",ArrayType(666666666666666,StringType())),FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([For(ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),IntLiteral(45)))))),CallExpr(Id("fun"),[IntLiteral(3)]),ArrayCell(Id("a"),CallExpr(Id("fun"),[ArrayCell(Id("a"),CallExpr(Id("fun"),[ArrayCell(Id("a"),CallExpr(Id("fun"),[]))]))])),Block([For(BinaryOp("*",Id("a"),BinaryOp("*",Id("a"),BinaryOp("*",Id("a"),BinaryOp("*",Id("a"),IntLiteral(3))))),BinaryOp("-",Id("a"),BinaryOp("-",Id("a"),BinaryOp("-",Id("a"),BinaryOp("-",Id("a"),IntLiteral(4))))),BinaryOp("+",Id("a"),BinaryOp("+",Id("a"),BinaryOp("+",Id("a"),BinaryOp("+",Id("a"),BinaryOp("+",Id("a"),IntLiteral(5)))))),Block([If(BinaryOp("/",BinaryOp("/",BinaryOp("/",BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("a"),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)),IntLiteral(6)),IntLiteral(7)),IntLiteral(8)),Block([CallExpr(Id("createString"),[BinaryOp("-",BinaryOp("*",Id("a"),ArrayCell(Id("b"),ArrayCell(Id("b"),ArrayCell(Id("b"),ArrayCell(Id("b"),ArrayCell(Id("b"),IntLiteral(3))))))),CallExpr(Id("a"),[CallExpr(Id("a"),[CallExpr(Id("a"),[CallExpr(Id("a"),[IntLiteral(3)])])])]))]),For(BinaryOp("=",Id("i"),ArrayCell(Id("a"),BinaryOp("=",Id("i"),ArrayCell(Id("a"),BinaryOp("=",Id("i"),ArrayCell(Id("a"),BinaryOp("=",Id("i"),ArrayCell(Id("a"),IntLiteral(3))))))))),BinaryOp("&&",BinaryOp(">=",Id("i"),IntLiteral(0)),BinaryOp("-",Id("b"),BinaryOp("*",Id("c"),ArrayCell(Id("a"),IntLiteral(2))))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),ArrayCell(Id("a"),BinaryOp("+",Id("i"),ArrayCell(Id("a"),BinaryOp("+",Id("i"),ArrayCell(Id("a"),BinaryOp("+",Id("i"),ArrayCell(Id("a"),IntLiteral(3)))))))))),Block([Dowhile([Dowhile([For(ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),IntLiteral(3)))),CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[IntLiteral(3)])])]),ArrayCell(Id("a"),CallExpr(Id("foo"),[ArrayCell(Id("a"),CallExpr(Id("foo"),[]))])),CallExpr(Id("printf"),[StringLiteral("Hope you passed this")]))],BinaryOp("=",BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("c"),BinaryOp("=",Id("d"),Id("e")))))],BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")),Id("a")))]))]),Block([Dowhile([For(CallExpr(Id("a"),[Id("a")]),CallExpr(Id("b"),[Id("b")]),ArrayCell(Id("c"),ArrayCell(Id("c"),ArrayCell(Id("c"),ArrayCell(Id("c"),ArrayCell(Id("c"),ArrayCell(Id("c"),Id("c"))))))),Block([Dowhile([If(BinaryOp("||",BinaryOp("||",BinaryOp("==",Id("condition"),BooleanLiteral(True)),BooleanLiteral(False)),BinaryOp("&&",Id("notTrueOrFalse"),ArrayCell(Id("condition"),BooleanLiteral(True)))),Block([CallExpr(Id("createWorld"),[BinaryOp("+",StringLiteral("Hello World"),ArrayCell(StringLiteral("HelloW World"),BinaryOp("+",StringLiteral("Hello World"),ArrayCell(Id("_"),ArrayCell(Id("_"),ArrayCell(Id("_"),Id("_")))))))])])),Dowhile([CallExpr(Id("makeThis"),[CallExpr(Id("makeThis"),[CallExpr(Id("makeThis"),[])])]),ArrayCell(Id("makeThat"),ArrayCell(Id("makeThat"),ArrayCell(Id("makeThat"),Id("expression")))),Dowhile([Block([For(BinaryOp("-",Id("i"),ArrayCell(Id("i"),BinaryOp("-",Id("i"),ArrayCell(Id("i"),BinaryOp("-",Id("i"),ArrayCell(Id("i"),BinaryOp("-",Id("i"),ArrayCell(Id("i"),IntLiteral(3))))))))),Id("something"),Id("something"),Block([Return(CallExpr(Id("foo"),[BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("A"),Id("A")),Id("A")),Id("A")),Id("A")),Id("A")),Id("A")),Id("A")),Id("A")),Id("A")),Id("A")),Id("A"))]))]))])],BooleanLiteral(True))],BooleanLiteral(True))],BooleanLiteral(True))])),Dowhile([Dowhile([Block([For(Id("something"),Id("something"),Id("something"),Block([If(Id("thisIsTrue"),CallExpr(Id("printf"),[StringLiteral("Well done")]),CallExpr(Id("printf"),[StringLiteral("Try again")]))]))])],BooleanLiteral(True))],BooleanLiteral(True))],BooleanLiteral(True))]))])),If(BinaryOp("=",Id("A"),BinaryOp("=",Id("B"),BinaryOp("=",Id("C"),BinaryOp("=",Id("D"),Id("a"))))),Block([For(Id("something"),Id("something"),Id("something"),Block([For(Id("something"),Id("something"),Id("something"),Block([If(Id("youCanMakeThis"),Block([CallExpr(Id("printf"),[StringLiteral("Congratulations!")]),CallExpr(Id("printf"),[StringLiteral("Well done!")])]))]))]))]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,400))
#=============================================================================================