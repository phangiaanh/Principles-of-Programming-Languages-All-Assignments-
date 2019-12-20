.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
	iconst_0
	dup
	istore_2
	istore_1
	goto Label4
Label2:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	pop
Label4:
	iload_1
	iconst_5
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	goto Label11
Label9:
	iload_2
	iconst_2
	iadd
	dup
	istore_2
	pop
Label11:
	iload_2
	bipush 7
	if_icmpgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	iload_1
	iload_2
	imul
	bipush 20
	if_icmple Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label18
	goto Label19
Label18:
	goto Label10
Label19:
	iload_1
	iload_2
	imul
	invokestatic io/putInt(I)V
Label15:
	goto Label9
Label10:
Label8:
	goto Label2
Label3:
Label1:
	return
.limit stack 16
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
