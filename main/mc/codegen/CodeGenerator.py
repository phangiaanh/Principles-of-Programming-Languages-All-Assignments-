#Id: 1710009
#Name: Phan Gia Anh
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

import copy


#==============================SUPPORTING CLASSES==============================
class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst, isCall = False):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
        self.isCall = isCall

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value
#==============================================================================


#==============================CODE GENERATOR==============================
class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return  [
                Symbol("getInt",MType([],IntType()), CName(self.libName)),
                Symbol("putInt",MType([IntType()],VoidType()), CName(self.libName)),
                Symbol("putIntLn",MType([IntType()],VoidType()), CName(self.libName)),
                Symbol("getFloat",MType([],FloatType()), CName(self.libName)),
                Symbol("putFloat",MType([FloatType()],VoidType()), CName(self.libName)),
                Symbol("putFloatLn",MType([FloatType()],VoidType()), CName(self.libName)),
                Symbol("putBool",MType([BoolType()],VoidType()), CName(self.libName)),
                Symbol("putBoolLn",MType([BoolType()],VoidType()), CName(self.libName)),
                Symbol("putString",MType([StringType()],VoidType()), CName(self.libName)),
                Symbol("putStringLn",MType([StringType()],VoidType()), CName(self.libName)),
                Symbol("putLn",MType([],VoidType()), CName(self.libName))
                ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)
#==========================================================================


