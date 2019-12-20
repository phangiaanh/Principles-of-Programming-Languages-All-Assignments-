.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static even(I)Z
Label0:
.var 0 is n I from Label0 to Label1
	iload_0
	iconst_2
	irem
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	goto Label1
Label1:
	ireturn
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label4 to Label5
Label4:
.var 1 is n I from Label4 to Label5
	iconst_0
	dup
	istore_1
	pop
	goto Label8
Label6:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	pop
Label8:
	iload_1
	bipush 20
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label7
Label11:
	iload_1
	invokestatic MCClass/even(I)Z
	ifgt Label13
Label15:
	iload_1
	iconst_2
	idiv
	invokestatic MCClass/odd(I)Z
	ifgt Label17
	goto Label18
Label17:
	iload_1
	invokestatic io/putInt(I)V
Label18:
Label16:
	goto Label14
Label13:
	goto Label6
Label14:
Label12:
	goto Label6
Label7:
Label5:
	return
.limit stack 8
.limit locals 2
.end method

.method public static odd(I)Z
Label19:
.var 0 is n I from Label19 to Label20
	iload_0
	iconst_2
	irem
	iconst_1
	if_icmpne Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	goto Label20
Label20:
	ireturn
.limit stack 9
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
