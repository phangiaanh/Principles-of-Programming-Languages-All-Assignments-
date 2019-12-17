.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/testDoWhile()V
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public static testDoWhile()V
Label2:
.var 0 is a I from Label2 to Label3
	iconst_0
	istore_0
Label4:
	iload_0
	iconst_1
	iadd
	istore_0
	iload_0
	bipush 10
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	goto Label4
Label5:
	iload_0
	invokestatic io/putInt(I)V
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
