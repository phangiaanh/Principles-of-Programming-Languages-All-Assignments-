.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
	iconst_1
	istore_1
	iconst_3
	istore_2
	ldc "Enter a number: "
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label2:
Label4:
	ldc "This number = "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	iconst_1
	iadd
	dup
	istore_2
	istore_1
Label5:
Label6:
	iload_2
	invokestatic io/putInt(I)V
Label7:
	iload_1
	iconst_5
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	goto Label2
Label3:
Label1:
	return
.limit stack 10
.limit locals 3
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
