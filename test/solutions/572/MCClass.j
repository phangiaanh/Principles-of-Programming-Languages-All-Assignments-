.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static findElement([III)V
.var 0 is arr [I from Label0 to Label1
.var 1 is size I from Label0 to Label1
.var 2 is key I from Label0 to Label1
Label0:
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
	goto Label4
Label2:
	iload_3
	iconst_1
	iadd
	istore_3
Label4:
	iload_3
	iload_1
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	aload_0
	iload_3
	iaload
	iload_2
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
	goto Label12
Label11:
Label13:
	ldc "Element found at position: "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_3
	iconst_1
	iadd
	invokestatic io/putIntLn(I)V
	goto Label3
Label14:
Label12:
Label8:
	goto Label2
Label3:
Label1:
	return
.limit stack 6
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label15 to Label16
Label15:
.var 1 is arr [I from Label15 to Label16
	bipush 6
	newarray int
	astore_1
.var 2 is i I from Label15 to Label16
.var 3 is n I from Label15 to Label16
.var 4 is key I from Label15 to Label16
	bipush 6
	istore_3
	iconst_3
	istore 4
	iconst_1
	istore_2
	goto Label19
Label17:
	iload_2
	iconst_1
	iadd
	istore_2
Label19:
	iload_2
	bipush 6
	if_icmpgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label18
	aload_1
	iload_2
	iconst_1
	isub
	iload_2
	iastore
	goto Label17
Label18:
	aload_1
	invokevirtual [I/clone()Ljava/lang/Object;
	checkcast [I
	iload_3
	iload 4
	invokestatic MCClass/findElement([III)V
Label16:
	return
.limit stack 10
.limit locals 5
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
