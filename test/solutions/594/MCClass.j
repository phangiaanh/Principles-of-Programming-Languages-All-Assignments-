.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static binary(I)V
Label0:
.var 0 is n I from Label0 to Label1
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_0
	iconst_1
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	ifgt Label6
Label8:
	iload_0
	iconst_2
	idiv
	invokestatic MCClass/binary(I)V
	iload_0
	iconst_2
	irem
	invokestatic io/putInt(I)V
Label9:
	goto Label7
Label6:
	iload_0
	invokestatic io/putInt(I)V
Label7:
Label1:
	return
.limit stack 6
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label10 to Label11
Label10:
	bipush 54
	invokestatic MCClass/binary(I)V
Label11:
	return
.limit stack 5
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
