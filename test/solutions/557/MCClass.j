.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is j I from Label0 to Label1
.var 2 is result I from Label0 to Label1
	iconst_0
	dup
	istore_1
	istore_2
Label2:
Label4:
Label6:
Label8:
	iload_1
	iconst_5
	if_icmpgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label13
Label12:
	iload_2
	iconst_2
	iadd
	istore_2
Label13:
Label9:
Label7:
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	bipush 10
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label3
	goto Label2
Label3:
	iload_2
	iload_1
	iadd
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 13
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
