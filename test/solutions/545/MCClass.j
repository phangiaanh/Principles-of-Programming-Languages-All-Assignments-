.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	bipush 6
	istore_1
	iload_1
	bipush 7
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iload_1
	iconst_1
	iadd
	invokestatic io/putInt(I)V
	goto Label5
Label4:
	iload_1
	invokestatic io/putInt(I)V
Label5:
	iload_1
	bipush 10
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	goto Label9
Label8:
	iload_1
	iconst_2
	iadd
	invokestatic io/putInt(I)V
Label9:
	iload_1
	iconst_3
	iadd
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 6
.limit locals 2
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
