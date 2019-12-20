.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
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
	iconst_0
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	goto Label1
Label8:
	goto Label2
Label3:
	iconst_1
	invokestatic io/putInt(I)V
	iconst_1
	i2f
	invokestatic io/putFloat(F)V
	iconst_1
	invokestatic io/putBool(Z)V
	ldc "Yeah"
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
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
