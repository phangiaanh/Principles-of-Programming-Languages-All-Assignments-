.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static compare(FI)Z
Label0:
.var 0 is a F from Label0 to Label1
.var 1 is b I from Label0 to Label1
	fload_0
	iload_1
	i2f
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iconst_0
	goto Label1
	goto Label5
Label4:
	iconst_1
	goto Label1
Label5:
Label1:
	ireturn
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label6 to Label7
Label6:
	ldc 5.2
	iconst_3
	invokestatic MCClass/compare(FI)Z
	ifgt Label8
	iconst_3
	i2f
	invokestatic io/putFloat(F)V
	goto Label9
Label8:
	iconst_2
	invokestatic io/putInt(I)V
Label9:
Label7:
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
