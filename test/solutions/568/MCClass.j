.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is k I from Label0 to Label1
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
Label7:
	iload_1
	iconst_5
	if_icmpeq Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
	goto Label12
Label11:
	goto Label2
Label12:
	iload_1
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label8:
	goto Label2
Label3:
	invokestatic io/putLn()V
	iconst_0
	istore_2
	goto Label15
Label13:
	iload_2
	iconst_1
	iadd
	istore_2
Label15:
	iload_2
	iconst_2
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label14
Label18:
	iconst_0
	istore_3
	goto Label22
Label20:
	iload_3
	iconst_1
	iadd
	istore_3
Label22:
	iload_3
	iconst_5
	if_icmpge Label23
	iconst_1
	goto Label24
Label23:
	iconst_0
Label24:
	ifle Label21
Label25:
	iload_3
	iconst_3
	if_icmpne Label27
	iconst_1
	goto Label28
Label27:
	iconst_0
Label28:
	ifgt Label29
	goto Label30
Label29:
	goto Label20
Label30:
	iload_2
	invokestatic io/putInt(I)V
	iload_3
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label26:
	goto Label20
Label21:
Label19:
	goto Label13
Label14:
Label1:
	return
.limit stack 11
.limit locals 4
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
