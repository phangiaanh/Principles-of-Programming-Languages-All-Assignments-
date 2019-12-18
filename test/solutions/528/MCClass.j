.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a F
.field static b Z

.method public static check()V
Label0:
.var 0 is a [I from Label0 to Label1
	bipush 10
	newarray int
	astore_0
	aload_0
	iconst_1
	iconst_2
	ineg
	ineg
	iastore
	aload_0
	iconst_3
	iconst_1
	ineg
	ineg
	ineg
	ineg
	iastore
	aload_0
	iconst_2
	bipush 6
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	iastore
	aload_0
	aload_0
	aload_0
	iconst_3
	iconst_1
	isub
	iconst_1
	iconst_1
	imul
	iconst_1
	idiv
	iadd
	iaload
	iaload
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 6
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	iconst_1
	ineg
	ineg
	ineg
	ineg
	iconst_2
	ineg
	isub
	i2f
	putstatic MCClass.a F
	getstatic MCClass.a F
	invokestatic io/putFloatLn(F)V
	iconst_1
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iconst_0
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ior
	putstatic MCClass.b Z
	getstatic MCClass.b Z
	invokestatic io/putBoolLn(Z)V
	invokestatic MCClass/check()V
Label3:
	return
.limit stack 10
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
