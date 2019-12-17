.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i [I
.field static f [F
.field static b [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass.i [I
	iconst_2
	iaload
	invokestatic io/putInt(I)V
	getstatic MCClass.f [F
	iconst_3
	faload
	invokestatic io/putFloat(F)V
	getstatic MCClass.b [Z
	iconst_4
	baload
	invokestatic io/putBool(Z)V
Label1:
	return
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

.method public static <clinit>()V
Label0:
	bipush 10
	newarray int
	putstatic MCClass.i [I
	bipush 100
	newarray float
	putstatic MCClass.f [F
	sipush 1000
	newarray boolean
	putstatic MCClass.b [Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
