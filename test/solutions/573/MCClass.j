.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [I from Label0 to Label1
	bipush 10
	newarray int
	astore_1
.var 2 is n I from Label0 to Label1
.var 3 is i I from Label0 to Label1
	iconst_0
	dup
	istore_3
	pop
	goto Label4
Label2:
	iload_3
	iconst_1
	iadd
	dup
	istore_3
	pop
Label4:
	iload_3
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	aload_1
	iload_3
	iload_3
	iload_3
	imul
	iastore
Label8:
	goto Label2
Label3:
	aload_1
	bipush 10
	bipush 64
	invokestatic MCClass/findValue([III)V
Label1:
	return
.limit stack 10
.limit locals 4
.end method

.method public static findValue([III)V
Label9:
.var 0 is arr [I from Label9 to Label10
.var 1 is size I from Label9 to Label10
.var 2 is value I from Label9 to Label10
.var 3 is i I from Label9 to Label10
	iconst_0
	dup
	istore_3
	pop
	goto Label13
Label11:
	iload_3
	iconst_1
	iadd
	dup
	istore_3
	pop
Label13:
	iload_3
	iload_1
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
Label16:
	aload_0
	iload_3
	iaload
	iload_2
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label20
	goto Label21
Label20:
Label22:
	ldc "Found value("
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	invokestatic io/putInt(I)V
	ldc ") at position: "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_3
	invokestatic io/putIntLn(I)V
	goto Label12
Label23:
Label21:
Label17:
	goto Label11
Label12:
Label10:
	return
.limit stack 12
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
