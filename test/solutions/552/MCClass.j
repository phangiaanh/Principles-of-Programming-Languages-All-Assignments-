.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is result I from Label0 to Label1
	iconst_0
	istore_3
	iconst_0
	istore_1
	goto Label4
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
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
	iconst_0
	istore_2
	goto Label9
Label7:
	iload_2
	iconst_1
	iadd
	istore_2
Label9:
	iload_2
	bipush 10
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label8
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label7
Label8:
	goto Label2
Label3:
	iload_3
	invokestatic io/putInt(I)V
	iconst_0
	istore_1
	goto Label14
Label12:
	iload_1
	iconst_1
	iadd
	istore_1
Label14:
	iload_1
	bipush 10
	if_icmpge Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label13
Label17:
	iload_3
	iconst_2
	iadd
	istore_3
Label18:
	goto Label12
Label13:
	iload_3
	invokestatic io/putInt(I)V
.var 4 is a [I from Label0 to Label1
	bipush 10
	newarray int
	astore 4
	iconst_0
	istore_1
	goto Label21
Label19:
	iload_1
	iconst_1
	iadd
	istore_1
Label21:
	iload_1
	bipush 10
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label20
	aload 4
	iload_1
	iaload
	invokestatic io/putInt(I)V
	goto Label19
Label20:
	iconst_0
	istore_1
	goto Label26
Label24:
	iload_1
	iconst_1
	iadd
	istore_1
Label26:
	iload_1
	bipush 10
	if_icmpge Label27
	iconst_1
	goto Label28
Label27:
	iconst_0
Label28:
	ifle Label25
	aload 4
	iload_1
	iload_1
	iastore
	goto Label24
Label25:
	iconst_0
	istore_1
	goto Label31
Label29:
	iload_1
	iconst_1
	iadd
	istore_1
Label31:
	iload_1
	bipush 10
	if_icmpge Label32
	iconst_1
	goto Label33
Label32:
	iconst_0
Label33:
	ifle Label30
	aload 4
	iload_1
	iaload
	invokestatic io/putInt(I)V
	goto Label29
Label30:
	iconst_0
	istore_1
	goto Label36
Label34:
	iload_1
	iconst_1
	iadd
	istore_1
Label36:
	iload_1
	bipush 10
	if_icmpge Label37
	iconst_1
	goto Label38
Label37:
	iconst_0
Label38:
	ifle Label35
	iload_3
	aload 4
	iload_1
	iaload
	iadd
	istore_3
	goto Label34
Label35:
	iload_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 17
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
