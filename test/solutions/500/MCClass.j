.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I
.field static a [Ljava/lang/String;
.field static b [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MCClass.i I
Label2:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	getstatic MCClass.a [Ljava/lang/String;
	getstatic MCClass.i I
	ldc "a"
	aastore
	getstatic MCClass.i I
	iconst_1
	iadd
	putstatic MCClass.i I
	goto Label2
Label3:
	iconst_0
	putstatic MCClass.i I
Label6:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	getstatic MCClass.b [Ljava/lang/String;
	getstatic MCClass.i I
	ldc "b"
	aastore
	getstatic MCClass.i I
	iconst_1
	iadd
	putstatic MCClass.i I
	goto Label6
Label7:
Label10:
	iconst_0
	putstatic MCClass.i I
Label12:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label13
	getstatic MCClass.b [Ljava/lang/String;
	getstatic MCClass.i I
	ldc "c"
	aastore
	getstatic MCClass.i I
	iconst_1
	iadd
	putstatic MCClass.i I
	goto Label12
Label13:
Label11:
	iconst_0
	putstatic MCClass.i I
Label16:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label17
	getstatic MCClass.a [Ljava/lang/String;
	getstatic MCClass.i I
	aaload
	invokestatic io/putStringLn(Ljava/lang/String;)V
	getstatic MCClass.i I
	iconst_1
	iadd
	putstatic MCClass.i I
	goto Label16
Label17:
	iconst_0
	putstatic MCClass.i I
Label20:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label21
	getstatic MCClass.b [Ljava/lang/String;
	getstatic MCClass.i I
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
	getstatic MCClass.i I
	iconst_1
	iadd
	putstatic MCClass.i I
	goto Label20
Label21:
Label1:
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

.method public static <clinit>()V
Label0:
	bipush 10
	anewarray java/lang/String
	putstatic MCClass.a [Ljava/lang/String;
	bipush 10
	anewarray java/lang/String
	putstatic MCClass.b [Ljava/lang/String;
Label1:
	return
.limit stack 1
.limit locals 0
.end method
