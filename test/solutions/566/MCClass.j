.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	goto Label4
Label2:
	getstatic MCClass.a I
	iconst_1
	iadd
	dup
	putstatic MCClass.a I
	pop
Label4:
	getstatic MCClass.a I
	bipush 6
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	invokestatic MCClass/True()Z
	getstatic MCClass.a I
	iconst_4
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	iand
	ifgt Label11
Label13:
	ldc "Stop"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label3
Label14:
	goto Label12
Label11:
Label15:
	getstatic MCClass.a I
	invokestatic io/putInt(I)V
	goto Label2
Label16:
Label12:
Label8:
	goto Label2
Label3:
Label1:
	return
.limit stack 8
.limit locals 1
.end method

.method public static True()Z
Label17:
	iconst_1
	goto Label18
Label18:
	ireturn
.limit stack 8
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

.method public static <clinit>()V
Label0:
	bipush 99
	newarray int
	putstatic MCClass.b [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
