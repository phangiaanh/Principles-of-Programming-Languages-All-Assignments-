.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static returnArray()[I
Label0:
.var 0 is i I from Label0 to Label1
.var 1 is a [I from Label0 to Label1
	bipush 10
	newarray int
	astore_1
	iconst_0
	istore_0
	goto Label4
Label2:
	iload_0
	iconst_1
	iadd
	istore_0
Label4:
	iload_0
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	aload_1
	iload_0
	iload_0
	iastore
	goto Label2
Label3:
	aload_1
	goto Label1
Label1:
	areturn
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label7 to Label8
Label7:
.var 1 is b [I from Label7 to Label8
	bipush 10
	newarray int
	astore_1
	invokestatic MCClass/returnArray()[I
	bipush 9
	iaload
	invokestatic io/putIntLn(I)V
Label8:
	return
.limit stack 4
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