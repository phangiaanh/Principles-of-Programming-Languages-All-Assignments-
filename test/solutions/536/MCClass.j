.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I

.method public static enter([I)I
Label0:
.var 0 is a [I from Label0 to Label1
	aload_0
	iconst_0
	iaload
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
.var 1 is a [I from Label2 to Label3
	bipush 9
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_1
	iastore
	aload_1
	invokestatic MCClass/enter([I)I
	ineg
	ineg
	ineg
	ineg
	ineg
	i2f
	invokestatic io/putFloat(F)V
Label3:
	return
.limit stack 5
.limit locals 2
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
