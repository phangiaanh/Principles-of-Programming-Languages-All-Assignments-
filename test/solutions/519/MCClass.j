.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a0 [I
.field static b0 [Z
.field static c0 [Ljava/lang/String;
.field static d0 [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
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
	iconst_0
	newarray int
	putstatic MCClass.a0 [I
	iconst_0
	newarray boolean
	putstatic MCClass.b0 [Z
	iconst_0
	anewarray java/lang/String
	putstatic MCClass.c0 [Ljava/lang/String;
	iconst_0
	newarray float
	putstatic MCClass.d0 [F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
