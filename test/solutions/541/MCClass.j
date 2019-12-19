.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static process(I)V
Label0:
.var 0 is a I from Label0 to Label1
Label2:
.var 1 is a I from Label2 to Label3
Label4:
	iconst_1
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label5:
Label6:
.var 2 is a I from Label6 to Label7
	iconst_2
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
Label7:
Label3:
Label8:
Label10:
.var 1 is a I from Label10 to Label11
Label12:
Label14:
Label16:
	iconst_4
	istore_1
Label17:
Label15:
Label13:
	iload_1
	invokestatic io/putIntLn(I)V
Label11:
Label9:
Label1:
	return
.limit stack 5
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label18 to Label19
Label18:
Label20:
	sipush 1000
	invokestatic MCClass/process(I)V
Label21:
Label19:
	return
.limit stack 4
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
