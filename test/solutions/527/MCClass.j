.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b [I from Label0 to Label1
	bipush 99
	newarray int
	astore_1
	aload_1
	bipush 9
	iconst_1
	iastore
	aload_1
	aload_1
	bipush 9
	iaload
	iconst_1
	iadd
	iconst_2
	iadd
	iconst_3
	iadd
	iconst_4
	iadd
	iconst_5
	iadd
	iconst_1
	ineg
	ineg
	iastore
	aload_1
	bipush 17
	iconst_1
	isub
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
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

.method public static <clinit>()V
Label0:
	bipush 99
	newarray int
	putstatic MCClass.a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
