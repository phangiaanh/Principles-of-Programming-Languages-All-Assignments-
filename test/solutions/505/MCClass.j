.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static f F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	i2f
	putstatic MCClass.f F
	iconst_2
	invokestatic io/putIntLn(I)V
	getstatic MCClass.f F
	invokestatic MCClass/testFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static testFloat(F)V
.var 0 is f F from Label2 to Label3
Label2:
	fload_0
	invokestatic io/putFloatLn(F)V
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
