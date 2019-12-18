.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	ldc 1.0
	fstore_1
Label2:
.var 2 is a I from Label2 to Label3
	iconst_5
	istore_2
	iload_2
	i2f
	invokestatic io/putFloatLn(F)V
Label4:
	bipush 6
	istore_2
	iload_2
	i2f
	invokestatic io/putFloatLn(F)V
Label5:
Label3:
	fload_1
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 3
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
