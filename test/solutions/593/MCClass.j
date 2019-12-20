.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	iconst_5
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_3
	iastore
	aload_1
	iconst_1
	bipush 6
	iastore
	aload_1
	iconst_2
	bipush 7
	iastore
	aload_1
	iconst_3
	bipush 14
	iastore
	aload_1
	iconst_4
	iconst_2
	iastore
	aload_1
	iconst_5
	invokestatic MCClass/mulGCD([II)V
Label1:
	return
.limit stack 9
.limit locals 2
.end method

.method public static mulGCD([II)V
Label2:
.var 0 is a [I from Label2 to Label3
.var 1 is size I from Label2 to Label3
.var 2 is mul I from Label2 to Label3
	iconst_1
	istore_2
.var 3 is i I from Label2 to Label3
	iconst_0
	dup
	istore_3
	pop
	goto Label6
Label4:
	iload_3
	iconst_1
	iadd
	dup
	istore_3
	pop
Label6:
	iload_3
	iload_1
	iconst_1
	isub
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	iload_2
	aload_0
	iload_3
	iaload
	aload_0
	iload_3
	iconst_1
	iadd
	iaload
	invokestatic MCClass/GCD(II)I
	imul
	istore_2
Label10:
	goto Label4
Label5:
	iload_2
	invokestatic io/putInt(I)V
Label3:
	return
.limit stack 17
.limit locals 4
.end method

.method public static GCD(II)I
Label11:
.var 0 is a I from Label11 to Label12
.var 1 is b I from Label11 to Label12
	iload_0
	iload_1
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifgt Label15
Label17:
	iload_1
	iload_0
	if_icmple Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifgt Label21
	iload_0
	iload_1
	isub
	iload_1
	invokestatic MCClass/GCD(II)I
	goto Label12
	goto Label22
Label21:
	iload_0
	iload_1
	iload_0
	isub
	invokestatic MCClass/GCD(II)I
	goto Label12
Label22:
Label18:
	goto Label16
Label15:
	iload_0
	goto Label12
Label16:
Label12:
	ireturn
.limit stack 19
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
