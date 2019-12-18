.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [I
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MCClass.i I
	goto Label4
Label2:
	getstatic MCClass.i I
	iconst_2
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
	getstatic MCClass.a [I
	getstatic MCClass.i I
	getstatic MCClass.i I
	getstatic MCClass.i I
	imul
	bipush 50
	irem
	iastore
	goto Label2
Label3:
	iconst_0
	putstatic MCClass.i I
	goto Label9
Label7:
	getstatic MCClass.i I
	iconst_1
	iadd
	putstatic MCClass.i I
Label9:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label8
	getstatic MCClass.a [I
	getstatic MCClass.i I
	iaload
	invokestatic io/putIntLn(I)V
	goto Label7
Label8:
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

.method public static <clinit>()V
Label0:
	bipush 100
	newarray int
	putstatic MCClass.a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
