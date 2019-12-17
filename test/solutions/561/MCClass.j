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
Label7:
	iload_1
	iconst_5
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label12
Label11:
	goto Label3
Label12:
Label8:
	goto Label2
Label3:
	iload_3
	invokestatic io/putInt(I)V
	iconst_0
	istore_1
	goto Label15
Label13:
	iload_1
	iconst_1
	iadd
	istore_1
Label15:
	iload_1
	bipush 10
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label14
Label18:
	iload_1
	bipush 100
	if_icmpne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifgt Label22
	goto Label23
Label22:
Label24:
	iload_1
	bipush 100
	iadd
	istore_1
	goto Label13
Label25:
Label23:
	iload_1
	invokestatic io/putInt(I)V
Label19:
	goto Label13
Label14:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 10
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
