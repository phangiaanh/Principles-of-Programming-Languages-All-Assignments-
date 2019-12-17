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
.var 1 is a I from Label0 to Label1
	bipush 9
	istore_1
	goto Label9
Label7:
	iload_1
	iconst_1
	iadd
	istore_1
Label9:
	iconst_1
	ifle Label8
Label10:
	iload_1
	invokestatic io/putIntLn(I)V
	iload_1
	bipush 20
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	goto Label15
Label14:
	goto Label8
Label15:
Label11:
	goto Label7
Label8:
Label1:
	return
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label16 to Label17
Label16:
	invokestatic MCClass/testFor()V
Label17:
	return
.limit stack 0
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
