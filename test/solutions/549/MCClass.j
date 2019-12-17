.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static result I
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MCClass.result I
	iconst_0
	putstatic MCClass.i I
	goto Label4
Label2:
	getstatic MCClass.i I
	iconst_1
	iadd
	putstatic MCClass.i I
Label4:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	getstatic MCClass.i I
	iconst_5
	if_icmpne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label9
	getstatic MCClass.result I
	iconst_1
	iadd
	putstatic MCClass.result I
	goto Label10
Label9:
	goto Label3
Label10:
	goto Label2
Label3:
	getstatic MCClass.result I
	invokestatic io/putInt(I)V
	invokestatic io/putLn()V
Label1:
	return
.limit stack 6
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
