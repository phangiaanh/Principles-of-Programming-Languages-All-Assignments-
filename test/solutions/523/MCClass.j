.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_1
	iconst_2
	imul
	iconst_3
	imul
	dup
	istore_1
	pop
	goto Label4
Label2:
	iload_1
	iconst_2
	imul
	dup
	istore_1
	pop
Label4:
	iload_1
	bipush 100
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_1
	iload_1
	imul
	bipush 50
	if_icmplt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	invokestatic io/putBool(Z)V
	iload_1
	iload_1
	imul
	iconst_2
	irem
	iconst_0
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	invokestatic io/putBoolLn(Z)V
Label8:
	goto Label2
Label3:
Label1:
	return
.limit stack 9
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
