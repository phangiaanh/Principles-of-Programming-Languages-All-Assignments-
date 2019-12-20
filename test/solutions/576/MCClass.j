.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/one()I
	pop
	invokestatic MCClass/two()F
	pop
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static one()I
Label2:
	iconst_1
	goto Label3
Label3:
	ireturn
.limit stack 1
.limit locals 0
.end method

.method public static two()F
Label4:
	ldc 2.0
	goto Label5
Label5:
	freturn
.limit stack 1
.limit locals 0
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
