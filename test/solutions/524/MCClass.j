.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I

.method public static cmple(II)Z
Label0:
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
	iload_0
	iload_1
	if_icmpgt Label2
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

.method public static cmpge(II)Z
Label4:
.var 0 is a I from Label4 to Label5
.var 1 is b I from Label4 to Label5
	iload_0
	iload_1
	if_icmplt Label6
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
	ldc "Good job\n"
	invokestatic io/putString(Ljava/lang/String;)V
	getstatic MCClass.i I
	iconst_1
	isub
	putstatic MCClass.i I
Label13:
	getstatic MCClass.i I
	iconst_3
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
	idiv
	iconst_3
	idiv
	iconst_4
	idiv
	iconst_5
	idiv
	bipush 6
	idiv
	bipush 7
	idiv
	bipush 8
	idiv
	bipush 9
	idiv
	pop
	bipush 6
	bipush 6
	invokestatic MCClass/cmple(II)Z
	invokestatic io/putBoolLn(Z)V
	bipush 6
	bipush 6
	invokestatic MCClass/cmpge(II)Z
	invokestatic io/putBoolLn(Z)V
Label9:
	return
.limit stack 10
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
