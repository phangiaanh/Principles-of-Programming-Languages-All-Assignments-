.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass.arr [I
	invokestatic MCClass/getArr([I)[I
	iconst_0
	iaload
	i2f
	invokestatic io/putFloat(F)V
	iconst_3
	invokestatic MCClass/changeArr(I)V
	getstatic MCClass.arr [I
	invokestatic MCClass/getArr([I)[I
	iconst_0
	iaload
	i2f
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static getArr([I)[I
Label2:
.var 0 is arr [I from Label2 to Label3
	aload_0
	goto Label3
Label3:
	areturn
.limit stack 1
.limit locals 1
.end method

.method public static changeArr(I)V
Label4:
.var 0 is val I from Label4 to Label5
.var 1 is i I from Label4 to Label5
	iconst_0
	dup
	istore_1
	pop
	goto Label8
Label6:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	pop
Label8:
	iload_1
	bipush 9
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label7
Label11:
	getstatic MCClass.arr [I
	iload_1
	iload_0
	iastore
Label12:
	goto Label6
Label7:
Label5:
	return
.limit stack 9
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
	bipush 9
	newarray int
	putstatic MCClass.arr [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
