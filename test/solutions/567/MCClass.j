.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "We have an array: "
	invokestatic io/putStringLn(Ljava/lang/String;)V
	goto Label4
Label2:
	getstatic MCClass.i I
	iconst_1
	iadd
	dup
	putstatic MCClass.i I
	pop
Label4:
	getstatic MCClass.i I
	bipush 15
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	getstatic MCClass.arr [I
	getstatic MCClass.i I
	getstatic MCClass.i I
	iastore
	getstatic MCClass.i I
	iconst_2
	irem
	iconst_0
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
	goto Label12
Label11:
	goto Label2
Label12:
Label8:
	goto Label2
Label3:
	getstatic MCClass.arr [I
	getstatic MCClass.i I
	iconst_1
	isub
	iaload
	iconst_2
	irem
	iconst_0
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifgt Label15
Label17:
	ldc "It's odd"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label18:
	goto Label16
Label15:
Label19:
	ldc "It's even"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label20:
Label16:
Label1:
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

.method public static <clinit>()V
Label0:
	bipush 15
	newarray int
	putstatic MCClass.arr [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
