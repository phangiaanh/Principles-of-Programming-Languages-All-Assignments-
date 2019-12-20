.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static message(Ljava/lang/String;)V
Label0:
.var 0 is s Ljava/lang/String; from Label0 to Label1
	ldc "Message: "
	invokestatic io/putString(Ljava/lang/String;)V
	aload_0
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static thank(Ljava/lang/String;)V
Label2:
.var 0 is s Ljava/lang/String; from Label2 to Label3
	ldc "Thanks to: "
	invokestatic io/putString(Ljava/lang/String;)V
	aload_0
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
	return
.limit stack 1
.limit locals 1
.end method

.method public static wish(Ljava/lang/String;)V
Label4:
.var 0 is s Ljava/lang/String; from Label4 to Label5
	ldc "Wish: "
	invokestatic io/putString(Ljava/lang/String;)V
	aload_0
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label5:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label6 to Label7
Label6:
	ldc "U"
	invokestatic MCClass/thank(Ljava/lang/String;)V
	ldc "Running out of ideas and time to write testcases"
	invokestatic MCClass/message(Ljava/lang/String;)V
	ldc "Sorryyyyyyyyyyyyyyyyyyyyyy"
	invokestatic MCClass/message(Ljava/lang/String;)V
	ldc "We all shall pass PPL <3"
	invokestatic MCClass/wish(Ljava/lang/String;)V
Label7:
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
