.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_5
	istore_1
	iload_1
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iload_1
	iconst_2
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	iconst_1
	invokestatic io/putBool(Z)V
	goto Label9
Label8:
	iconst_0
	invokestatic io/putBool(Z)V
Label9:
	goto Label5
Label4:
	iconst_1
	invokestatic io/putBool(Z)V
Label5:
Label1:
	return
.limit stack 8
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
