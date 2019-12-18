.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static test I

.method public static printMultipleInt()V
Label0:
	getstatic MCClass.test I
	iconst_1
	iconst_2
	imul
	iconst_3
	imul
	iconst_3
	irem
	iconst_4
	imul
	iconst_5
	imul
	sipush 10000
	idiv
	iadd
	putstatic MCClass.test I
	getstatic MCClass.test I
	i2f
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 3
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	iconst_0
	ifgt Label4
Label6:
	iconst_1
	putstatic MCClass.test I
Label7:
	goto Label5
Label4:
Label8:
	iconst_3
	iconst_0
	iadd
	putstatic MCClass.test I
Label9:
Label5:
	getstatic MCClass.test I
	i2f
	invokestatic io/putFloatLn(F)V
	invokestatic MCClass/printMultipleInt()V
Label3:
	return
.limit stack 3
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
