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
	iconst_5
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
	goto Label7
Label6:
	iload_1
	invokestatic io/putInt(I)V
Label7:
	iload_1
	iconst_5
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	iload_1
	bipush 10
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	goto Label15
Label14:
	iload_1
	invokestatic io/putInt(I)V
Label15:
Label11:
	iload_1
	iconst_5
	if_icmple Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	iload_1
	bipush 10
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	iand
	ifgt Label20
	goto Label21
Label20:
Label22:
.var 2 is a I from Label22 to Label23
	bipush 11
	istore_2
	iload_2
	invokestatic io/putInt(I)V
	iload_2
	iconst_1
	iadd
	invokestatic io/putInt(I)V
	iload_2
	iconst_2
	iadd
	invokestatic io/putInt(I)V
Label23:
Label21:
	iload_1
	invokestatic io/putInt(I)V
	iload_1
	bipush 55
	if_icmple Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	iload_1
	bipush 10
	if_icmpge Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	iand
	ifgt Label28
Label30:
	iload_1
	iconst_1
	iadd
	invokestatic io/putInt(I)V
Label31:
	goto Label29
Label28:
Label32:
	iload_1
	invokestatic io/putInt(I)V
Label33:
Label29:
	iconst_1
	ifgt Label34
	iload_1
	iconst_4
	iadd
	invokestatic io/putInt(I)V
	goto Label35
Label34:
	iconst_1
	ifgt Label36
	iload_1
	iconst_3
	iadd
	invokestatic io/putInt(I)V
	goto Label37
Label36:
	iconst_0
	ifgt Label38
	iload_1
	iconst_2
	iadd
	invokestatic io/putInt(I)V
	goto Label39
Label38:
	iconst_1
	ifgt Label40
	iload_1
	iconst_1
	iadd
	invokestatic io/putInt(I)V
	goto Label41
Label40:
	iload_1
	invokestatic io/putInt(I)V
Label41:
Label39:
Label37:
Label35:
Label1:
	return
.limit stack 22
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
