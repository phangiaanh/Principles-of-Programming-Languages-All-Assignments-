.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is j I from Label0 to Label1
	iconst_0
	istore_1
	goto Label4
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
Label4:
	iload_1
	bipush 8
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_1
	iconst_4
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
	goto Label12
Label11:
	goto Label2
Label12:
	iload_1
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label8:
	goto Label2
Label3:
Label1:
	return
.limit stack 5
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
