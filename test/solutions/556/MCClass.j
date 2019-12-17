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
Label4:
.var 2 is a I from Label4 to Label5
	bipush 7
	istore_2
	iload_2
	iconst_1
	iadd
	istore_2
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	bipush 10
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	goto Label2
Label3:
	iload_1
	invokestatic io/putInt(I)V
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
.var 4 is result I from Label0 to Label1
	iconst_0
	istore_2
	iconst_0
	istore_3
	iconst_0
	istore 4
	iconst_0
	istore_3
	iconst_0
	istore 4
Label8:
	iload_3
	iconst_5
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label13
Label12:
	iload 4
	iconst_2
	iadd
	istore 4
Label13:
	iload_3
	iconst_1
	iadd
	istore_3
	iload_3
	bipush 10
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label9
	goto Label8
Label9:
	iload 4
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 7
.limit locals 5
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
