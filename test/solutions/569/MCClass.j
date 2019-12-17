.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static num I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MCClass.num I
	goto Label4
Label2:
	getstatic MCClass.num I
	iconst_2
	iadd
	putstatic MCClass.num I
Label4:
	getstatic MCClass.num I
	bipush 6
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	getstatic MCClass.num I
	iconst_3
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
	goto Label2
Label14:
Label12:
	getstatic MCClass.num I
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label8:
	goto Label2
Label3:
Label1:
	return
.limit stack 5
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
