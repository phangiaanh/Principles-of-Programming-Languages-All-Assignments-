.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/getFloatLiteral()F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static getFloatLiteral()F
Label2:
.var 0 is m F from Label2 to Label3
	iconst_1
	i2f
	fstore_0
	iconst_1
	iconst_2
	isub
	i2f
	fstore_0
	fload_0
	goto Label3
Label3:
	freturn
.limit stack 2
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
