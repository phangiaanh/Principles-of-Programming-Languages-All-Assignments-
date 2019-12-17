.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a Z from Label0 to Label1
	iconst_0
	istore_1
Label2:
.var 2 is a Z from Label2 to Label3
	iconst_5
	iconst_3
	iconst_1
	iadd
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore_2
Label3:
	iload_1
	invokestatic io/putBool(Z)V
Label6:
.var 2 is a Z from Label6 to Label7
	iconst_5
	iconst_1
	iadd
	iconst_1
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	isub
	iconst_5
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	istore_2
Label7:
	iload_1
	invokestatic io/putBool(Z)V
Label10:
.var 2 is a Z from Label10 to Label11
	iconst_5
	bipush 9
	imul
	bipush 9
	iconst_5
	imul
	if_icmplt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	istore_2
Label11:
	iload_1
	invokestatic io/putBool(Z)V
Label14:
.var 2 is a Z from Label14 to Label15
	iconst_5
	bipush 30
	imul
	iconst_3
	bipush 7
	imul
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	istore_2
Label15:
	iload_1
	invokestatic io/putBool(Z)V
Label18:
.var 2 is a Z from Label18 to Label19
	iconst_5
	iconst_3
	iconst_2
	iadd
	if_icmpeq Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	istore_2
Label19:
	iload_1
	invokestatic io/putBool(Z)V
Label22:
.var 2 is a Z from Label22 to Label23
	iconst_5
	i2f
	ldc 2.5
	fsub
	iconst_3
	i2f
	ldc 7.1
	fmul
	bipush 15
	i2f
	fsub
	fcmpl
	ifge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	istore_2
Label23:
	iload_1
	invokestatic io/putBool(Z)V
Label26:
.var 2 is a Z from Label26 to Label27
	iconst_5
	iconst_3
	imul
	iconst_3
	iconst_5
	imul
	if_icmpne Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	istore_2
Label27:
	iload_1
	invokestatic io/putBool(Z)V
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
