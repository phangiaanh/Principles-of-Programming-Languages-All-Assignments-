.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static process(I)V
.var 0 is a I from Label0 to Label1
Label0:
Label2:
Label4:
.var 1 is a I from Label4 to Label5
	iconst_1
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label5:
Label6:
.var 1 is a I from Label6 to Label7
	iconst_2
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label7:
Label3:
Label8:
Label10:
.var 1 is a I from Label10 to Label11
	iconst_3
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label11:
Label12:
.var 1 is a I from Label12 to Label13
	iconst_4
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label13:
Label9:
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label14 to Label15
Label14:
Label16:
	sipush 1000
	invokestatic MCClass/process(I)V
Label17:
Label15:
	return
.limit stack 1
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
