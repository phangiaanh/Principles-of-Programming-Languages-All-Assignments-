.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
Label2:
	iconst_3
	istore_1
Label3:
.var 2 is b I from Label0 to Label1
.var 3 is c F from Label0 to Label1
.var 4 is d Z from Label0 to Label1
.var 5 is e Ljava/lang/String; from Label0 to Label1
	iload_1
	invokestatic io/putInt(I)V
	iconst_0
	istore_2
	goto Label6
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
Label6:
	iload_2
	bipush 30
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
	iload_2
	invokestatic io/putIntLn(I)V
	goto Label4
Label5:
Label1:
	return
.limit stack 3
.limit locals 6
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
	bipush 69
	newarray int
	putstatic MCClass.a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
