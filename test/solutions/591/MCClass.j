.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static b [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [F from Label0 to Label1
	iconst_3
	newarray float
	astore_1
	aload_1
	iconst_2
	iconst_3
	i2f
	fastore
	getstatic MCClass.b [Z
	sipush 998
	baload
	iconst_1
	iand
	ifgt Label2
Label4:
	aload_1
	iconst_2
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	aload_1
	iconst_2
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	faload
	iconst_3
	i2f
	fdiv
	fastore
Label5:
	goto Label3
Label2:
Label6:
	getstatic MCClass.b [Z
	iconst_0
	baload
	iconst_1
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
Label12:
	goto Label1
Label13:
Label11:
Label7:
Label3:
	aload_1
	iconst_2
	faload
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 8
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

.method public static <clinit>()V
Label0:
	sipush 999
	newarray boolean
	putstatic MCClass.b [Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
