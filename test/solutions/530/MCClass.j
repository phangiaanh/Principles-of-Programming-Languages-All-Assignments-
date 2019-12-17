.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static random Ljava/lang/String;
.field static one I

.method public static getRandomString()Ljava/lang/String;
Label0:
	ldc "random"
	goto Label1
Label1:
	areturn
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	invokestatic MCClass/getRandomString()Ljava/lang/String;
	putstatic MCClass.random Ljava/lang/String;
	invokestatic MCClass/getOne()I
	putstatic MCClass.one I
	getstatic MCClass.random Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	getstatic MCClass.one I
	invokestatic io/putIntLn(I)V
Label3:
	return
.limit stack 1
.limit locals 1
.end method

.method public static getOne()I
Label4:
	iconst_1
	goto Label5
Label5:
	ireturn
.limit stack 1
.limit locals 0
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
