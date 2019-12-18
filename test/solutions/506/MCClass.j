.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static globalFloat F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	invokestatic io/putIntLn(I)V
	invokestatic MCClass/testFloat()V
	getstatic MCClass.globalFloat F
	iconst_2
	i2f
	fadd
	putstatic MCClass.globalFloat F
	invokestatic MCClass/testFloat()V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static testFloat()V
Label2:
	getstatic MCClass.globalFloat F
	invokestatic io/putFloatLn(F)V
Label3:
	return
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
