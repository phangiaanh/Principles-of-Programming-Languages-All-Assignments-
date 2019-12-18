.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static sqrt(I)I
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_1
	istore_1
	goto Label4
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
Label4:
	iload_1
	iload_0
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_1
	iload_1
	imul
	iload_0
	if_icmple Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
	goto Label12
Label11:
	iload_1
	goto Label1
Label12:
Label8:
	goto Label2
Label3:
	iload_1
	goto Label1
Label1:
	ireturn
.limit stack 6
.limit locals 2
.end method

.method public static checkPrime(I)Z
.var 0 is n I from Label13 to Label14
Label13:
.var 1 is i I from Label13 to Label14
	iload_0
	iconst_1
	if_icmpne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifgt Label17
	goto Label18
Label17:
	iconst_0
	goto Label14
Label18:
	iconst_2
	istore_1
	goto Label21
Label19:
	iload_1
	iconst_1
	iadd
	istore_1
Label21:
	iload_1
	iload_0
	invokestatic MCClass/sqrt(I)I
	if_icmpgt Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label20
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifgt Label26
	goto Label27
Label26:
	iconst_0
	goto Label14
Label27:
	goto Label19
Label20:
	iconst_1
	goto Label14
Label14:
	ireturn
.limit stack 17
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label28 to Label29
Label28:
	iconst_1
	invokestatic MCClass/checkPrime(I)Z
	invokestatic io/putBoolLn(Z)V
	bipush 21
	invokestatic MCClass/checkPrime(I)Z
	invokestatic io/putBoolLn(Z)V
	bipush 37
	invokestatic MCClass/checkPrime(I)Z
	invokestatic io/putBoolLn(Z)V
	bipush 47
	invokestatic MCClass/checkPrime(I)Z
	invokestatic io/putBoolLn(Z)V
	sipush 152
	invokestatic MCClass/checkPrime(I)Z
	invokestatic io/putBoolLn(Z)V
Label29:
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
