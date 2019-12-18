.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static helloWorld(Ljava/lang/String;)Ljava/lang/String;
.var 0 is str Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "Hello World \n"
	goto Label1
Label1:
	areturn
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	ldc "AAAAAAAAAAA"
	invokestatic MCClass/helloWorld(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
	return
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
