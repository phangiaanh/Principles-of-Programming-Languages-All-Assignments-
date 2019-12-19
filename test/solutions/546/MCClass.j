.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static PI F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 3.14
	putstatic MCClass.PI F
.var 1 is b F from Label0 to Label1
	getstatic MCClass.PI F
	fstore_1
	fload_1
	iconst_3
	i2f
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	fload_1
	iconst_2
	i2f
	fdiv
	invokestatic io/putFloat(F)V
	goto Label5
Label4:
	fload_1
	invokestatic io/putFloat(F)V
Label5:
	fload_1
	iconst_4
	i2f
	fcmpl
	ifge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	goto Label9
Label8:
	iconst_2
	i2f
	fload_1
	fmul
	invokestatic io/putFloat(F)V
Label9:
	getstatic MCClass.PI F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 8
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
