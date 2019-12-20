.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static str Ljava/lang/String;
.field static bool [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	goto Label4
Label2:
Label4:
	invokestatic MCClass/wrong()Z
	ifle Label3
Label5:
Label7:
	ldc "ABC"
	putstatic MCClass.str Ljava/lang/String;
	getstatic MCClass.str Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	getstatic MCClass.bool [Z
	iconst_0
	baload
	ifle Label8
	goto Label7
Label8:
Label6:
	goto Label2
Label3:
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public static wrong()Z
Label9:
	iconst_0
	goto Label10
Label10:
	ireturn
.limit stack 5
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

.method public static <clinit>()V
Label0:
	bipush 99
	newarray boolean
	putstatic MCClass.bool [Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
