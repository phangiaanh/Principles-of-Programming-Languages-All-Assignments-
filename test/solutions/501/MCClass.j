.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static get()I
Label0:
	iconst_2
	iconst_3
	iadd
	invokestatic io/putInt(I)V
	iconst_3
	iconst_5
	iadd
	invokestatic io/putInt(I)V
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	invokestatic MCClass/get()I
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
