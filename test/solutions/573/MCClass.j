.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is choice I from Label0 to Label1
	bipush 20
	istore_1
Label2:
Label4:
	iload_1
	bipush 17
	irem
	istore_3
	iload_3
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	goto Label9
Label8:
Label10:
	goto Label3
Label11:
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
Label5:
	iconst_1
	ifle Label3
	goto Label2
Label3:
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 4
.limit locals 4
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
