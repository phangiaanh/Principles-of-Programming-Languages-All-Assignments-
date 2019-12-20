.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static many F
.field static man I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	goto Label4
Label2:
	getstatic MCClass.man I
	iconst_1
	iadd
	dup
	putstatic MCClass.man I
	pop
Label4:
	getstatic MCClass.man I
	i2f
	getstatic MCClass.many F
	fcmpl
	ifgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	goto Label11
Label9:
Label11:
	iconst_1
	ifle Label10
Label12:
	ldc "Upin Ipin >.<"
	invokestatic MCClass/print(Ljava/lang/String;)V
	goto Label10
Label13:
	goto Label9
Label10:
Label8:
	goto Label2
Label3:
Label1:
	return
.limit stack 8
.limit locals 1
.end method

.method public static print(Ljava/lang/String;)V
Label14:
.var 0 is str Ljava/lang/String; from Label14 to Label15
	aload_0
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label15:
	return
.limit stack 8
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
