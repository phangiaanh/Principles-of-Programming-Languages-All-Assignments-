.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static checkBool(Z)Z
.var 0 is bool Z from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
	goto Label4
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
Label4:
	iload_1
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_0
	invokestatic io/putBoolLn(Z)V
	iload_0
	ifgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	istore_0
Label8:
	goto Label2
Label3:
	iload_0
	goto Label1
Label1:
	ireturn
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label11 to Label12
Label11:
	iconst_1
	invokestatic MCClass/checkBool(Z)Z
	invokestatic io/putBool(Z)V
Label12:
	return
.limit stack 7
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
