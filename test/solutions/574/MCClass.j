.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is str [Ljava/lang/String; from Label0 to Label1
	iconst_3
	anewarray java/lang/String
	astore_1
	aload_1
	iconst_0
	ldc "Oh no"
	aastore
	aload_1
	iconst_1
	ldc "Yessss"
	aastore
	aload_1
	iconst_2
	ldc "Damn....."
	aastore
.var 2 is i I from Label0 to Label1
	iconst_0
	dup
	istore_2
	pop
	goto Label4
Label2:
	iload_2
	iconst_1
	iadd
	dup
	istore_2
	pop
Label4:
	iload_2
	iconst_3
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_2
	iconst_2
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label11
	goto Label12
Label11:
	goto Label3
Label12:
	aload_1
	iload_2
	aaload
	invokestatic MCClass/clinit(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label8:
	goto Label2
Label3:
Label1:
	return
.limit stack 11
.limit locals 3
.end method

.method public static clinit(Ljava/lang/String;)Ljava/lang/String;
Label13:
.var 0 is s Ljava/lang/String; from Label13 to Label14
	ldc "Init"
	invokestatic io/putString(Ljava/lang/String;)V
	aload_0
	goto Label14
Label14:
	areturn
.limit stack 10
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
