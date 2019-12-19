.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static loop(I)V
Label0:
.var 0 is n I from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
	goto Label4
Label2:
Label4:
	iload_1
	iload_0
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
Label8:
	goto Label2
Label3:
Label1:
	return
.limit stack 9
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label9 to Label10
Label9:
.var 1 is a I from Label9 to Label10
	iconst_1
	istore_1
	goto Label13
Label11:
Label13:
	iconst_1
	ifle Label12
Label14:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	invokestatic MCClass/loop(I)V
	iload_1
	iconst_4
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label18
	goto Label19
Label18:
	goto Label12
Label19:
Label15:
	goto Label11
Label12:
Label10:
	return
.limit stack 14
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
