.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static b Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_1
	iand
	iconst_0
	ior
	iconst_0
	ior
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	putstatic MCClass.b Z
	getstatic MCClass.b Z
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 24
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
