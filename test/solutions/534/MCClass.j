.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static f F
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	i2f
	putstatic MCClass.f F
	iconst_1
	invokestatic MCClass/setInt(I)V
	getstatic MCClass.f F
	getstatic MCClass.i I
	i2f
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
Label6:
	ldc "Float is not equal to int"
	invokestatic io/putString(Ljava/lang/String;)V
Label7:
	goto Label5
Label4:
Label8:
	ldc "Float is equal to int"
	invokestatic io/putString(Ljava/lang/String;)V
Label9:
Label5:
	iconst_5
	invokestatic MCClass/setInt(I)V
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static setInt(I)V
Label10:
.var 0 is k I from Label10 to Label11
	iload_0
	putstatic MCClass.i I
Label11:
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
