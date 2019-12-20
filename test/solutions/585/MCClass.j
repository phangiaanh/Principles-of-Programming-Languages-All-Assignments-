.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static first I
.field static array [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
Label4:
	getstatic MCClass.array [Z
	getstatic MCClass.first I
	iconst_3
	idiv
	getstatic MCClass.array [Z
	iconst_1
	invokestatic MCClass/Return(I)I
	invokestatic MCClass/Return(I)I
	invokestatic MCClass/Return(I)I
	invokestatic MCClass/Return(I)I
	baload
	iconst_1
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	bastore
Label5:
	getstatic MCClass.array [Z
	getstatic MCClass.first I
	baload
	ifle Label3
	goto Label2
Label3:
	getstatic MCClass.array [Z
	getstatic MCClass.first I
	iconst_3
	idiv
	baload
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 14
.limit locals 1
.end method

.method public static Return(I)I
Label12:
.var 0 is a I from Label12 to Label13
	iload_0
	goto Label13
Label13:
	ireturn
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

.method public static <clinit>()V
Label0:
	sipush 1000
	newarray boolean
	putstatic MCClass.array [Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
