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
	istore_1
	pop
	goto Label4
Label2:
Label4:
	iload_1
	iconst_5
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	invokestatic io/putInt(I)V
	iconst_0
	dup
	istore_2
	pop
	goto Label11
Label9:
Label11:
	iload_2
	iconst_5
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	iload_2
	iconst_1
	iadd
	dup
	istore_2
	invokestatic io/putInt(I)V
Label15:
	goto Label9
Label10:
Label8:
	goto Label2
Label3:
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
