.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static result I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is a [I from Label0 to Label1
	bipush 10
	newarray int
	astore_2
.var 3 is b [I from Label0 to Label1
	bipush 10
	newarray int
	astore_3
.var 4 is c [I from Label0 to Label1
	bipush 10
	newarray int
	astore 4
	iconst_0
	dup
	istore_1
	pop
	goto Label4
Label2:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	pop
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
	aload_2
	iload_1
	iload_1
	iload_1
	imul
	iastore
	aload_2
	iload_1
	iaload
	invokestatic io/putInt(I)V
Label8:
	goto Label2
Label3:
	iconst_0
	dup
	istore_1
	pop
	goto Label11
Label9:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	pop
Label11:
	iload_1
	bipush 10
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	aload_3
	iload_1
	iconst_2
	iload_1
	imul
	iastore
	aload_3
	iload_1
	iaload
	invokestatic io/putInt(I)V
Label15:
	goto Label9
Label10:
	iconst_0
	dup
	istore_1
	pop
	goto Label18
Label16:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	pop
Label18:
	iload_1
	bipush 10
	if_icmpge Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label17
Label21:
	aload 4
	iload_1
	aload_2
	iload_1
	iaload
	aload_3
	iload_1
	iaload
	iadd
	iastore
	getstatic MCClass.result I
	aload 4
	iload_1
	iaload
	iadd
	putstatic MCClass.result I
Label22:
	goto Label16
Label17:
	getstatic MCClass.result I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 21
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
