.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	putstatic MCClass.a I
	getstatic MCClass.a I
	iconst_1
	if_icmplt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	getstatic MCClass.a I
	iconst_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ior
	putstatic MCClass.b Z
	getstatic MCClass.b Z
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 17
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
