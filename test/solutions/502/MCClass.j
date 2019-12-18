.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static getTwoInt(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iconst_2
	iconst_3
	iconst_5
	imul
	iconst_2
	idiv
	iadd
	iconst_3
	isub
	invokestatic io/putInt(I)V
	iconst_2
	iload_0
	imul
	iconst_3
	iadd
	invokestatic io/putInt(I)V
	iload_0
	iconst_1
	iadd
	goto Label1
Label1:
	ireturn
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	iconst_2
	invokestatic MCClass/getTwoInt(I)I
	invokestatic io/putInt(I)V
Label3:
	return
.limit stack 1
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
