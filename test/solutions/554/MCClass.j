.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static testFor()V
Label0:
.var 0 is i I from Label0 to Label1
	iconst_0
	istore_0
	goto Label4
Label2:
	iload_0
	iconst_1
	iadd
	istore_0
Label4:
	iload_0
	bipush 10
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	getstatic MCClass.a I
	iconst_2
	imul
	putstatic MCClass.a I
	goto Label2
Label3:
	getstatic MCClass.a I
	invokestatic io/putIntLn(I)V
	invokestatic MCClass/foo()V
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label7 to Label8
Label7:
	invokestatic MCClass/testFor()V
Label8:
	return
.limit stack 0
.limit locals 1
.end method

.method public static foo()V
Label9:
.var 0 is a I from Label9 to Label10
.var 1 is f F from Label9 to Label10
	iconst_1
	ineg
	iconst_2
	imul
	iconst_3
	imul
	i2f
	fstore_1
	bipush 9
	istore_0
	goto Label13
Label11:
	iload_0
	iconst_1
	iadd
	istore_0
Label13:
	fload_1
	bipush 11
	i2f
	fcmpl
	ifgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
Label16:
	iload_0
	invokestatic io/putIntLn(I)V
	fload_1
	iconst_2
	ineg
	i2f
	fmul
	fstore_1
Label17:
	goto Label11
Label12:
Label10:
	return
.limit stack 6
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
