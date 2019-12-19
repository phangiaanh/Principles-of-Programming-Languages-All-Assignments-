.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [I
.field static f [F

.method public static sum([II)I
Label0:
.var 0 is a [I from Label0 to Label1
.var 1 is l I from Label0 to Label1
.var 2 is temp I from Label0 to Label1
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_2
	iconst_0
	dup
	istore_3
	pop
	goto Label4
Label2:
	iload_3
	iconst_1
	iadd
	dup
	istore_3
	pop
Label4:
	iload_3
	iload_1
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	iload_2
	aload_0
	iload_3
	iaload
	iadd
	istore_2
	goto Label2
Label3:
	iload_2
	goto Label1
Label1:
	ireturn
.limit stack 10
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label7 to Label8
Label7:
	ldc "Test sum and mul:"
	invokestatic io/putStringLn(Ljava/lang/String;)V
.var 1 is i I from Label7 to Label8
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
	getstatic MCClass.a [I
	iload_1
	iload_1
	iastore
	goto Label9
Label10:
	iconst_0
	dup
	istore_1
	pop
	goto Label16
Label14:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	pop
Label16:
	iload_1
	bipush 10
	if_icmpge Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label15
	getstatic MCClass.f [F
	iload_1
	iload_1
	iconst_1
	iadd
	i2f
	fastore
	goto Label14
Label15:
	getstatic MCClass.a [I
	bipush 10
	invokestatic MCClass/sum([II)I
	invokestatic io/putIntLn(I)V
	getstatic MCClass.f [F
	bipush 10
	invokestatic MCClass/multiply([FI)F
	invokestatic io/putFloatLn(F)V
Label8:
	return
.limit stack 21
.limit locals 2
.end method

.method public static multiply([FI)F
Label19:
.var 0 is a [F from Label19 to Label20
.var 1 is l I from Label19 to Label20
.var 2 is temp F from Label19 to Label20
.var 3 is i I from Label19 to Label20
	iconst_1
	i2f
	fstore_2
	iconst_0
	dup
	istore_3
	pop
	goto Label23
Label21:
	iload_3
	iconst_1
	iadd
	dup
	istore_3
	pop
Label23:
	iload_3
	iload_1
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label22
	fload_2
	aload_0
	iload_3
	faload
	fmul
	fstore_2
	goto Label21
Label22:
	fload_2
	goto Label20
Label20:
	freturn
.limit stack 26
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

.method public static <clinit>()V
Label0:
	bipush 10
	newarray int
	putstatic MCClass.a [I
	bipush 10
	newarray float
	putstatic MCClass.f [F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