#==============================CODE VISITTOR==============================
class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    #====================METHOD GENERATOR====================
    def printCode(self, ast, code, o, typ):
        if isinstance(o, SubBody):
            self.emit.printout(code)
            if isinstance(ast, BinaryOp):
                if ast.op != "=":
                    self.emit.printout(self.emit.emitPOP(o.frame))
            if isinstance(ast, (UnaryOp, IntLiteral, FloatLiteral, BooleanLiteral, StringLiteral, Id, ArrayCell)):
                self.emit.printout(self.emit.emitPOP(o.frame))
            if isinstance(ast, CallExpr):
                if not isinstance(typ, VoidType):
                    self.emit.printout(self.emit.emitPOP(o.frame))
            return typ
        elif isinstance(o, Access):
            return code, typ


    def checkArray(self, x, e):
        globalEnvi = e.sym
        frame = e.frame
        if isinstance(x, VarDecl):
            varFound = self.lookup(x.variable, globalEnvi[::-1], lambda y: y.name)
            if isinstance(varFound.mtype, ArrayType) and varFound.value is not None:
                if isinstance(varFound.mtype.eleType, StringType):
                    VarDeclJasminArray = self.emit.emitANEWARRAY(varFound.name, varFound.mtype, varFound.value, frame)
                else:
                    VarDeclJasminArray = self.emit.emitNEWARRAY(varFound.name, varFound.mtype, varFound.value, frame)
                self.emit.printout(VarDeclJasminArray)


    def genMETHOD(self, consdecl, sym, frame):

	    isInit=(consdecl.name.name=='<init>')
	    isClinit=(consdecl.name.name=='<clinit>')   
	    isMain=(consdecl.name.name=='main' and len(consdecl.param)==0 and type(consdecl.returnType) is VoidType)    
	    # get return type
	    returnType=VoidType() if isClinit or isInit else consdecl.returnType    
	    # get method name
	    methodName=consdecl.name.name   
	    # get InType
	    inType=[]
	    if isMain: inType=[ArrayPointerType(StringType())]
	    elif isInit or isClinit: inType=[]
	    else: inType=[x.varType for x in consdecl.param]    
	    # get MType
	    mtype=MType(inType,returnType)  
	    # create prototype
	    self.emit.printout(self.emit.emitMETHOD(methodName,mtype,not isInit,frame)) 
	    # real processings
	    frame.enterScope(True)  
	    if isInit: 
	    	self.emit.printout(self.emit.emitVAR(frame.getNewIndex(),"this",ClassType(self.className),frame.getStartLabel(),frame.getEndLabel(),frame))
	    elif isMain:
	    	self.emit.printout(self.emit.emitVAR(frame.getNewIndex(),"args",ArrayPointerType(StringType()),frame.getStartLabel(),frame.getEndLabel(),frame))    
	    # param
	    stmtList=[] 
	    newFrame=frame
	    newSym=copy.copy(sym)   
	    self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(),frame))    
	    e=SubBody(newFrame,newSym)
	    if not isInit and not isClinit: 
	    	for x in consdecl.param: e=self.visit(x,e)
	    	for x in consdecl.body.member:  
	    		if type(x) is VarDecl:
	    			e=self.visit(x,e)
	    			glenv=e.sym
	    			frame=e.frame   
	    			info=self.lookup(x.variable,glenv[::-1],lambda x: x.name)   
	    			if not isInit and not isClinit:
	    				if type(info.mtype) is ArrayType and info.value is not None:
	    					if type(info.mtype.eleType) is StringType:
	    						declStmt=self.emit.emitANEWARRAY(info.name,info.mtype,info.value,frame)
	    					else:
	    						declStmt=self.emit.emitNEWARRAY(info.name,info.mtype,info.value,frame)
	    					self.emit.printout(declStmt)    
	    		else: self.visit(x,e)					    
	    glenv=e.sym
	    frame=e.frame
	    if isClinit:
	    	for x in glenv:
	    		if type(x.mtype) is ArrayType and x.value is None:
	    			if type(x.mtype.eleType) is StringType:
	    				declStmt=self.emit.emitANEWARRAY(self.className+'.'+x.name,x.mtype,x.value,frame)
	    			else:
	    				declStmt=self.emit.emitNEWARRAY(self.className+'.'+x.name,x.mtype,x.value,frame)
	    			self.emit.printout(declStmt)    
	    if isInit:
	    	self.emit.printout(self.emit.emitREADVAR("this",ClassType(self.className),0,frame))
	    	self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
	    # finish labels
	    self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame))
	    self.emit.printout(self.emit.emitRETURN(returnType,frame))
	    self.emit.printout(self.emit.emitENDMETHOD(frame))
	    frame.exitScope()
    #========================================================



    #====================VISITOR====================
    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        
        #1. Set parent class
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        #2. Create SubBody
        e = SubBody(Frame(None, None), self.env)
        
        #3.1. Visit VarDecl
        FuncList = []
        for x in ast.decl:
            if isinstance(x, VarDecl):
                e = self.visit(x, e)
            else:
                FuncList.append(x)
        
        #3.2.1. Visit FuncDecl first time
        for x in FuncList:
            e = self.visit(x, e)

        #3.2.2. Visit FuncDecl second time
        frame = e.frame
        for x in FuncList:
            sym = e.sym

            #Set frame properties as the current function
            frame.name = x.name.name
            frame.returnType = x.returnType
            
            #Generate code for every function
            self.genMETHOD(x, sym, frame)

        #4. Generate constructor for class
        self.genMETHOD(FuncDecl(Id("<init>"), [], None, Block([])), e.sym, Frame("<init>", VoidType))

        #5. Create clinit for array constructor
        for x in e.sym:
            #If x is a Symbol of a variable which type is ArrayType
            if isinstance(x.mtype, ArrayType):
                self.genMETHOD(FuncDecl(Id("<clinit>"), [], None, Block([])), e.sym, Frame("<clinit>", VoidType))
                #ArrayType constructor only need to be called once
                break

        #6. Write to file .j
        self.emit.emitEPILOG()
        return c


    def visitVarDecl(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym

        #Check if the VarDecl is global or local
        #If the indexLocal field is empty(there is no new scope), set isGlobal
        isGlobal = (len(frame.indexLocal) == 0)
        VarDeclJasmin = None
        
        if isGlobal:
            #Call emitATTRIBUTE for static variable(global)
            VarDeclJasmin = self.emit.emitATTRIBUTE(ast.variable, ast.varType, False, None)
            sym.append(Symbol(ast.variable, ast.varType, None))
        else:
            #New index for a new variable
            idx = frame.getNewIndex()
            #Call emitVAR for variable in scope
            VarDeclJasmin = self.emit.emitVAR(idx, ast.variable, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame) 
            sym.append(Symbol(ast.variable, ast.varType, idx))
        self.emit.printout(VarDeclJasmin)
        return SubBody(frame, sym)


    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym
        
        #Check the frame
        if frame is None:
            frame = Frame(ast.name.name, ast.returnType)
        else:
            #frame holds the current function's properties 
            frame.name = ast.name.name
            frame.returnType = ast.returnType

        #Return new SubBody with a new Symbol
        return SubBody(frame, sym + [Symbol(ast.name.name, MType(list(map(lambda x: x.varType, ast.param)), ast.returnType), CName(self.className))])


    def visitBinaryOp(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        #Check if the operator is "="
        if ast.op != "=":
            #Visit left and rignt first, then the operator
            leftString, leftType = self.visit(ast.left, Access(frame, nenv, False, False))
            rightString, rightType = self.visit(ast.right, Access(frame, nenv, False, False))
            
            #Boolean Operators
            if isinstance(leftType, BoolType) or isinstance(rightType, BoolType):
                if ast.op == "&&":
                    return self.printCode(ast, leftString + rightString + self.emit.emitANDOP(frame), ctxt, BoolType())
                elif ast.op == "||":
                    return self.printCode(ast, leftString + rightString + self.emit.emitOROP(frame), ctxt, BoolType())
                elif ast.op in ["==", "!="]:
                    return self.printCode(ast, leftString + rightString + self.emit.emitREOP(ast.op, BoolType(), frame), ctxt, BoolType())
            
            #Integer Operators
            if isinstance(leftType, IntType) and isinstance(rightType, IntType):
                if ast.op in ["+", "-"]:
                    return self.printCode(ast, leftString + rightString + self.emit.emitADDOP(ast.op, IntType(), frame), ctxt, IntType())
                elif ast.op == "*":
                    return self.printCode(ast, leftString + rightString + self.emit.emitMULOP(ast.op, IntType(), frame), ctxt, IntType())
                elif ast.op == "/":
                    return self.printCode(ast, leftString + rightString + self.emit.emitDIV(frame), ctxt, IntType())
                elif ast.op == "%":
                    return self.printCode(ast, leftString + rightString + self.emit.emitMOD(frame), ctxt, IntType())
                elif ast.op in [">", ">=", "<", "<=", "==", "!="]:
                    return self.printCode(ast, leftString + rightString + self.emit.emitREOP(ast.op, IntType(), frame), ctxt, BoolType())

            #Convert to Floating 
            if isinstance(leftType, IntType):
                leftString = leftString + self.emit.emitI2F(frame)
            if isinstance(rightType, IntType):
                rightString = rightString + self.emit.emitI2F(frame)

            #Floating Operators
            if ast.op in ["+", "-"]:
                return self.printCode(ast, leftString + rightString + self.emit.emitADDOP(ast.op, FloatType(), frame), ctxt, FloatType())
            elif ast.op in ["*", "/"]:
                return self.printCode(ast, leftString + rightString + self.emit.emitMULOP(ast.op, FloatType(), frame), ctxt, FloatType())
            elif ast.op in ["<", "<=", ">", ">="]:
                return self.printCode(ast, leftString + rightString + self.emit.emitFREOP(ast.op, FloatType(), frame), ctxt, FloatType())
        
        else:
            isCall = True
            
            leftString, leftType = self.visit(ast.right,Access(frame,nenv,False,False))
            rightString, rightType = self.visit(ast.right,Access(frame,nenv,False,False))
            leftString, leftType = self.visit(ast.left,Access(frame,nenv,True,True, isCall))
            rightString, rightType = self.visit(ast.right,Access(frame,nenv,False,False, isCall)) 
            leftStringExtra = self.emit.emitPOP(frame)
            if isinstance(ast.left, ArrayCell):
                if not isinstance(ast.left.arr, CallExpr):
                    leftStringExtra, _ = self.visit(ast.left,Access(frame,nenv,True,False, isCall))
            else:
                leftStringExtra, _ = self.visit(ast.left,Access(frame,nenv,True,False, isCall))


            coercion = isinstance(rightType, IntType) and isinstance(leftType, FloatType)
            rightString += self.emit.emitI2F(frame) if coercion else ""

            returnType = leftType

            if isinstance(ctxt, Access) and isCall:
                if isinstance(ast.left, ArrayCell):
                    rightString += self.emit.emitDUPX2(frame)
                else:
                    rightString += self.emit.emitDUP(frame)

            finalCode = leftString + rightString + leftStringExtra
            return self.printCode(ast, finalCode, ctxt, returnType)


    def visitUnaryOp(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        unaString, unaType = self.visit(ast.body, Access(frame, nenv, False, False))

        if ast.op != "!":
            return self.printCode(ast, unaString + self.emit.emitNEGOP(unaType, frame), ctxt, unaType)
        else:
            return self.printCode(ast, unaString + self.emit.emitNOT(unaType, frame), ctxt, unaType)


    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        #Get function symbol
        sym = self.lookup(ast.method.name, nenv[::-1], lambda x: x.name)
        
        #Get function class name and type
        cname = sym.value.value
        ctype = sym.mtype

        in_ = ""
        i = 0
        
        for x in ast.param:
            str1,typ1 = self.visit(x, Access(frame, nenv, False, False))
            in_ += str1
            if isinstance(sym.mtype.partype[i], FloatType) and isinstance(typ1, IntType):
                in_ += self.emit.emitI2F(frame)
            i += 1   

        #Concatenate two strings
        finalCode = in_ + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame)
        return self.printCode(ast, finalCode, ctxt, sym.mtype.rettype)


    def visitId(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        id_ = self.lookup(ast.name, nenv[::-1], lambda x: x.name)

        #Incase ctxt is SubBody
        if isinstance(ctxt, SubBody):
            if id_.value is not None:
                return self.printCode(ast, self.emit.emitREADVAR(id_.name, id_.mtype, id_.value, frame), ctxt, id_.mtype)
            else:
                return self.printCode(ast, self.emit.emitGETSTATIC(self.className + "." + id_.name, id_.mtype, frame), ctxt, id_.mtype)

        #ctxt must be Access
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst

        #LHS visit the first time
        if isLeft and isFirst:
            #If not ArrayType, doing nothing because this is the first time visit
            if not isinstance(id_.mtype, ArrayType) and not isinstance(id_.mtype, ArrayPointerType):
                return self.printCode(ast, "", ctxt, id_.mtype)
            else:
                #If local, emit READVAR. If global, emit GETSTATIC
                if id_.value is not None:
                    return self.printCode(ast, self.emit.emitREADVAR(id_.name, id_.mtype, id_.value, frame), ctxt, id_.mtype)
                else:
                    return self.printCode(ast, self.emit.emitGETSTATIC(self.className + "." + id_.name, id_.mtype, frame), ctxt, id_.mtype)

        #RHS
        if not isLeft and not isFirst:
            if id_.value is not None:
                return self.printCode(ast, self.emit.emitREADVAR(id_.name, id_.mtype, id_.value, frame), ctxt, id_.mtype)
            else:
                return self.printCode(ast, self.emit.emitGETSTATIC(self.className + "." + id_.name, id_.mtype, frame), ctxt, id_.mtype)
        
        #LHS visit the second time
        if isLeft and not isFirst:
            if not isinstance(id_.mtype, ArrayType) and not isinstance(id_.mtype, ArrayPointerType):
                if id_.value is None:
                    return self.printCode(ast, self.emit.emitPUTSTATIC(self.className + "." + id_.name, id_.mtype, frame), ctxt, id_.mtype)
                else:
                    return self.printCode(ast, self.emit.emitWRITEVAR(id_.name, id_.mtype, id_.value, frame), ctxt, id_.mtype)
            else:
                return self.printCode(ast, self.emit.emitASTORE(id_.mtype.eleType, frame), ctxt, id_.mtype.eleType)


    def visitArrayCell(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        if isinstance(o, SubBody):
            arrString, arrType = self.visit(ast.arr, Access(frame, nenv, True, True))
            idxString, idxType = self.visit(ast.idx, Access(frame, nenv, False, False))

            arrString += idxString
            return self.printCode(ast, arrString, ctxt, arrType.eleType)
        
        #ctxt must be Access
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst

        #LHS visit the first time
        if isLeft and isFirst:
            arrString, arrType = self.visit(ast.arr, Access(frame, nenv, True, True))
            idxString, idxType = self.visit(ast.idx, Access(frame, nenv, False, False))

            arrString += idxString
            return self.printCode(ast, arrString, ctxt, arrType.eleType)

        if not isLeft and not isFirst:
            arrString, arrType = self.visit(ast.arr, Access(frame, nenv, False, False))
            idxString, idxType = self.visit(ast.idx, Access(frame, nenv, False, False))

            arrString += idxString
            arrString += self.emit.emitALOAD(arrType.eleType, frame)
            return self.printCode(ast, arrString, ctxt, arrType.eleType)

        if isLeft and not isFirst:
            return self.visit(ast.arr, Access(frame, nenv, True, False))


    def visitIf(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        thenStmt = ast.thenStmt
        elseStmt = ast.elseStmt

        #Code for expr
        exprString, exprType = self.visit(ast.expr, Access(frame, nenv, False, False))
        self.emit.printout(exprString)

        #Create two new labels
        trueLabel = frame.getNewLabel()
        falseLabel = frame.getNewLabel()

        #Code IFTRUE + trueLabel
        self.emit.printout(self.emit.emitIFTRUE(trueLabel, frame))

        #Check elseStmt
        if elseStmt is not None:
            elseSubBody = SubBody(frame, nenv)
            elseSubBody = self.visit(elseStmt, elseSubBody)
        
        #Labels
        self.emit.printout(self.emit.emitGOTO(falseLabel,frame))
        self.emit.printout(self.emit.emitLABEL(trueLabel,frame))
        thenSubBody = SubBody(frame, nenv)
        thenSubBody = self.visit(thenStmt, thenSubBody)

        #Out
        self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
        

    def visitDowhile(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        stmtList = ast.sl

        frame.enterLoop()
        continueLabel = frame.getContinueLabel()
        breakLabel = frame.getBreakLabel()

        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))

        e = SubBody(frame, nenv)
        list(map(lambda x: self.visit(x, e), stmtList))

        exprString, exprType = self.visit(ast.exp, Access(frame, nenv, False, False))
        self.emit.printout(exprString)

        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))

        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))        
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))

        frame.exitLoop()


    def visitFor(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        #Get parameters
        init = ast.expr1
        condition = ast.expr2
        step = ast.expr3
        stmt = ast.loop

        initString, initType = self.visit(init, Access(frame, nenv, False, False))
        
        #Code for initialization
        if isinstance(ast.expr1, BinaryOp):
            if ast.expr1.op == "=":
                self.emit.printout(initString)
                self.emit.printout(self.emit.emitPOP(frame))

        frame.enterLoop()
        continueLabel = frame.getContinueLabel()
        breakLabel = frame.getBreakLabel()
        label = frame.getNewLabel()

        #Skip the update
        self.emit.printout(self.emit.emitGOTO(label, frame))   
        
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))

        #Step
        stepString, stepType = self.visit(step, Access(frame, nenv, False, False))
        if isinstance(ast.expr3, BinaryOp):
            if ast.expr3.op == "=":
                self.emit.printout(stepString)
                self.emit.printout(self.emit.emitPOP(frame))

        #Check condition
        self.emit.printout(self.emit.emitLABEL(label, frame))
        conditionString, conditionType = self.visit(condition, Access(frame, nenv, False, False))
        self.emit.printout(conditionString)
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))
        e = SubBody(frame, nenv)
        self.visit(stmt, e)


        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))        
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        frame.exitLoop()


    def visitBlock(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = copy.copy(ctxt.sym)

        #Start scope
        frame.enterScope(False)
        
        #Create new labels
        startLabel = frame.getStartLabel()
        endLabel = frame.getEndLabel()
        e = SubBody(frame, nenv)

        #Start label
        self.emit.printout(self.emit.emitLABEL(startLabel, frame))

        for x in ast.member:
            if isinstance(x, VarDecl):
                e = self.visit(x, e)
                self.checkArray(x, e)
            else:
                self.visit(x, e)

        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        frame.exitScope()
        



    def visitContinue(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        continueLabel = frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))


    def visitBreak(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        breakLabel = frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(breakLabel, frame))


    def visitReturn(self, ast, o):
        #For an easier understanding
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        if ast.expr is not None:
            exprString, exprType = self.visit(ast.expr, Access(frame, nenv, False, False))
            self.emit.printout(exprString)
            

            if isinstance(exprType, IntType) and isinstance(frame.returnType, FloatType):
                self.emit.printout(self.emit.emitI2F(frame))
        
        self.emit.printout(self.emit.emitGOTO(frame.endLabel[0], frame))
        return True


    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.printCode(ast, self.emit.emitPUSHICONST(ast.value, frame), ctxt, IntType())
    

    def visitFloatLiteral(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        return self.printCode(ast, self.emit.emitPUSHFCONST(ast.value, frame), ctxt, FloatType())


    def visitBooleanLiteral(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        return self.printCode(ast, self.emit.emitPUSHICONST(str(ast.value).lower(), frame), ctxt, BoolType())


    def visitStringLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.printCode(ast, self.emit.emitPUSHCONST('"' + ast.value + '"', StringType(), frame), ctxt, StringType())
    #===============================================

#=========================================================================
    
