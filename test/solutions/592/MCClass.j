.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 36
	bipush 6
	bipush 17
	imul
	invokestatic MCClass/GCD(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static GCD(II)I
Label2:
.var 0 is a I from Label2 to Label3
.var 1 is b I from Label2 to Label3
	iload_0
	iload_1
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
Label8:
	iload_1
	iload_0
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	iload_0
	iload_1
	isub
	iload_1
	invokestatic MCClass/GCD(II)I
	goto Label3
	goto Label13
Label12:
	iload_0
	iload_1
	iload_0
	isub
	invokestatic MCClass/GCD(II)I
	goto Label3
Label13:
Label9:
	goto Label7
Label6:
	iload_0
	goto Label3
Label7:
Label3:
	ireturn
.limit stack 8
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
