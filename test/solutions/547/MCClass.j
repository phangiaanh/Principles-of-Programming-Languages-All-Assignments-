.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iconst_1
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
	goto Label7
Label6:
	goto Label3
Label7:
	iload_1
	bipush 10
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	goto Label2
Label3:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 5
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
