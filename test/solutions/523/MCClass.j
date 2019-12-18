.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I

.method public static cmpGE(II)Z
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	goto Label1
Label1:
	ireturn
.limit stack 3
.limit locals 2
.end method

.method public static cmpLE(II)Z
.var 0 is a I from Label4 to Label5
.var 1 is b I from Label4 to Label5
Label4:
	iload_0
	iload_1
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	goto Label5
Label5:
	ireturn
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label8 to Label9
Label8:
	iconst_5
	putstatic MCClass.i I
Label10:
Label12:
	ldc "Just for fun\n"
	invokestatic io/putString(Ljava/lang/String;)V
Label13:
	getstatic MCClass.i I
	iconst_5
	iconst_1
	iadd
	iconst_2
	iadd
	iconst_3
	iadd
	iconst_4
	iadd
	iconst_5
	iadd
	bipush 6
	iadd
	if_icmplt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label11
	goto Label10
Label11:
	iconst_1
	iconst_2
	imul
	iconst_3
	imul
	iconst_4
	imul
	iconst_5
	imul
	bipush 6
	imul
	bipush 7
	imul
	bipush 8
	imul
	bipush 9
	imul
	getstatic MCClass.i I
	bipush 6
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	bipush 6
	bipush 6
	invokestatic MCClass/cmpGE(II)Z
	invokestatic io/putBoolLn(Z)V
	bipush 6
	bipush 6
	invokestatic MCClass/cmpGE(II)Z
	invokestatic io/putBoolLn(Z)V
Label9:
	return
.limit stack 8
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
