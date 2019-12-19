.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static testFor()I
Label0:
.var 0 is i I from Label0 to Label1
	iconst_0
	dup
	istore_0
	pop
	goto Label4
Label2:
	iload_0
	iconst_1
	iadd
	dup
	istore_0
	pop
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
Label7:
.var 1 is a I from Label7 to Label8
	iconst_1
	istore_1
	goto Label11
Label9:
Label11:
	iconst_1
	ifle Label10
Label12:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	invokestatic io/putIntLn(I)V
	iload_1
	bipush 10
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	goto Label17
Label16:
	goto Label10
Label17:
Label13:
	goto Label9
Label10:
Label8:
	getstatic MCClass.a I
	goto Label1
Label1:
	ireturn
.limit stack 13
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label18 to Label19
Label18:
	invokestatic MCClass/testFor()I
	invokestatic io/putIntLn(I)V
Label19:
	return
.limit stack 13
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
