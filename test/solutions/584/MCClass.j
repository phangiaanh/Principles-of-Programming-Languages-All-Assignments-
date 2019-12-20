.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static maximum(FFF)F
Label0:
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is c F from Label0 to Label1
	fload_0
	fload_1
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
Label6:
	fload_1
	fload_2
	fcmpl
	ifle Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	fload_2
	goto Label1
	goto Label11
Label10:
	fload_1
	goto Label1
Label11:
Label7:
	goto Label5
Label4:
Label12:
	fload_0
	fload_2
	fcmpl
	ifle Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	fload_2
	goto Label1
	goto Label17
Label16:
	fload_0
	goto Label1
Label17:
Label13:
Label5:
Label1:
	freturn
.limit stack 10
.limit locals 3
.end method

.method public static minimum(FFF)F
Label18:
.var 0 is a F from Label18 to Label19
.var 1 is b F from Label18 to Label19
.var 2 is c F from Label18 to Label19
	fload_0
	fload_1
	fcmpl
	ifge Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifgt Label22
Label24:
	fload_1
	fload_2
	fcmpl
	ifge Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifgt Label28
	fload_2
	goto Label19
	goto Label29
Label28:
	fload_1
	goto Label19
Label29:
Label25:
	goto Label23
Label22:
Label30:
	fload_0
	fload_2
	fcmpl
	ifge Label32
	iconst_1
	goto Label33
Label32:
	iconst_0
Label33:
	ifgt Label34
	fload_2
	goto Label19
	goto Label35
Label34:
	fload_0
	goto Label19
Label35:
Label31:
Label23:
Label19:
	freturn
.limit stack 19
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label36 to Label37
Label36:
	iconst_1
	i2f
	iconst_3
	i2f
	bipush 9
	i2f
	invokestatic MCClass/minimum(FFF)F
	bipush 99
	i2f
	sipush 199
	i2f
	sipush 299
	i2f
	invokestatic MCClass/maximum(FFF)F
	fadd
	invokestatic io/putFloat(F)V
Label37:
	return
.limit stack 22
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
