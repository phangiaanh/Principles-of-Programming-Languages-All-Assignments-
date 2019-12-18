.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static random Ljava/lang/String;
.field static one I

.method public static getRandomString()Ljava/lang/String;
Label0:
	ldc "R-A-N-D-O-M"
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
	getstatic MCClass.random Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	ldc "Kidding"
	invokestatic MCClass/getOne(Ljava/lang/String;)I
	i2f
	invokestatic io/putFloatLn(F)V
Label3:
	return
.limit stack 1
.limit locals 1
.end method

.method public static getOne(Ljava/lang/String;)I
.var 0 is s Ljava/lang/String; from Label4 to Label5
Label4:
	iconst_1
	ineg
	goto Label5
Label5:
	ireturn
.limit stack 1
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
