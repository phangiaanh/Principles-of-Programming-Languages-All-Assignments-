.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	invokestatic MCClass/foo()[I
	iconst_1
	iaload
	istore_1
	invokestatic MCClass/foo()[I
	iconst_1
	iconst_5
	ineg
	pop
	iload_1
	i2f
	invokestatic io/putFloat(F)V
	invokestatic MCClass/foo()[I
	iconst_1
	iaload
	i2f
	invokestatic io/putFloat(F)V
.var 2 is c Ljava/lang/String; from Label0 to Label1
	invokestatic MCClass/foo2()[Ljava/lang/String;
	iconst_1
	aaload
	astore_2
	invokestatic MCClass/foo2()[Ljava/lang/String;
	iconst_1
	ldc "Fool"
	pop
	aload_2
	invokestatic io/putString(Ljava/lang/String;)V
	invokestatic MCClass/foo2()[Ljava/lang/String;
	iconst_1
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 12
.limit locals 3
.end method

.method public static foo()[I
Label2:
.var 0 is a [I from Label2 to Label3
	bipush 10
	newarray int
	astore_0
	aload_0
	iconst_1
	iconst_5
	ineg
	iconst_5
	imul
	iastore
	aload_0
	goto Label3
Label3:
	areturn
.limit stack 16
.limit locals 1
.end method

.method public static foo2()[Ljava/lang/String;
Label4:
.var 0 is a [Ljava/lang/String; from Label4 to Label5
	bipush 10
	anewarray java/lang/String
	astore_0
	aload_0
	iconst_1
	ldc "Anh"
	aastore
	aload_0
	goto Label5
Label5:
	areturn
.limit stack 16
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
