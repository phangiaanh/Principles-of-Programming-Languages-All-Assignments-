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
	iconst_2
	imul
	iadd
	iconst_3
	isub
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	istore_2
Label3:
	iload_1
	invokestatic io/putBool(Z)V
Label10:
.var 2 is a Z from Label10 to Label11
	iconst_1
	iconst_2
	iadd
	iconst_3
	iadd
	iconst_4
	iadd
	iconst_5
	iadd
	bipush 6
	iadd
	bipush 100
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	istore_2
Label11:
	iload_1
	invokestatic io/putBool(Z)V
Label18:
.var 2 is a Z from Label18 to Label19
	iconst_1
	dup
	istore_2
	dup
	istore_2
	dup
	istore_2
	istore_2
Label19:
	iload_1
	invokestatic io/putBool(Z)V
Label20:
.var 2 is a Z from Label20 to Label21
	iconst_3
	iconst_3
	if_icmpne Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	istore_2
Label21:
	iload_1
	invokestatic io/putBool(Z)V
Label28:
.var 2 is a Z from Label28 to Label29
	iconst_3
	bipush 9
	bipush 8
	imul
	bipush 7
	idiv
	iconst_3
	iconst_5
	imul
	iadd
	if_icmpeq Label34
	iconst_1
	goto Label35
Label34:
	iconst_0
Label35:
	istore_2
Label29:
	iload_1
	invokestatic io/putBool(Z)V
Label36:
.var 2 is a Z from Label36 to Label37
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
	ifge Label42
	iconst_1
	goto Label43
Label42:
	iconst_0
Label43:
	istore_2
Label37:
	iload_1
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 162
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
