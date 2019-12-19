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
	invokestatic io/putInt(I)V
	iload_1
	bipush 55
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_1
	bipush 10
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	ifgt Label6
Label8:
	iload_1
	iconst_1
	iadd
	invokestatic io/putInt(I)V
Label9:
	goto Label7
Label6:
Label10:
	iload_1
	invokestatic io/putInt(I)V
Label11:
Label7:
	iconst_1
	ifgt Label12
	iload_1
	iconst_4
	iadd
	invokestatic io/putInt(I)V
	goto Label13
Label12:
	iconst_1
	ifgt Label14
	iload_1
	iconst_3
	iadd
	invokestatic io/putInt(I)V
	goto Label15
Label14:
	iconst_0
	ifgt Label16
	iload_1
	iconst_2
	iadd
	invokestatic io/putInt(I)V
	goto Label17
Label16:
	iconst_1
	ifgt Label18
	iload_1
	iconst_1
	iadd
	invokestatic io/putInt(I)V
	goto Label19
Label18:
	iload_1
	invokestatic io/putInt(I)V
Label19:
Label17:
Label15:
Label13:
Label1:
	return
.limit stack 11
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
