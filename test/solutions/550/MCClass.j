.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is flag I from Label0 to Label1
	iconst_0
	istore_3
	ldc "Enter a positive integer: "
	invokestatic io/putStringLn(Ljava/lang/String;)V
	bipush 13
	istore_1
	iconst_2
	istore_2
	goto Label4
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
Label4:
	iload_2
	iload_1
	iconst_2
	idiv
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_1
	iload_2
	irem
	iconst_0
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
	goto Label12
Label11:
Label13:
	iconst_1
	istore_3
	goto Label3
Label14:
Label12:
Label8:
	goto Label2
Label3:
	iload_1
	iconst_1
	if_icmpne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifgt Label17
Label19:
	iload_3
	iconst_0
	if_icmpne Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifgt Label23
Label25:
	iload_1
	invokestatic io/putInt(I)V
	ldc " is not a prime number."
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label26:
	goto Label24
Label23:
Label27:
	iload_1
	invokestatic io/putInt(I)V
	ldc " is a prime number."
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label28:
Label24:
Label20:
	goto Label18
Label17:
Label29:
	ldc "1 is neither prime nor composite."
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label30:
Label18:
Label1:
	return
.limit stack 9
.limit locals 4
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
