.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static result I
.field static i I

.method public static setup()V
Label0:
	iconst_0
	putstatic MCClass.result I
	iconst_0
	putstatic MCClass.i I
Label1:
	return
.limit stack 4
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	invokestatic MCClass/setup()V
	goto Label6
Label4:
	getstatic MCClass.i I
	iconst_1
	iadd
	dup
	putstatic MCClass.i I
	pop
Label6:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
	getstatic MCClass.i I
	iconst_5
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
	getstatic MCClass.result I
	getstatic MCClass.i I
	imul
	putstatic MCClass.result I
	goto Label12
Label11:
	goto Label5
Label12:
	goto Label4
Label5:
	getstatic MCClass.result I
	invokestatic io/putInt(I)V
	invokestatic io/putLn()V
Label3:
	return
.limit stack 12
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
