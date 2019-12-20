.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [I
.field static global Z

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
.var 2 is x I from Label0 to Label1
Label2:
.var 3 is x Ljava/lang/String; from Label2 to Label3
Label4:
Label6:
Label8:
.var 4 is x Ljava/lang/String; from Label8 to Label9
Label10:
	ldc "OK"
	astore 4
Label11:
Label9:
Label7:
Label5:
	ldc "OK"
	astore_3
.var 4 is b Ljava/lang/String; from Label2 to Label3
	aload_3
	astore 4
	aload 4
	invokestatic io/putStringLn(Ljava/lang/String;)V
	getstatic MCClass.a [I
	invokestatic MCClass/check([I)I
	pop
Label3:
	goto Label1
Label1:
	return
.limit stack 7
.limit locals 5
.end method

.method public static check([I)I
Label12:
.var 0 is arr [I from Label12 to Label13
.var 1 is i I from Label12 to Label13
	iconst_0
	dup
	istore_1
	pop
	goto Label16
Label14:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	pop
Label16:
	iload_1
	bipush 10
	if_icmpge Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label15
Label19:
	aload_0
	iload_1
	iaload
	iconst_0
	if_icmpeq Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifgt Label23
	goto Label24
Label23:
Label25:
	ldc "Found a value!"
	invokestatic io/putString(Ljava/lang/String;)V
	iconst_1
	goto Label13
Label26:
Label24:
Label20:
	goto Label14
Label15:
	ldc "No value found!"
	invokestatic io/putString(Ljava/lang/String;)V
	iconst_0
	goto Label13
Label13:
	ireturn
.limit stack 13
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
