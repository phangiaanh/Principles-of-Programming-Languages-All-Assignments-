.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/getHelloString()Ljava/lang/String;
	putstatic MCClass.a Ljava/lang/String;
	getstatic MCClass.a Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static getHelloString()Ljava/lang/String;
Label2:
	ldc "hello"
	goto Label3
Label3:
	areturn
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
