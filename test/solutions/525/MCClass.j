.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static tmp I
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MCClass.tmp I
	iconst_0
	dup
	putstatic MCClass.i I
	pop
	goto Label4
Label2:
	getstatic MCClass.i I
	iconst_1
	iadd
	dup
	putstatic MCClass.i I
	pop
Label4:
	getstatic MCClass.i I
	sipush 2019
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	getstatic MCClass.tmp I
	iconst_5
	imul
	bipush 13
	irem
	putstatic MCClass.tmp I
	goto Label2
Label3:
	getstatic MCClass.tmp I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 9
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
