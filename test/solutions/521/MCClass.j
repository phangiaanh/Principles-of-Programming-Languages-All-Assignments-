.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.11
	iconst_2
	i2f
	fadd
	iconst_3
	i2f
	fadd
	ldc 1.0
	fadd
	ldc 1.1
	fadd
	ldc 1.2
	fadd
	ldc 1.3
	fadd
	putstatic MCClass.a F
	getstatic MCClass.a F
	bipush 10
	i2f
	fdiv
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 4
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
