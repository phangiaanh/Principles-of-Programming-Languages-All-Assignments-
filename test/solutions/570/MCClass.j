.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static n F

.method public static print(Ljava/lang/String;)V
Label0:
.var 0 is s Ljava/lang/String; from Label0 to Label1
	aload_0
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	ldc 3.14
	putstatic MCClass.n F
	getstatic MCClass.n F
	iconst_3
	i2f
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
Label8:
	ldc "Love PPL"
	invokestatic MCClass/print(Ljava/lang/String;)V
Label9:
	goto Label7
Label6:
Label10:
	goto Label14
Label12:
Label14:
	getstatic MCClass.n F
	bipush 7
	i2f
	fcmpl
	ifge Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label13
Label17:
	ldc "Loop for n"
	invokestatic MCClass/print(Ljava/lang/String;)V
	getstatic MCClass.n F
	iconst_1
	i2f
	fadd
	putstatic MCClass.n F
Label18:
	goto Label12
Label13:
Label11:
Label7:
Label3:
	return
.limit stack 11
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
