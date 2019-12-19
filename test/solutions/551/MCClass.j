.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static n I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "Enter a number:"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	bipush 17
	putstatic MCClass.n I
	getstatic MCClass.n I
	invokestatic io/putInt(I)V
	getstatic MCClass.n I
	invokestatic MCClass/checkPrime(I)Z
	ifgt Label2
Label4:
	ldc " is not a prime number!"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label5:
	goto Label3
Label2:
Label6:
	ldc " is a prime number!"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label7:
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static checkPrime(I)Z
Label8:
.var 0 is n I from Label8 to Label9
.var 1 is i I from Label8 to Label9
	iconst_2
	istore_1
	goto Label12
Label10:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	pop
Label12:
	iload_1
	iload_0
	iconst_2
	idiv
	if_icmpge Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label11
Label15:
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpeq Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifgt Label19
	iconst_0
	goto Label9
	goto Label20
Label19:
	goto Label10
Label20:
Label16:
	goto Label10
Label11:
	iconst_1
	goto Label9
Label9:
	ireturn
.limit stack 12
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
