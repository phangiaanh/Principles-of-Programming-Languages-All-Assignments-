.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static getThreeFloat(I)F
Label0:
.var 0 is _ I from Label0 to Label1
	iload_0
	iconst_1
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
Label6:
	iload_0
	bipush 10
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	ldc 2.0
	iconst_3
	i2f
	fdiv
	invokestatic io/putFloat(F)V
	goto Label11
Label10:
	ldc 5.5
	invokestatic io/putFloat(F)V
Label11:
Label7:
	goto Label5
Label4:
Label12:
	iload_0
	iconst_0
	if_icmplt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	iconst_1
	ineg
	i2f
	invokestatic io/putFloat(F)V
	goto Label17
Label16:
	ldc 1.5
	invokestatic io/putFloat(F)V
Label17:
Label13:
Label5:
	iload_0
	i2f
	goto Label1
Label1:
	freturn
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label18 to Label19
Label18:
	bipush 6
	invokestatic MCClass/getThreeFloat(I)F
	invokestatic io/putFloat(F)V
Label19:
	return
.limit stack 7
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
