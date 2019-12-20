.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	dup
	istore_1
	pop
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
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
.var 2 is a I from Label7 to Label8
	bipush 6
	istore_2
	goto Label11
Label9:
Label11:
	iconst_1
	ifle Label10
Label12:
Label14:
	iload_2
	invokestatic io/putInt(I)V
Label16:
Label18:
	iload_2
	iconst_5
	if_icmple Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	iload_2
	bipush 10
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	iand
	ifgt Label24
	goto Label10
	goto Label25
Label24:
Label26:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label9
Label27:
Label25:
Label19:
Label17:
Label15:
	iload_2
	invokestatic io/putInt(I)V
Label13:
	goto Label9
Label10:
Label8:
	goto Label2
Label3:
	iload_1
	invokestatic io/putInt(I)V
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
