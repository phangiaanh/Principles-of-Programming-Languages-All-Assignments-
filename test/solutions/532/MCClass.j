.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [Ljava/lang/String; from Label0 to Label1
	bipush 10
	anewarray java/lang/String
	astore_1
.var 2 is b [Ljava/lang/String; from Label0 to Label1
	bipush 10
	anewarray java/lang/String
	astore_2
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
	aload_1
	getstatic MCClass.i I
	ldc "a"
	aastore
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
	aload_2
	getstatic MCClass.i I
	aload_1
	getstatic MCClass.i I
	aaload
	aastore
	goto Label7
Label8:
Label12:
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
	aload_2
	getstatic MCClass.i I
	ldc "c"
	aastore
	goto Label14
Label15:
Label13:
	iconst_0
	putstatic MCClass.i I
	goto Label21
Label19:
	getstatic MCClass.i I
	iconst_1
	iadd
	putstatic MCClass.i I
Label21:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label20
	aload_1
	getstatic MCClass.i I
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label19
Label20:
	iconst_0
	putstatic MCClass.i I
	goto Label26
Label24:
	getstatic MCClass.i I
	iconst_1
	iadd
	putstatic MCClass.i I
Label26:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label27
	iconst_1
	goto Label28
Label27:
	iconst_0
Label28:
	ifle Label25
	aload_2
	getstatic MCClass.i I
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label24
Label25:
Label1:
	return
.limit stack 12
.limit locals 3
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
