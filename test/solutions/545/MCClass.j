.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass.a F
	invokestatic io/putFloat(F)V
.var 1 is a F from Label0 to Label1
	iconst_1
	i2f
	fstore_1
Label2:
.var 2 is a F from Label2 to Label3
	iconst_2
	i2f
	fstore_2
Label4:
.var 3 is a F from Label4 to Label5
	iconst_3
	i2f
	fstore_3
Label6:
.var 4 is a F from Label6 to Label7
	iconst_4
	i2f
	fstore 4
	fload 4
	invokestatic io/putFloatLn(F)V
Label7:
	fload_3
	invokestatic io/putFloatLn(F)V
Label5:
	fload_2
	invokestatic io/putFloatLn(F)V
Label3:
	fload_1
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 6
.limit locals 5
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
