.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static printMultipleInt()V
Label0:
	iconst_1
	iconst_2
	imul
	iconst_3
	imul
	iconst_3
	idiv
	iconst_4
	imul
	iconst_5
	imul
	putstatic MCClass.a I
	getstatic MCClass.a I
	i2f
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	iconst_1
	iconst_2
	iadd
	iconst_3
	iadd
	iconst_4
	iadd
	iconst_5
	iadd
	bipush 6
	iadd
	bipush 7
	iadd
	bipush 8
	iadd
	bipush 9
	iadd
	bipush 10
	iadd
	putstatic MCClass.a I
	getstatic MCClass.a I
	i2f
	invokestatic io/putFloatLn(F)V
	invokestatic MCClass/printMultipleInt()V
Label3:
	return
.limit stack 2
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
