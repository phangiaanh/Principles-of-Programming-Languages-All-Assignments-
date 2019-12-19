.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	dup
	putstatic MCClass.i I
	pop
	goto Label4
Label2:
	getstatic MCClass.i I
	iconst_1
	isub
	dup
	putstatic MCClass.i I
	pop
Label4:
	getstatic MCClass.i I
	iconst_5
	if_icmplt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	getstatic MCClass.i I
	ineg
	iconst_2
	imul
	invokestatic io/putIntLn(I)V
	goto Label2
Label3:
	bipush 10
	dup
	putstatic MCClass.i I
	pop
	goto Label9
Label7:
	getstatic MCClass.i I
	iconst_1
	isub
	dup
	putstatic MCClass.i I
	pop
Label9:
	getstatic MCClass.i I
	iconst_5
	if_icmplt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label8
	getstatic MCClass.i I
	iconst_2
	imul
	bipush 7
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	invokestatic io/putBoolLn(Z)V
	goto Label7
Label8:
Label1:
	return
.limit stack 14
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
