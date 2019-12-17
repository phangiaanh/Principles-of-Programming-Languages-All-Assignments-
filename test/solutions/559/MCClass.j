.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is number I from Label0 to Label1
	iconst_1
	istore_1
	iconst_3
	istore_2
	ldc "Enter a number: "
	invokestatic io/putStringLn(Ljava/lang/String;)V
	bipush 10
	istore_3
Label2:
Label4:
	ldc "number * i = "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_3
	iload_1
	imul
	invokestatic io/putIntLn(I)V
	iload_1
	iconst_1
	iadd
	istore_1
Label5:
Label6:
	ldc "number * j = "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_3
	iload_2
	imul
	invokestatic io/putIntLn(I)V
	iload_2
	iconst_1
	iadd
	istore_2
Label7:
	iload_1
	iconst_5
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	goto Label2
Label3:
Label1:
	return
.limit stack 3
.limit locals 4
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
