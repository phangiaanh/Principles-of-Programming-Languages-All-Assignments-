.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	invokestatic io/putIntLn(I)V
	iconst_1
	i2f
	ldc 1.1
	fadd
	ldc 1.11
	fadd
	ldc 1.111
	fadd
	invokestatic io/putFloatLn(F)V
	iconst_1
	iconst_0
	iconst_1
	iand
	iconst_0
	iand
	ior
	invokestatic io/putBoolLn(Z)V
	ldc "Your results are OK"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
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
