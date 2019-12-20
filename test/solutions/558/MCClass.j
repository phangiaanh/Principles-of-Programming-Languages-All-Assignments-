.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label2:
Label4:
	ldc "Still looping"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label5:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	iconst_5
	iconst_2
	imul
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	goto Label2
Label3:
	ldc "Out of loop"
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
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
