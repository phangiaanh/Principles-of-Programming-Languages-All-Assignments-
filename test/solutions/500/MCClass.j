.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static cmp()V
Label0:
.var 0 is m F from Label0 to Label1
	ldc 1.2
	fstore_0
.var 1 is x I from Label0 to Label1
	iconst_2
	istore_1
	fload_0
	iconst_5
	i2f
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	iconst_2
	istore_1
Label5:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label6 to Label7
Label6:
	iconst_2
	invokestatic io/putInt(I)V
Label7:
	return
.limit stack 3
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
