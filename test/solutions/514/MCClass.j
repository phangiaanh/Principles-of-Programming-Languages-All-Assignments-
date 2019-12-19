.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/getFloatLiteral()F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static getFloatLiteral()F
Label2:
.var 0 is f F from Label2 to Label3
	ldc 3.3
	fstore_0
	fload_0
	fneg
	iconst_3
	i2f
	fmul
	iconst_2
	i2f
	fsub
	fstore_0
	fload_0
	goto Label3
Label3:
	freturn
.limit stack 5
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
