.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	bipush 10
	newarray int
	astore_1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
.var 4 is k I from Label0 to Label1
	iconst_0
	istore_2
	goto Label4
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
Label4:
	iload_2
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	aload_1
	iload_2
	iload_2
	iastore
	goto Label2
Label3:
	iconst_0
	istore_3
	goto Label9
Label7:
	iload_3
	iconst_1
	iadd
	istore_3
Label9:
	iload_3
	bipush 10
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label8
	aload_1
	iload_3
	iaload
	invokestatic io/putInt(I)V
	goto Label7
Label8:
	bipush 9
	istore 4
	goto Label14
Label12:
	iload 4
	iconst_1
	isub
	istore 4
Label14:
	iload 4
	iconst_0
	if_icmplt Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label13
	aload_1
	iload 4
	iaload
	i2f
	invokestatic io/putFloat(F)V
	goto Label12
Label13:
Label1:
	return
.limit stack 8
.limit locals 5
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
