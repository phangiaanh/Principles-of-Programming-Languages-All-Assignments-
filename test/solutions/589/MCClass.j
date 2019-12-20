.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static factorial(I)I
Label0:
.var 0 is n I from Label0 to Label1
.var 1 is result I from Label0 to Label1
.var 2 is i I from Label0 to Label1
	iconst_1
	istore_1
	iconst_2
	dup
	istore_2
	pop
	goto Label4
Label2:
	iload_2
	iconst_1
	iadd
	dup
	istore_2
	pop
Label4:
	iload_2
	iload_0
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_1
	iload_2
	imul
	istore_1
Label8:
	goto Label2
Label3:
	iload_1
	goto Label1
Label1:
	ireturn
.limit stack 9
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label9 to Label10
Label9:
	ldc "Factorial of 10 is: "
	invokestatic io/putStringLn(Ljava/lang/String;)V
	bipush 10
	invokestatic MCClass/factorial(I)I
	invokestatic io/putIntLn(I)V
Label10:
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
