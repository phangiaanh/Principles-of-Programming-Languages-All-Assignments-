.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a0 I
.field static a1 [I
.field static a2 I
.field static a3 [I
.field static a4 I
.field static a5 [I
.field static f0 [F
.field static f1 F
.field static f2 [F
.field static f3 F
.field static f4 [F
.field static b0 Z
.field static b1 [Z
.field static b2 Z
.field static b3 [Z
.field static b4 Z

.method public static declareVar()V
Label0:
.var 0 is a0 I from Label0 to Label1
.var 1 is a2 I from Label0 to Label1
.var 2 is a4 I from Label0 to Label1
.var 3 is a1 [I from Label0 to Label1
	iconst_1
	newarray int
	astore_3
.var 4 is a3 [I from Label0 to Label1
	iconst_3
	newarray int
	astore 4
.var 5 is a5 [I from Label0 to Label1
	iconst_5
	newarray int
	astore 5
	getstatic MCClass.b0 Z
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 1
.limit locals 6
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	invokestatic MCClass/declareVar()V
Label3:
	return
.limit stack 0
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
	iconst_1
	newarray int
	putstatic MCClass.a1 [I
	iconst_3
	newarray int
	putstatic MCClass.a3 [I
	iconst_5
	newarray int
	putstatic MCClass.a5 [I
	iconst_1
	newarray float
	putstatic MCClass.f0 [F
	iconst_1
	newarray float
	putstatic MCClass.f2 [F
	iconst_3
	newarray float
	putstatic MCClass.f4 [F
	iconst_1
	newarray boolean
	putstatic MCClass.b1 [Z
	iconst_3
	newarray boolean
	putstatic MCClass.b3 [Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
