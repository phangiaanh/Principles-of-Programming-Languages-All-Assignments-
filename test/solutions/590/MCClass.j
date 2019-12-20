.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static s [Ljava/lang/String;

.method public static reverse([Ljava/lang/String;I)V
Label0:
.var 0 is s [Ljava/lang/String; from Label0 to Label1
.var 1 is size I from Label0 to Label1
.var 2 is max I from Label0 to Label1
.var 3 is i I from Label0 to Label1
	iconst_2
	istore_2
	iconst_0
	dup
	istore_3
	pop
	goto Label4
Label2:
	iload_3
	iconst_1
	iadd
	dup
	istore_3
	pop
Label4:
	iload_3
	iload_2
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
.var 4 is temp Ljava/lang/String; from Label7 to Label8
	aload_0
	iload_3
	aaload
	astore 4
	aload_0
	iload_3
	aload_0
	iload_1
	iload_3
	isub
	iconst_1
	isub
	aaload
	aastore
	aload_0
	iload_1
	iload_3
	isub
	iconst_1
	isub
	aload 4
	aastore
Label8:
	goto Label2
Label3:
	iconst_0
	dup
	istore_3
	pop
	goto Label11
Label9:
	iload_3
	iconst_1
	iadd
	dup
	istore_3
	pop
Label11:
	iload_3
	iload_1
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	aload_0
	iload_3
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
Label15:
	goto Label9
Label10:
Label1:
	return
.limit stack 14
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label16 to Label17
Label16:
	getstatic MCClass.s [Ljava/lang/String;
	iconst_0
	ldc "R"
	aastore
	getstatic MCClass.s [Ljava/lang/String;
	iconst_1
	ldc "E"
	aastore
	getstatic MCClass.s [Ljava/lang/String;
	iconst_2
	ldc "D"
	aastore
	getstatic MCClass.s [Ljava/lang/String;
	iconst_3
	ldc "R"
	aastore
	getstatic MCClass.s [Ljava/lang/String;
	iconst_4
	ldc "U"
	aastore
	getstatic MCClass.s [Ljava/lang/String;
	iconst_5
	ldc "M"
	aastore
	getstatic MCClass.s [Ljava/lang/String;
	bipush 6
	invokestatic MCClass/reverse([Ljava/lang/String;I)V
Label17:
	return
.limit stack 22
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
	bipush 6
	anewarray java/lang/String
	putstatic MCClass.s [Ljava/lang/String;
Label1:
	return
.limit stack 1
.limit locals 0
.end method
