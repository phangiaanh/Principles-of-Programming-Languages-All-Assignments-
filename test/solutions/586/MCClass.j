.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static first I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	dup
	putstatic MCClass.first I
	pop
	goto Label4
Label2:
	getstatic MCClass.first I
	iconst_1
	iadd
	dup
	putstatic MCClass.first I
	pop
Label4:
	getstatic MCClass.first I
	bipush 7
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	invokestatic MCClass/array()[I
	pop
Label8:
	goto Label2
Label3:
	iconst_0
	dup
	putstatic MCClass.first I
	pop
	goto Label11
Label9:
	getstatic MCClass.first I
	iconst_1
	iadd
	dup
	putstatic MCClass.first I
	pop
Label11:
	getstatic MCClass.first I
	iconst_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	invokestatic MCClass/array()[I
	getstatic MCClass.first I
	iaload
	invokestatic io/putInt(I)V
Label15:
	goto Label9
Label10:
Label1:
	return
.limit stack 10
.limit locals 1
.end method

.method public static array()[I
Label16:
.var 0 is input [I from Label16 to Label17
	iconst_3
	newarray int
	astore_0
	aload_0
	iconst_0
	iconst_0
	iastore
	aload_0
	iconst_1
	iconst_1
	iastore
	aload_0
	iconst_2
	iconst_2
	iastore
	aload_0
	goto Label17
Label17:
	areturn
.limit stack 15
.limit locals 1
.end method

.method public static num()I
Label18:
	getstatic MCClass.first I
	iconst_1
	iadd
	goto Label19
Label19:
	ireturn
.limit stack 13
.limit locals 0
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
