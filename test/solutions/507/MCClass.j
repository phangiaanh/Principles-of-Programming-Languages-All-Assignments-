.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static checkPrime(I)Z
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iload_0
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	iconst_0
	goto Label1
Label5:
	iconst_2
	istore_1
	goto Label8
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
Label8:
	iload_1
	iload_0
	iconst_1
	isub
	if_icmpgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label7
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label13
	goto Label14
Label13:
	iconst_0
	goto Label1
Label14:
	goto Label6
Label7:
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 12
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label15 to Label16
Label15:
	iconst_1
	iconst_0
	iconst_1
	iand
	iconst_0
	iand
	ior
	invokestatic io/putBoolLn(Z)V
	iconst_1
	invokestatic MCClass/checkPrime(I)Z
	invokestatic io/putBool(Z)V
	iconst_2
	invokestatic MCClass/checkPrime(I)Z
	invokestatic io/putBool(Z)V
	iconst_3
	invokestatic MCClass/checkPrime(I)Z
	invokestatic io/putBool(Z)V
	iconst_4
	invokestatic MCClass/checkPrime(I)Z
	invokestatic io/putBool(Z)V
	iconst_5
	invokestatic MCClass/checkPrime(I)Z
	invokestatic io/putBool(Z)V
Label16:
	return
.limit stack 18
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
