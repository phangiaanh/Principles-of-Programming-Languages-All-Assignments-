.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static enter(I)V
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_1
	istore_1
	goto Label4
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
Label4:
	iload_1
	iload_0
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	iload_1
	invokestatic io/putIntLn(I)V
	goto Label2
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label7 to Label8
Label7:
	bipush 10
	invokestatic MCClass/enter(I)V
	ldc 2.39
	ldc 2.3
	fadd
	invokestatic io/putFloatLn(F)V
Label8:
	return
.limit stack 4
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
