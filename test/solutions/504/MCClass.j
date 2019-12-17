.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static check()Z
Label0:
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	invokestatic MCClass/check()Z
	invokestatic io/putBool(Z)V
Label3:
	return
.limit stack 2
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
