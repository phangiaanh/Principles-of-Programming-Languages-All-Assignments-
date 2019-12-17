.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I
.field static a [I
.field static b Ljava/lang/String;

.method public static setup()V
Label0:
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
	getstatic MCClass.a [I
	getstatic MCClass.i I
	getstatic MCClass.i I
	iastore
	goto Label2
Label3:
Label1:
	return
.limit stack 5
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label7 to Label8
Label7:
	ldc "--12"
	putstatic MCClass.b Ljava/lang/String;
	invokestatic MCClass/setup()V
	iconst_2
	putstatic MCClass.i I
	goto Label11
Label9:
	getstatic MCClass.i I
	iconst_1
	iadd
	putstatic MCClass.i I
Label11:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
	getstatic MCClass.a [I
	getstatic MCClass.i I
	getstatic MCClass.a [I
	getstatic MCClass.a [I
	getstatic MCClass.i I
	iconst_1
	isub
	iaload
	iconst_1
	ineg
	ineg
	imul
	iaload
	iastore
	goto Label9
Label10:
	iconst_0
	putstatic MCClass.i I
	goto Label16
Label14:
	getstatic MCClass.i I
	iconst_1
	iadd
	putstatic MCClass.i I
Label16:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label15
	getstatic MCClass.a [I
	getstatic MCClass.i I
	iaload
	invokestatic io/putIntLn(I)V
	goto Label14
Label15:
	getstatic MCClass.b Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label8:
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
	bipush 20
	newarray int
	putstatic MCClass.a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
