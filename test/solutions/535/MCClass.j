.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I
.field static j I
.field static l I
.field static a [I
.field static mul I

.method public static returnArray()[I
Label0:
.var 0 is a [I from Label0 to Label1
	bipush 11
	newarray int
	astore_0
	iconst_0
	dup
	putstatic MCClass.j I
	pop
	goto Label4
Label2:
	getstatic MCClass.j I
	iconst_1
	iadd
	dup
	putstatic MCClass.j I
	pop
Label4:
	getstatic MCClass.j I
	getstatic MCClass.l I
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	aload_0
	getstatic MCClass.j I
	getstatic MCClass.j I
	iconst_1
	iadd
	iastore
	goto Label2
Label3:
	aload_0
	goto Label1
Label1:
	areturn
.limit stack 10
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label7 to Label8
Label7:
	bipush 10
	putstatic MCClass.l I
	iconst_1
	putstatic MCClass.mul I
	iconst_0
	dup
	putstatic MCClass.i I
	pop
	goto Label11
Label9:
	getstatic MCClass.i I
	iconst_1
	iadd
	dup
	putstatic MCClass.i I
	pop
Label11:
	getstatic MCClass.i I
	getstatic MCClass.l I
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
	getstatic MCClass.mul I
	invokestatic MCClass/returnArray()[I
	getstatic MCClass.i I
	iaload
	imul
	putstatic MCClass.mul I
	goto Label9
Label10:
	getstatic MCClass.mul I
	invokestatic io/putIntLn(I)V
Label8:
	return
.limit stack 16
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
	newarray int
	putstatic MCClass.a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
