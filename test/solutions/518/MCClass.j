.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a I from Label2 to Label3
Label3:
.var 1 is b I from Label0 to Label1
.var 2 is c F from Label0 to Label1
.var 3 is d Z from Label0 to Label1
.var 4 is e Ljava/lang/String; from Label0 to Label1
	iconst_0
	istore_1
	goto Label6
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
Label6:
	iload_1
	bipush 30
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
	iload_1
	invokestatic io/putIntLn(I)V
	goto Label4
Label5:
Label1:
	return
.limit stack 3
.limit locals 5
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
	bipush 30
	newarray int
	putstatic MCClass.a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
