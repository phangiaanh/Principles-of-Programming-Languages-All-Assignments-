.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static str Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/getHelloString()Ljava/lang/String;
	putstatic MCClass.str Ljava/lang/String;
	getstatic MCClass.str Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static getHelloString()Ljava/lang/String;
Label2:
.var 0 is helloS [Ljava/lang/String; from Label2 to Label3
	bipush 10
	anewarray java/lang/String
	astore_0
	aload_0
	iconst_0
	ldc "The real Hello"
	aastore
	aload_0
	iconst_0
	aaload
	goto Label3
Label3:
	areturn
.limit stack 6
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
