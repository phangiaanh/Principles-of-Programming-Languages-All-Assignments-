.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [Ljava/lang/String;
.field static b Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
	goto Label4
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
Label4:
	iload_1
	iconst_5
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	getstatic MCClass.a [Ljava/lang/String;
	iload_1
	ldc "1"
	aastore
	goto Label2
Label3:
	iconst_0
	istore_1
	goto Label9
Label7:
	iload_1
	iconst_1
	iadd
	istore_1
Label9:
	iload_1
	iconst_5
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label8
	getstatic MCClass.a [Ljava/lang/String;
	iload_1
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label7
Label8:
	getstatic MCClass.a [Ljava/lang/String;
	iconst_4
	aaload
	putstatic MCClass.b Ljava/lang/String;
	getstatic MCClass.b Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
.limit locals 2
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
	bipush 30
	anewarray java/lang/String
	putstatic MCClass.a [Ljava/lang/String;
Label1:
	return
.limit stack 1
.limit locals 0
.end method
