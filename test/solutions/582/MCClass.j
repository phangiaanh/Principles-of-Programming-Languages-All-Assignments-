.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	iconst_1
	istore_1
	getstatic MCClass.a [I
	iload_1
	iconst_1
	iadd
	iload_1
	iastore
	getstatic MCClass.a [I
	invokestatic MCClass/check([I)I
	pop
Label1:
	return
.limit stack 6
.limit locals 2
.end method

.method public static check([I)I
Label2:
.var 0 is arr [I from Label2 to Label3
.var 1 is i I from Label2 to Label3
	iconst_0
	dup
	istore_1
	pop
	goto Label6
Label4:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	pop
Label6:
	iload_1
	bipush 10
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	aload_0
	iload_1
	iaload
	iconst_0
	if_icmpeq Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label13
	goto Label14
Label13:
Label15:
	ldc "Found a value!"
	invokestatic io/putString(Ljava/lang/String;)V
	iconst_1
	goto Label3
Label16:
Label14:
Label10:
	goto Label4
Label5:
	ldc "No value found!"
	invokestatic io/putString(Ljava/lang/String;)V
	iconst_0
	goto Label3
Label3:
	ireturn
.limit stack 10
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
	bipush 10
	newarray int
	putstatic MCClass.a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
