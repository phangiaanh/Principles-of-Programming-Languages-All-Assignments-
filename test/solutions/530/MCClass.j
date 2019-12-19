.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I
.field static a [I
.field static b Z

.method public static setup()V
Label0:
	iconst_0
	dup
	putstatic MCClass.i I
	pop
	goto Label4
Label2:
	getstatic MCClass.i I
	iconst_1
	iadd
	dup
	putstatic MCClass.i I
	pop
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
.limit stack 9
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label7 to Label8
Label7:
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
	bipush 10
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	getstatic MCClass.a [I
	getstatic MCClass.i I
	iaload
	iconst_5
	if_icmple Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label18
	goto Label19
Label18:
	getstatic MCClass.b Z
	ifgt Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	putstatic MCClass.b Z
Label19:
Label15:
	goto Label9
Label10:
	getstatic MCClass.b Z
	invokestatic io/putBoolLn(Z)V
Label8:
	return
.limit stack 23
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
