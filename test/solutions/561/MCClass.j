.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
	iconst_0
	dup
	istore_1
	pop
	goto Label4
Label2:
	iload_1
	iconst_1
	iadd
	dup
	istore_1
	pop
Label4:
	iload_1
	bipush 10
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_1
	iconst_5
	if_icmplt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
Label13:
	iload_1
	invokestatic io/putInt(I)V
	iconst_0
	dup
	istore_2
	pop
	goto Label17
Label15:
	iload_2
	iconst_1
	iadd
	dup
	istore_2
	pop
Label17:
	iload_2
	bipush 10
	if_icmpgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label16
Label20:
	iload_2
	iconst_5
	if_icmplt Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifgt Label24
	iload_2
	invokestatic io/putInt(I)V
	goto Label25
Label24:
	goto Label15
Label25:
Label21:
	goto Label15
Label16:
Label14:
	goto Label12
Label11:
	goto Label2
Label12:
Label8:
	goto Label2
Label3:
Label1:
	return
.limit stack 13
.limit locals 3
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
