.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is number F from Label0 to Label1
.var 3 is sum F from Label0 to Label1
	ldc 0.0
	fstore_3
	iconst_5
	istore_1
	goto Label4
Label2:
	iload_1
	iconst_1
	isub
	istore_1
Label4:
	iload_1
	iconst_5
	ineg
	if_icmplt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	ldc "Enter a n:"
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	iconst_2
	isub
	i2f
	fstore_2
	fload_2
	ldc 0.0
	fcmpl
	ifge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
	goto Label12
Label11:
Label13:
	goto Label3
Label14:
Label12:
	fload_3
	fload_2
	fadd
	fstore_3
Label8:
	goto Label2
Label3:
	ldc "sum = "
	invokestatic io/putString(Ljava/lang/String;)V
	fload_3
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 6
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
